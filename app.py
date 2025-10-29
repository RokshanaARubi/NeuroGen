import dash
from dash import dcc, html, Input, Output, State, callback_context
from components.auth_page import create_auth_layout
from components.dashboard_page import create_dashboard_layout
from components.predict_page import create_predict_layout
from components.profile_page import create_profile_layout, create_profile_view, create_profile_edit
from components.symptom_tracker_page import create_symptom_tracker_layout
from components.assessment_page import create_assessment_layout
from components.results_page import create_results_layout
from components.education_page import create_education_layout
from components.recommendations_page import create_recommendations_layout
from components.feedback_page import create_feedback_layout
from db.db_utils import insert_input, fetch_input_history, register_user, authenticate_user, save_user_profile, get_user_profile, fetch_user_input_history
from logic.predict import run_prediction
import json
import webbrowser
from threading import Timer


app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "NeuroGen"

# ------------------- MAIN LAYOUT -------------------
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Store(id='current-user', data=None, storage_type='session'),
    dcc.Store(id='user-profile', data={}),
    dcc.Store(id='symptom-data', data=[]),
    dcc.Store(id='assessment-data', data={}),
    
    # Navigation Header (only shown when logged in)
    html.Div(id='nav-header'),
    
    # Page Content
    html.Div(id='page-content')
])

# ------------------- NAVIGATION HEADER -------------------
def create_nav_header(user, current_path='/'):
    if not user:
        return html.Div()
    
    nav_links = [
        {'name': 'Dashboard', 'path': '/'},
        {'name': 'Assessment', 'path': '/assessment'},
        {'name': 'Prediction', 'path': '/predict'},
        {'name': 'Results', 'path': '/results'},
        {'name': 'Education', 'path': '/education'},
        {'name': 'Recommendations', 'path': '/recommendations'},
        {'name': 'Symptom Tracker', 'path': '/symptoms'},
        {'name': 'Community', 'path': '/community'},
        {'name': 'Profile', 'path': '/profile'},
    ]
    
    return html.Div([
        html.Div([
            # Left side: Logo and navigation links
            html.Div([
                html.H2("NeuroGen", className="nav-title"),
                html.Div([
                    *[dcc.Link(
                        link['name'], 
                        href=link['path'], 
                        className=f"nav-link {'active' if current_path == link['path'] else ''}"
                    ) for link in nav_links if link['name'] != 'Profile'],
                ], className="nav-links")
            ], className="nav-left"),
            
            # Right side: Profile and logout button
            html.Div([
                dcc.Link(
                    '👤 Profile', 
                    href='/profile', 
                    className=f"nav-link profile-link {'active' if current_path == '/profile' else ''}"
                ),
                html.Span(f"Welcome, {user}", className="welcome-text"),
                html.Button('Logout', id='logout-button', n_clicks=0, className="logout-btn")
            ], className="nav-right")
            
        ], className="nav-container")
    ], className="nav-header")

# ------------------- COGNITIVE ASSESSMENT -------------------
@app.callback(
    Output('cognitive-results', 'children'),
    Input('submit-cognitive', 'n_clicks'),
    [State('q1-orientation', 'value'),
     State('q2-registration', 'value'),
     State('q3-calculation', 'value'),
     State('q4-recall', 'value'),
     State('q5-language', 'value'),
     State('q6-repetition', 'value'),
     State('q7-comprehension', 'value'),
     State('q8-reading', 'value'),
     State('q9-writing', 'value'),
     State('q10-copying', 'value')],
    prevent_initial_call=True
)
def calculate_cognitive_score(n_clicks, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
    print(f"🧠 COGNITIVE CALLBACK TRIGGERED - Clicks: {n_clicks}")
    print(f"📝 Answers received: Q1={q1}, Q2={q2}, Q3={q3}, Q4={q4}, Q5={q5}, Q6={q6}, Q7={q7}, Q8={q8}, Q9={q9}, Q10={q10}")
    
    if not n_clicks:
        print("❌ No clicks - returning empty")
        return ""
    
    # Check if all questions are answered
    answers = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    unanswered = [i+1 for i, answer in enumerate(answers) if answer is None]
    
    if unanswered:
        print(f"❌ Unanswered questions: {unanswered}")
        return html.Div([
            html.H4("❌ Please Complete All Questions", style={'color': '#dc3545', 'marginBottom': '10px'}),
            html.P(f"Missing answers for questions: {', '.join(map(str, unanswered))}", style={'color': '#666'})
        ], className="alert alert-error", style={'padding': '15px', 'border': '1px solid #dc3545'})
    
    # Calculate total score (MMSE-like, max 30 points)
    total_score = sum(answers)
    print(f"✅ Score calculated: {total_score}/30")
    
    # Interpret results
    if total_score >= 27:
        risk_level = "Normal cognitive function"
        color = "#28a745"
        interpretation = "Your cognitive screening results are within normal range. Continue maintaining brain-healthy habits."
        recommendations = [
            "Continue regular physical and mental exercise",
            "Maintain social connections", 
            "Eat a balanced diet rich in antioxidants",
            "Get quality sleep (7-8 hours per night)"
        ]
    elif total_score >= 24:
        risk_level = "Mild cognitive changes"
        color = "#ffc107"
        interpretation = "Mild cognitive changes detected. This may be normal aging or early signs that need monitoring."
        recommendations = [
            "Schedule regular cognitive check-ups",
            "Increase mental stimulation activities",
            "Review medications with your doctor",
            "Consider neuropsychological testing"
        ]
    elif total_score >= 18:
        risk_level = "Moderate cognitive impairment"
        color = "#fd7e14"
        interpretation = "Significant cognitive changes detected. Consider consulting a healthcare provider for comprehensive evaluation."
        recommendations = [
            "Consult with a neurologist or geriatrician",
            "Complete comprehensive neuropsychological testing",
            "Review cardiovascular risk factors",
            "Consider brain imaging if recommended"
        ]
    else:
        risk_level = "Severe cognitive impairment"
        color = "#dc3545"
        interpretation = "Severe cognitive impairment detected. Urgent medical consultation recommended."
        recommendations = [
            "Seek immediate medical attention",
            "Consult with a dementia specialist",
            "Ensure safety at home",
            "Discuss care planning with family"
        ]
    
    print(f"✅ Returning results: {risk_level}")
    
    return html.Div([
        html.H3("📊 Cognitive Assessment Results", style={'marginBottom': '20px', 'color': '#333'}),
        
        # Score Card
        html.Div([
            html.Div([
                html.H4(f"Total Score: {total_score}/30", style={
                    'marginBottom': '10px', 
                    'color': color,
                    'fontSize': '24px'
                }),
                html.P(f"Assessment: {risk_level}", style={
                    'color': color, 
                    'fontWeight': 'bold', 
                    'fontSize': '18px',
                    'marginBottom': '10px'
                }),
                html.P(interpretation, style={'lineHeight': '1.5'})
            ], style={
                'padding': '25px',
                'border': f'3px solid {color}',
                'borderRadius': '12px',
                'backgroundColor': '#f8f9fa',
                'textAlign': 'center'
            })
        ], style={'marginBottom': '30px'}),
        
        # Detailed Breakdown
        html.Div([
            html.H4("Detailed Breakdown", style={'marginBottom': '15px', 'color': '#333'}),
            html.Div([
                html.Div([
                    html.Table([
                        html.Tr([html.Td("Orientation to Time:", style={'padding': '8px', 'fontWeight': 'bold'}), html.Td(f"{q1}/5", style={'padding': '8px'})]),
                        html.Tr([html.Td("Immediate Memory:", style={'padding': '8px', 'fontWeight': 'bold'}), html.Td(f"{q2}/3", style={'padding': '8px'})]),
                        html.Tr([html.Td("Attention/Calculation:", style={'padding': '8px', 'fontWeight': 'bold'}), html.Td(f"{q3}/5", style={'padding': '8px'})]),
                        html.Tr([html.Td("Delayed Recall:", style={'padding': '8px', 'fontWeight': 'bold'}), html.Td(f"{q4}/3", style={'padding': '8px'})]),
                        html.Tr([html.Td("Language/Naming:", style={'padding': '8px', 'fontWeight': 'bold'}), html.Td(f"{q5}/2", style={'padding': '8px'})]),
                    ], style={'width': '100%', 'marginBottom': '10px'})
                ], style={'flex': '1'}),
                
                html.Div([
                    html.Table([
                        html.Tr([html.Td("Repetition:", style={'padding': '8px', 'fontWeight': 'bold'}), html.Td(f"{q6}/1", style={'padding': '8px'})]),
                        html.Tr([html.Td("Comprehension:", style={'padding': '8px', 'fontWeight': 'bold'}), html.Td(f"{q7}/3", style={'padding': '8px'})]),
                        html.Tr([html.Td("Reading:", style={'padding': '8px', 'fontWeight': 'bold'}), html.Td(f"{q8}/1", style={'padding': '8px'})]),
                        html.Tr([html.Td("Writing:", style={'padding': '8px', 'fontWeight': 'bold'}), html.Td(f"{q9}/1", style={'padding': '8px'})]),
                        html.Tr([html.Td("Visual-Spatial:", style={'padding': '8px', 'fontWeight': 'bold'}), html.Td(f"{q10}/1", style={'padding': '8px'})]),
                    ], style={'width': '100%'})
                ], style={'flex': '1'})
            ], style={'display': 'flex', 'gap': '20px', 'flexWrap': 'wrap'})
        ], style={'marginBottom': '30px'}),
        
        # Recommendations
        html.Div([
            html.H4("Recommended Next Steps", style={'marginBottom': '15px', 'color': '#333'}),
            html.Ul([html.Li(rec) for rec in recommendations], style={'lineHeight': '1.6', 'marginBottom': '15px'}),
            html.P("💡 This is a screening tool only. For formal diagnosis, consult with a healthcare professional.", 
                  style={'fontStyle': 'italic', 'color': '#666'})
        ], style={
            'padding': '20px',
            'backgroundColor': '#e7f3ff',
            'borderRadius': '8px',
            'borderLeft': '4px solid #007bff'
        })
    ])

# ------------------- RISK FACTORS SAVING -------------------
@app.callback(
    Output('risk-factors-output', 'children'),
    Input('save-factors-btn', 'n_clicks'),
    [State('family-history-checklist', 'value'),
     State('lifestyle-factors-checklist', 'value'),
     State('medical-history-checklist', 'value')],
    prevent_initial_call=True
)
def save_risk_factors(n_clicks, family_history, lifestyle_factors, medical_history):
    print(f"💾 SAVE RISK FACTORS CALLBACK - Clicks: {n_clicks}")
    print(f"📋 Factors: Family={family_history}, Lifestyle={lifestyle_factors}, Medical={medical_history}")
    
    if not n_clicks:
        return ""
    
    # Count risk factors (excluding 'none' options and protective factors)
    protective_factors = [f for f in lifestyle_factors if f in ['exercise', 'healthy_diet', 'social']]
    risk_factors = (
        len([f for f in family_history if f != 'none']) +
        len([f for f in lifestyle_factors if f not in ['exercise', 'healthy_diet', 'social']]) +
        len([f for f in medical_history if f != 'none'])
    )
    
    print(f"✅ Risk factors counted: {risk_factors} risk factors, {len(protective_factors)} protective factors")
    
    return html.Div([
        html.Span("✅ Risk Factors Saved! ", style={'color': '#28a745', 'fontWeight': 'bold'}),
        html.Span(f"({risk_factors} risk factors, {len(protective_factors)} protective factors)")
    ], style={'padding': '10px', 'backgroundColor': '#d4edda', 'borderRadius': '4px'})

# ------------------- GENETIC ANALYSIS -------------------
@app.callback(
    Output('genetic-analysis-output', 'children'),
    Input('analyze-genetic-btn', 'n_clicks'),
    [State('snp-input-assessment', 'value')],
    prevent_initial_call=True
)
def analyze_genetic_data(n_clicks, snp_input):
    print(f"🧬 GENETIC ANALYSIS CALLBACK - Clicks: {n_clicks}, Input: {snp_input}")
    
    if not n_clicks:
        return ""
    
    if not snp_input:
        return html.Div([
            html.H4("❌ No SNP Data", style={'color': '#dc3545'}),
            html.P("Please enter SNP values in the text area above.")
        ], className="alert alert-error")
    
    try:
        # Use your existing prediction function
        result = run_prediction(snp_input)
        print(f"🔮 Prediction result: {result}")
        
        # Format results
        result_display = []
        for disease, info in result.items():
            risk_level = info['risk_level']
            risk_class = "risk-moderate"
            if "low" in risk_level.lower():
                risk_class = "risk-low"
            elif "high" in risk_level.lower():
                risk_class = "risk-high"
            
            result_display.append(html.Div([
                html.H4(disease, style={'marginBottom': '10px', 'color': '#333'}),
                html.Div([
                    html.Span("Risk Level: ", style={'fontWeight': 'bold'}),
                    html.Span(risk_level, className=f"risk-badge {risk_class}")
                ], style={'marginBottom': '10px'}),
                html.Ul([html.Li(detail, style={'marginBottom': '5px'}) for detail in info.get('details', [])])
            ], style={
                'padding': '15px',
                'border': '1px solid #ddd',
                'borderRadius': '8px',
                'marginBottom': '15px',
                'backgroundColor': '#f8f9fa'
            }))
        
        return html.Div([
            html.H3("🧬 Genetic Analysis Results", style={'marginBottom': '20px', 'color': '#333'}),
            html.Div(result_display)
        ])
        
    except Exception as e:
        print(f"💥 Genetic analysis error: {e}")
        return html.Div([
            html.H4("❌ Analysis Error", style={'color': '#dc3545'}),
            html.P(f"Error analyzing genetic data: {str(e)}")
        ], className="alert alert-error")

# ------------------- GENETIC UPLOAD -------------------
@app.callback(
    Output('genetic-upload-output', 'children'),
    Input('upload-genetic-data', 'contents'),
    State('upload-genetic-data', 'filename'),
    prevent_initial_call=True
)
def handle_upload(contents, filename):
    print(f"📁 UPLOAD CALLBACK - File: {filename}")
    
    if contents is not None:
        return html.Div([
            html.Span("✅ ", style={'color': 'green'}),
            html.Span(f"File uploaded: {filename}"),
            html.Br(),
            html.Small("Note: File processing would be implemented in a production system", 
                      style={'color': '#666', 'fontStyle': 'italic'})
        ], style={'padding': '10px', 'backgroundColor': '#d4edda', 'borderRadius': '4px'})
    
    return ""
# ------------------- RESULTS PAGE DATA -------------------
@app.callback(
    Output('results-history-table', 'children'),
    Input('url', 'pathname'),
    State('current-user', 'data'),
    prevent_initial_call=True
)
def update_results_page(pathname, username):
    print(f"📊 Updating results page - Path: {pathname}, User: {username}")
    
    # Only update when we're actually on the results page
    if pathname != '/results' or not username:
        return html.Div("No data available")
    
    try:
        # Fetch prediction history for the current user only
        from db.db_utils import fetch_user_input_history
        history = fetch_user_input_history(username, limit=10)
        
        if not history:
            return html.Div(
                "No prediction history found. Complete some assessments to see your results here.",
                style={'textAlign': 'center', 'padding': '40px', 'color': '#666'}
            )
        
        # Create table
        table_header = [
            html.Thead(html.Tr([
                html.Th("SNP Input", style={'padding': '12px'}),
                html.Th("Result", style={'padding': '12px'}),
                html.Th("Date", style={'padding': '12px'})
            ]))
        ]
        
        table_rows = []
        for row in history:
            username_val, snp_input, result_val, timestamp = row
            
            # Parse result for display
            try:
                parsed = json.loads(result_val) if isinstance(result_val, str) else result_val
                if isinstance(parsed, dict):
                    result_display = []
                    for disease, info in parsed.items():
                        risk_level = info.get('risk_level', 'Unknown')
                        risk_class = "risk-moderate"
                        if "low" in risk_level.lower():
                            risk_class = "risk-low"
                        elif "high" in risk_level.lower():
                            risk_class = "risk-high"
                            
                        result_display.append(html.Div([
                            html.Strong(f"{disease}: "),
                            html.Span(risk_level, className=f"risk-badge {risk_class}")
                        ]))
                else:
                    result_display = html.Div(str(parsed))
            except:
                result_display = html.Div(str(result_val))
            
            table_rows.append(html.Tr([
                html.Td(snp_input, style={'padding': '12px', 'borderBottom': '1px solid #e0e0e0'}),
                html.Td(result_display, style={'padding': '12px', 'borderBottom': '1px solid #e0e0e0'}),
                html.Td(
                    timestamp.strftime("%Y-%m-%d %H:%M") if timestamp else "Unknown",
                    style={'padding': '12px', 'borderBottom': '1px solid #e0e0e0'}
                )
            ]))
        
        return html.Table(table_header + [html.Tbody(table_rows)], 
                         style={'width': '100%', 'borderCollapse': 'collapse'})
        
    except Exception as e:
        print(f"💥 Error loading results: {e}")
        return html.Div([
            html.H4("Error loading results", style={'color': '#dc3545'}),
            html.P(str(e))
        ], className="alert alert-error")

# ------------------- PAGE ROUTER -------------------
@app.callback(
    [Output('page-content', 'children'),
     Output('nav-header', 'children')],
    [Input('url', 'pathname'),
     Input('current-user', 'data')]
)
def display_page(pathname, user):
    print(f"🔍 Display page - User: {user}, Path: {pathname}")
    
    # If no user, always show auth page
    if not user:
        print("🚫 No user - showing auth page")
        return create_auth_layout(), html.Div()
    
    # User is authenticated - show appropriate page with navigation
    nav_header = create_nav_header(user, pathname)
    print(f"✅ User authenticated: {user}, showing path: {pathname}")
    
    # Route to correct page
    if pathname == '/profile':
        return create_profile_layout(), nav_header
    elif pathname == '/symptoms':
        return create_symptom_tracker_layout(), nav_header
    elif pathname == '/assessment':
        return create_assessment_layout(), nav_header
    elif pathname == '/predict':
        return create_predict_layout(), nav_header
    elif pathname == '/results':
        return create_results_layout(), nav_header
    elif pathname == '/education':
        return create_education_layout(), nav_header
    elif pathname == '/recommendations':
        return create_recommendations_layout(), nav_header
    elif pathname == '/community':
        return create_feedback_layout(), nav_header
    else:  # Default to dashboard for '/' or any other path
        return create_dashboard_layout(), nav_header
    
from dash import callback_context, ALL, MATCH

# ------------------- PROFILE MODE TOGGLE -------------------
@app.callback(
    [Output('profile-view-mode', 'style'),
     Output('profile-edit-mode', 'style'),
     Output('profile-view-mode', 'children'),
     Output('profile-edit-mode', 'children')],
    Input('profile-mode', 'value'),
    prevent_initial_call=True
)
def toggle_profile_mode(mode):
    print(f"🔄 Profile mode: {mode}")
    
    if mode == 'view':
        return (
            {'display': 'block'},
            {'display': 'none'},
            create_profile_view(),
            dash.no_update
        )
    else:
        return (
            {'display': 'none'},
            {'display': 'block'},
            dash.no_update,
            create_profile_edit()
        )

# ------------------- LOAD PROFILE DATA -------------------
@app.callback(
    [Output('user-fullname', 'value'),
     Output('user-age', 'value'),
     Output('user-gender', 'value'),
     Output('user-ethnicity', 'value'),
     Output('user-email', 'value'),
     Output('user-phone', 'value'),
     Output('medical-conditions', 'value'),
     Output('family-medical-history', 'value'),
     Output('current-medications', 'value'),
     Output('allergies', 'value'),
     Output('diet-pattern', 'value'),
     Output('exercise-frequency', 'value'),
     Output('sleep-quality', 'value'),
     Output('smoking-status', 'value'),
     Output('alcohol-consumption', 'value'),
     Output('stress-level', 'value'),
     Output('emergency-name', 'value'),
     Output('emergency-relationship', 'value'),
     Output('emergency-phone', 'value'),
     Output('emergency-email', 'value')],
    Input('profile-edit-mode', 'children'),  # Trigger when edit mode loads
    State('current-user', 'data'),
    prevent_initial_call=True
)
def load_profile_data(edit_mode_children, username):
    print(f"📥 Loading profile data for: {username}")
    
    if username:
        profile_data = get_user_profile(username)
        
        if profile_data:
            print(f"✅ Loaded profile data: {profile_data}")
            return (
                profile_data.get('fullname', ''),
                profile_data.get('age', ''),
                profile_data.get('gender', ''),
                profile_data.get('ethnicity', ''),
                profile_data.get('email', ''),
                profile_data.get('phone', ''),
                profile_data.get('medical_conditions', []),
                profile_data.get('family_history', []),
                profile_data.get('medications', ''),
                profile_data.get('allergies', ''),
                profile_data.get('diet', ''),
                profile_data.get('exercise', ''),
                profile_data.get('sleep', ''),
                profile_data.get('smoking', ''),
                profile_data.get('alcohol', ''),
                profile_data.get('stress', ''),
                profile_data.get('emergency_name', ''),
                profile_data.get('emergency_relationship', ''),
                profile_data.get('emergency_phone', ''),
                profile_data.get('emergency_email', '')
            )
    
    # Return empty values if no data
    return [''] * 20

# ------------------- SAVE PROFILE DATA -------------------
@app.callback(
    Output('profile-save-output', 'children'),
    Input('save-profile-btn', 'n_clicks'),
    [State('user-fullname', 'value'),
     State('user-age', 'value'),
     State('user-gender', 'value'),
     State('user-ethnicity', 'value'),
     State('user-email', 'value'),
     State('user-phone', 'value'),
     State('medical-conditions', 'value'),
     State('family-medical-history', 'value'),
     State('current-medications', 'value'),
     State('allergies', 'value'),
     State('diet-pattern', 'value'),
     State('exercise-frequency', 'value'),
     State('sleep-quality', 'value'),
     State('smoking-status', 'value'),
     State('alcohol-consumption', 'value'),
     State('stress-level', 'value'),
     State('emergency-name', 'value'),
     State('emergency-relationship', 'value'),
     State('emergency-phone', 'value'),
     State('emergency-email', 'value'),
     State('current-user', 'data')],
    prevent_initial_call=True
)
def save_profile_data(n_clicks, fullname, age, gender, ethnicity, email, phone, 
                     medical_conditions, family_history, medications, allergies,
                     diet, exercise, sleep, smoking, alcohol, stress,
                     emergency_name, emergency_relationship, emergency_phone, emergency_email, username):
    
    if not n_clicks or not username:
        return ""
    
    print(f"💾 Saving profile data for: {username}")
    
    # Prepare profile data
    profile_data = {
        'fullname': fullname,
        'age': age,
        'gender': gender,
        'ethnicity': ethnicity,
        'email': email,
        'phone': phone,
        'medical_conditions': medical_conditions or [],
        'family_history': family_history or [],
        'medications': medications,
        'allergies': allergies,
        'diet': diet,
        'exercise': exercise,
        'sleep': sleep,
        'smoking': smoking,
        'alcohol': alcohol,
        'stress': stress,
        'emergency_name': emergency_name,
        'emergency_relationship': emergency_relationship,
        'emergency_phone': emergency_phone,
        'emergency_email': emergency_email
    }
    
    # Save to database
    success = save_user_profile(username, profile_data)
    
    if success:
        return html.Div([
            html.Span("✅ Profile information saved successfully!", 
                     style={'color': '#28a745', 'fontWeight': 'bold', 'fontSize': '16px'}),
            html.Br(),
            html.Span("Switch to 'View Profile' to see your updated information.", 
                     style={'color': '#666', 'fontSize': '14px'})
        ], style={
            'padding': '15px',
            'backgroundColor': '#d4edda',
            'border': '1px solid #c3e6cb',
            'borderRadius': '8px',
            'textAlign': 'center'
        })
    else:
        return html.Div([
            html.Span("❌ Error saving profile information", 
                     style={'color': '#dc3545', 'fontWeight': 'bold', 'fontSize': '16px'}),
            html.Br(),
            html.Span("Please try again.", 
                     style={'color': '#666', 'fontSize': '14px'})
        ], style={
            'padding': '15px',
            'backgroundColor': '#f8d7da',
            'border': '1px solid #f5c6cb',
            'borderRadius': '8px',
            'textAlign': 'center'
        })

# ------------------- DISPLAY PROFILE VIEW -------------------
@app.callback(
    [Output('personal-info-view', 'children'),
     Output('medical-info-view', 'children'),
     Output('lifestyle-info-view', 'children'),
     Output('emergency-info-view', 'children')],
    [Input('profile-mode', 'value'),  # Trigger when mode changes
     Input('current-user', 'data'),   # Trigger when user changes  
     Input('save-profile-btn', 'n_clicks'),  # Trigger when profile is saved
     Input('url', 'pathname')],  # NEW: Trigger when URL changes to profile page
    [State('current-user', 'data')],
    prevent_initial_call=True
)
def display_profile_view(mode, user_data, save_clicks, pathname, username):
    print(f"👀 Display profile view triggered - Mode: {mode}, User: {username}, Save clicks: {save_clicks}, Path: {pathname}")
    
    # Only update when we're on the profile page, in view mode, and have a user
    if pathname == '/profile' and mode == 'view' and username:
        print(f"📊 Loading profile data for view mode: {username}")
        profile_data = get_user_profile(username)
        
        if not profile_data:
            print("❌ No profile data found")
            no_data_msg = html.Div([
                html.H4("No Profile Data Found", style={'color': '#666', 'textAlign': 'center', 'marginBottom': '10px'}),
                html.P("Click 'Edit Profile' to add your information.", style={'color': '#999', 'textAlign': 'center'})
            ], style={'padding': '40px', 'textAlign': 'center', 'border': '2px dashed #ddd', 'borderRadius': '8px'})
            return no_data_msg, no_data_msg, no_data_msg, no_data_msg
        
        print(f"✅ Profile data found: {len(profile_data)} keys")
        
        # Personal Information
        personal_info = html.Div([
            html.Table([
                html.Tr([html.Td("Full Name:", style={'fontWeight': 'bold', 'padding': '8px', 'width': '200px'}), 
                         html.Td(profile_data.get('fullname', 'Not provided') or 'Not provided')]),
                html.Tr([html.Td("Age:", style={'fontWeight': 'bold', 'padding': '8px'}), 
                         html.Td(str(profile_data.get('age', 'Not provided')) or 'Not provided')]),
                html.Tr([html.Td("Gender:", style={'fontWeight': 'bold', 'padding': '8px'}), 
                         html.Td(profile_data.get('gender', 'Not provided') or 'Not provided')]),
                html.Tr([html.Td("Ethnicity:", style={'fontWeight': 'bold', 'padding': '8px'}), 
                         html.Td(profile_data.get('ethnicity', 'Not provided') or 'Not provided')]),
                html.Tr([html.Td("Email:", style={'fontWeight': 'bold', 'padding': '8px'}), 
                         html.Td(profile_data.get('email', 'Not provided') or 'Not provided')]),
                html.Tr([html.Td("Phone:", style={'fontWeight': 'bold', 'padding': '8px'}), 
                         html.Td(profile_data.get('phone', 'Not provided') or 'Not provided')]),
            ], style={'width': '100%'})
        ])
        
        # Medical Information
        medical_conditions = [condition.replace('_', ' ').title() for condition in profile_data.get('medical_conditions', []) if condition != 'none']
        family_history_list = [condition.replace('_', ' ').title() for condition in profile_data.get('family_history', []) if condition != 'none_family']
        
        medical_info = html.Div([
            html.Div([
                html.H4("Existing Conditions", style={'color': '#333', 'marginBottom': '10px'}),
                html.Ul([html.Li(condition) for condition in medical_conditions]) if medical_conditions else html.P("No conditions reported", style={'color': '#666', 'fontStyle': 'italic'})
            ], style={'marginBottom': '15px'}),
            html.Div([
                html.H4("Family History", style={'color': '#333', 'marginBottom': '10px'}),
                html.Ul([html.Li(condition) for condition in family_history_list]) if family_history_list else html.P("No significant family history", style={'color': '#666', 'fontStyle': 'italic'})
            ], style={'marginBottom': '15px'}),
            html.Div([
                html.H4("Current Medications", style={'color': '#333', 'marginBottom': '10px'}),
                html.P(profile_data.get('medications', 'None reported') or 'None reported', style={'color': '#666'})
            ], style={'marginBottom': '15px'}),
            html.Div([
                html.H4("Allergies", style={'color': '#333', 'marginBottom': '10px'}),
                html.P(profile_data.get('allergies', 'None reported') or 'None reported', style={'color': '#666'})
            ])
        ])
        
        # Lifestyle Information
        lifestyle_map = {
            'diet': 'Diet',
            'exercise': 'Exercise Frequency', 
            'sleep': 'Sleep Quality',
            'smoking': 'Smoking Status',
            'alcohol': 'Alcohol Consumption',
            'stress': 'Stress Level'
        }
        
        lifestyle_info = html.Div([
            html.Table([
                html.Tr([html.Td(f"{lifestyle_map[key]}:", style={'fontWeight': 'bold', 'padding': '8px', 'width': '200px'}), 
                         html.Td(profile_data.get(key, 'Not provided') or 'Not provided')])
                for key in lifestyle_map.keys()
            ], style={'width': '100%'})
        ])
        
        # Emergency Contact
        emergency_info = html.Div([
            html.Table([
                html.Tr([html.Td("Name:", style={'fontWeight': 'bold', 'padding': '8px', 'width': '200px'}), 
                         html.Td(profile_data.get('emergency_name', 'Not provided') or 'Not provided')]),
                html.Tr([html.Td("Relationship:", style={'fontWeight': 'bold', 'padding': '8px'}), 
                         html.Td(profile_data.get('emergency_relationship', 'Not provided') or 'Not provided')]),
                html.Tr([html.Td("Phone:", style={'fontWeight': 'bold', 'padding': '8px'}), 
                         html.Td(profile_data.get('emergency_phone', 'Not provided') or 'Not provided')]),
                html.Tr([html.Td("Email:", style={'fontWeight': 'bold', 'padding': '8px'}), 
                         html.Td(profile_data.get('emergency_email', 'Not provided') or 'Not provided')]),
            ], style={'width': '100%'})
        ])
        
        return personal_info, medical_info, lifestyle_info, emergency_info
    
    return dash.no_update, dash.no_update, dash.no_update, dash.no_update
def create_nav_header(user, current_path='/'):
    if not user:
        return html.Div([
            html.Div([
                html.Div([
                    html.H2("NeuroGen", className="nav-title"),
                ], className="nav-left"),
                
                # Right side: Sign in/Sign up buttons with black text
                html.Div([
                    html.Button('Sign In', id='signin-button', className='nav-signin-btn', style={'color': '#222'}),
                    html.Button('Sign Up', id='signup-button', className='nav-signup-btn', style={'color': '#222'})
                ], className="nav-right")
                
            ], className="nav-container")
        ], className="nav-header")
    
    # Existing code for logged-in user
    nav_links = [
        {'name': 'Dashboard', 'path': '/'},
        {'name': 'Assessment', 'path': '/assessment'},
        {'name': 'Prediction', 'path': '/predict'},
        {'name': 'Results', 'path': '/results'},
        {'name': 'Education', 'path': '/education'},
        {'name': 'Recommendations', 'path': '/recommendations'},
        {'name': 'Symptom Tracker', 'path': '/symptoms'},
        {'name': 'Community', 'path': '/community'},
        {'name': 'Profile', 'path': '/profile'},
    ]
    
    return html.Div([
        html.Div([
            # Left side: Logo and navigation links
            html.Div([
                html.H2("NeuroGen", className="nav-title"),
                html.Div([
                    *[dcc.Link(
                        link['name'], 
                        href=link['path'], 
                        className=f"nav-link {'active' if current_path == link['path'] else ''}"
                    ) for link in nav_links if link['name'] != 'Profile'],
                ], className="nav-links")
            ], className="nav-left"),
            
            # Right side: Profile and logout button
            html.Div([
                dcc.Link(
                    '👤 Profile', 
                    href='/profile', 
                    className=f"nav-link profile-link {'active' if current_path == '/profile' else ''}"
                ),
                html.Span(f"Welcome, {user}", className="welcome-text"),
                html.Button('Logout', id='logout-button', n_clicks=0, className="logout-btn")
            ], className="nav-right")
            
        ], className="nav-container")
    ], className="nav-header")

# ------------------- NAVIGATION AUTH BUTTONS -------------------
@app.callback(
    Output('url', 'pathname', allow_duplicate=True),
    [Input('signin-button', 'n_clicks'),
     Input('signup-button', 'n_clicks')],
    prevent_initial_call=True
)
def handle_nav_auth_buttons(signin_clicks, signup_clicks):
    ctx = callback_context
    if not ctx.triggered:
        return dash.no_update
    
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if trigger_id == 'signin-button' and signin_clicks:
        print("🔄 Navigation: Switching to auth page for sign in")
        return "/auth"
    elif trigger_id == 'signup-button' and signup_clicks:
        print("🔄 Navigation: Switching to auth page for sign up")
        return "/auth"
    
    return dash.no_update

# ------------------- AUTH PAGE REDIRECT -------------------
@app.callback(
    Output('page-content', 'children', allow_duplicate=True),
    Input('url', 'pathname'),
    State('current-user', 'data'),
    prevent_initial_call=True
)
def redirect_to_auth(pathname, user):
    if pathname == '/auth' and not user:
        print("🔄 Redirecting to auth page")
        return create_auth_layout()
    return dash.no_update
# ------------------- AUTH CALLBACKS (COMBINED) -------------------
@app.callback(
    [Output('current-user', 'data'),
     Output('auth-output', 'children'),
     Output('url', 'pathname'),
     Output('auth-tabs', 'value')],
    [Input('login-button', 'n_clicks'),
     Input('register-button', 'n_clicks'),
     Input('goto-register', 'n_clicks')],
    [State('login-username', 'value'),
     State('login-password', 'value'),
     State('reg-username', 'value'),
     State('reg-password', 'value'),
     State('reg-email', 'value')],
    prevent_initial_call=True
)
def handle_auth(login_clicks, register_clicks, goto_register_clicks, 
                login_username, login_password, reg_username, reg_password, reg_email):
    ctx = callback_context
    if not ctx.triggered:
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update
    
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print(f"🔐 Auth triggered by: {trigger_id}")
    
    # Handle Login
    if trigger_id == 'login-button' and login_clicks:
        print(f"🔐 Login attempt - Username: {login_username}")
        
        if not login_username or not login_password:
            return None, html.Div("Please enter username and password", style={'color': 'red'}), dash.no_update, dash.no_update
        
        try:
            auth_result = authenticate_user(login_username, login_password)
            print(f"🔑 Authentication result: {auth_result}")
            
            if auth_result:
                print(f"✅ Login successful for: {login_username}")
                return login_username, html.Div("Login successful!", style={'color': 'green'}), "/", dash.no_update
            else:
                print("❌ Login failed - invalid credentials")
                return None, html.Div("Invalid username or password", style={'color': 'red'}), dash.no_update, dash.no_update
        except Exception as e:
            print(f"💥 Login error: {e}")
            return None, html.Div(f"Login error: {str(e)}", style={'color': 'red'}), dash.no_update, dash.no_update
    
    # Handle Register
    elif trigger_id == 'register-button' and register_clicks:
        print(f"📝 Register attempt - Username: {reg_username}")
        
        if not reg_username or not reg_password:
            return dash.no_update, html.Div("Username and password required", style={'color': 'red'}), dash.no_update, 'tab-register'
        
        try:
            reg_result = register_user(reg_username, reg_password, reg_email)
            print(f"📋 Registration result: {reg_result}")
            
            if reg_result:
                return dash.no_update, html.Div("Registration successful! Please login.", style={'color': 'green'}), dash.no_update, 'tab-login'
            else:
                return dash.no_update, html.Div("Username already exists", style={'color': 'red'}), dash.no_update, 'tab-register'
        except Exception as e:
            print(f"💥 Registration error: {e}")
            return dash.no_update, html.Div(f"Registration error: {str(e)}", style={'color': 'red'}), dash.no_update, 'tab-register'
    
    # Handle Tab Switch (goto register)
    elif trigger_id == 'goto-register' and goto_register_clicks:
        print("🔄 Switching to register tab")
        return dash.no_update, dash.no_update, dash.no_update, 'tab-register'
    
    return dash.no_update, dash.no_update, dash.no_update, dash.no_update

# ------------------- LOGOUT -------------------
@app.callback(
    [Output('current-user', 'data', allow_duplicate=True),
     Output('url', 'pathname', allow_duplicate=True)],
    Input('logout-button', 'n_clicks'),
    prevent_initial_call=True
)
def handle_logout(n_clicks):
    print(f"🚪 Logout clicked: {n_clicks}")
    if n_clicks and n_clicks > 0:
        return None, "/"
    return dash.no_update, dash.no_update

# ------------------- PREDICTION -------------------
@app.callback(
    [Output('result-output', 'children'),
     Output('history-table', 'data')],
    Input('submit-button', 'n_clicks'),
    [State('snp-input', 'value'),
     State('current-user', 'data')],
    prevent_initial_call=True
)
def handle_prediction(n_clicks, snp_input, username):
    print(f"🔮 Prediction request - User: {username}, SNPs: {snp_input}")
    
    if not snp_input:
        return "Please enter SNPs to predict.", []

    try:
        # Run prediction
        result = run_prediction(snp_input)
        print(f"📊 Prediction result: {result}")

        # Insert record into DB
        insert_input(snp_input, json.dumps(result), username)
        print("💾 Prediction saved to database")

        # Fetch history
        history = fetch_input_history()
        history_data = []
        for row in history:
            username_val = row[0] if row[0] else ""
            snp_val = row[1]
            result_val = row[2]

            # Try to parse JSON for table display
            try:
                parsed = json.loads(result_val)
            except Exception:
                parsed = result_val

            # Format result for table as plain text
            if isinstance(parsed, dict):
                table_text = "\n".join(
                    f"{disease}: {info['risk_level']}\n" +
                    "\n".join(f"- {detail}" for detail in info.get('details', []))
                    for disease, info in parsed.items()
                )
            else:
                table_text = str(parsed)

            history_data.append({
                "username": username_val,
                "snp_input": snp_val,
                "result": table_text,
                "timestamp": row[3].strftime("%Y-%m-%d %H:%M") if row[3] else ""
            })

        # Pretty display for most recent prediction
        result_lines = []
        for disease, info in result.items():
            result_lines.append(html.H4(disease))
            
            # Add risk level with appropriate badge
            risk_level = info['risk_level']
            risk_class = "risk-moderate"  # default
            if "low" in risk_level.lower():
                risk_class = "risk-low"
            elif "high" in risk_level.lower():
                risk_class = "risk-high"
                
            result_lines.append(
                html.Div([
                    html.Span(f"Risk Level: ", style={'fontWeight': 'bold'}),
                    html.Span(risk_level, className=f"risk-badge {risk_class}")
                ])
            )
            
            details_list = html.Ul([html.Li(detail) for detail in info.get('details', [])])
            result_lines.append(details_list)
            result_lines.append(html.Hr())

        pretty_display = html.Div(result_lines, className="results-container")

        return pretty_display, history_data

    except Exception as e:
        print(f"💥 Prediction error: {e}")
        return html.Div(f"Error during prediction: {e}", className="alert alert-error"), []


# ------------------- SYMPTOM TRACKER -------------------
@app.callback(
    Output('symptom-output', 'children'),
    Input('log-symptom', 'n_clicks'),
    [State('symptom-type', 'value'),
     State('symptom-severity', 'value'),
     State('symptom-notes', 'value')],
    prevent_initial_call=True
)
def log_symptom(n_clicks, symptom_type, severity, notes):
    if not n_clicks or n_clicks == 0:
        return ""
    
    if not symptom_type:
        return html.Div("Please select a symptom type.", className="alert alert-error")
    
    print(f"📝 Logging symptom: {symptom_type}, Severity: {severity}")
    # Here you would save to database
    return html.Div(f"Symptom logged: {symptom_type} (Severity: {severity})", 
                   className="alert alert-success")

# ------------------- APP LAUNCH -------------------
if __name__ == '__main__':
    print("🚀 Starting NeuroGen App...")
    # Create test user if doesn't exist
    try:
        register_user("testuser", "password123", "test@example.com")
        register_user("demo", "demo123", "demo@example.com")
        print("✅ Test users created")
    except Exception as e:
        print(f"⚠️  Could not create test users: {e}")
    
    Timer(1, lambda: webbrowser.open("http://127.0.0.1:8050")).start()
    app.run(debug=True, port=8050)