from dash import html, dcc

def create_profile_layout():
    return html.Div([
        html.H1("User Profile", style={'textAlign': 'center', 'marginBottom': '30px'}),
        
        html.Div([
            # Profile View/Edit Toggle
            html.Div([
                dcc.RadioItems(
                    id='profile-mode',
                    options=[
                        {'label': ' 👁️ View Profile', 'value': 'view'},
                        {'label': ' ✏️ Edit Profile', 'value': 'edit'}
                    ],
                    value='view',
                    inline=True,
                    labelStyle={'marginRight': '20px', 'fontWeight': 'bold', 'fontSize': '16px'}
                )
            ], style={'textAlign': 'center', 'marginBottom': '30px'}),
            
            # Profile View Mode
            html.Div(id='profile-view-mode', style={'display': 'block'}),
            
            # Profile Edit Mode
            html.Div(id='profile-edit-mode', style={'display': 'none'})
            
        ], style={'maxWidth': '1200px', 'margin': '0 auto', 'padding': '20px'})
    ])

# This function returns the complete edit form with all components
def create_profile_edit():
    return html.Div([
        # Personal Information Section
        html.Div([
            html.H2("👤 Personal Information", style={'color': '#6a46f0', 'marginBottom': '20px'}),
            
            html.Div([
                html.Div([
                    html.Label("Full Name", className='form-label'),
                    dcc.Input(id='user-fullname', type='text', placeholder='Enter your full name', className='form-input')
                ], className='form-group'),
                
                html.Div([
                    html.Label("Age", className='form-label'),
                    dcc.Input(id='user-age', type='number', placeholder='Enter your age', min=18, max=120, className='form-input')
                ], className='form-group'),
                
                html.Div([
                    html.Label("Gender", className='form-label'),
                    dcc.Dropdown(
                        id='user-gender',
                        options=[
                            {'label': 'Male', 'value': 'male'},
                            {'label': 'Female', 'value': 'female'},
                            {'label': 'Other', 'value': 'other'},
                            {'label': 'Prefer not to say', 'value': 'prefer_not'}
                        ],
                        placeholder='Select gender',
                        className='form-input'
                    )
                ], className='form-group'),
                
                html.Div([
                    html.Label("Ethnicity", className='form-label'),
                    dcc.Dropdown(
                        id='user-ethnicity',
                        options=[
                            {'label': 'Asian', 'value': 'asian'},
                            {'label': 'Black or African American', 'value': 'black'},
                            {'label': 'Hispanic or Latino', 'value': 'hispanic'},
                            {'label': 'White', 'value': 'white'},
                            {'label': 'Native American', 'value': 'native_american'},
                            {'label': 'Pacific Islander', 'value': 'pacific_islander'},
                            {'label': 'Multiracial', 'value': 'multiracial'},
                            {'label': 'Other', 'value': 'other'},
                            {'label': 'Prefer not to say', 'value': 'prefer_not'}
                        ],
                        placeholder='Select ethnicity',
                        className='form-input'
                    )
                ], className='form-group'),
                
                html.Div([
                    html.Label("Email Address", className='form-label'),
                    dcc.Input(id='user-email', type='email', placeholder='Enter your email', className='form-input')
                ], className='form-group'),
                
                html.Div([
                    html.Label("Phone Number", className='form-label'),
                    dcc.Input(id='user-phone', type='tel', placeholder='Enter your phone number', className='form-input')
                ], className='form-group')
                
            ], style={'display': 'grid', 'gridTemplateColumns': '1fr 1fr', 'gap': '20px'})
            
        ], className='card', style={'marginBottom': '30px'}),
        
        # Medical History Section
        html.Div([
            html.H2("🏥 Medical History", style={'color': '#6a46f0', 'marginBottom': '20px'}),
            
            html.Div([
                html.Div([
                    html.Label("Existing Medical Conditions", className='form-label'),
                    dcc.Checklist(
                        id='medical-conditions',
                        options=[
                            {'label': ' High blood pressure', 'value': 'hypertension'},
                            {'label': ' Diabetes', 'value': 'diabetes'},
                            {'label': ' High cholesterol', 'value': 'cholesterol'},
                            {'label': ' Heart disease', 'value': 'heart_disease'},
                            {'label': ' Stroke', 'value': 'stroke'},
                            {'label': ' Depression/Anxiety', 'value': 'depression'},
                            {'label': ' Thyroid disorders', 'value': 'thyroid'},
                            {'label': ' Autoimmune diseases', 'value': 'autoimmune'},
                            {'label': ' None of the above', 'value': 'none'}
                        ],
                        value=[],
                        labelStyle={'display': 'block', 'marginBottom': '8px'}
                    )
                ], className='form-group'),
                
                html.Div([
                    html.Label("Family Medical History", className='form-label'),
                    dcc.Checklist(
                        id='family-medical-history',
                        options=[
                            {'label': ' Alzheimer\'s disease', 'value': 'alzheimers'},
                            {'label': ' Parkinson\'s disease', 'value': 'parkinsons'},
                            {'label': ' Other dementia', 'value': 'dementia'},
                            {'label': ' Stroke', 'value': 'stroke_family'},
                            {'label': ' Heart disease', 'value': 'heart_disease_family'},
                            {'label': ' Diabetes', 'value': 'diabetes_family'},
                            {'label': ' Cancer', 'value': 'cancer'},
                            {'label': ' No significant family history', 'value': 'none_family'}
                        ],
                        value=[],
                        labelStyle={'display': 'block', 'marginBottom': '8px'}
                    )
                ], className='form-group'),
                
                html.Div([
                    html.Label("Current Medications", className='form-label'),
                    dcc.Textarea(
                        id='current-medications', 
                        placeholder='List your current medications...', 
                        style={'width': '100%', 'height': '80px', 'padding': '10px', 'border': '1px solid #ddd', 'borderRadius': '4px'}
                    )
                ], className='form-group'),
                
                html.Div([
                    html.Label("Allergies", className='form-label'),
                    dcc.Textarea(
                        id='allergies', 
                        placeholder='List any allergies...', 
                        style={'width': '100%', 'height': '60px', 'padding': '10px', 'border': '1px solid #ddd', 'borderRadius': '4px'}
                    )
                ], className='form-group')
                
            ], style={'display': 'grid', 'gridTemplateColumns': '1fr 1fr', 'gap': '30px'})
            
        ], className='card', style={'marginBottom': '30px'}),
        
        # Lifestyle Section
        html.Div([
            html.H2("💪 Lifestyle & Habits", style={'color': '#6a46f0', 'marginBottom': '20px'}),
            
            html.Div([
                html.Div([
                    html.Label("Dietary Pattern", className='form-label'),
                    dcc.Dropdown(
                        id='diet-pattern',
                        options=[
                            {'label': 'Mediterranean', 'value': 'mediterranean'},
                            {'label': 'Vegetarian', 'value': 'vegetarian'},
                            {'label': 'Vegan', 'value': 'vegan'},
                            {'label': 'Keto/Low-carb', 'value': 'keto'},
                            {'label': 'Standard American', 'value': 'standard'},
                            {'label': 'Pescatarian', 'value': 'pescatarian'},
                            {'label': 'Other', 'value': 'other'}
                        ],
                        placeholder='Select your primary diet',
                        className='form-input'
                    )
                ], className='form-group'),
                
                html.Div([
                    html.Label("Exercise Frequency", className='form-label'),
                    dcc.Dropdown(
                        id='exercise-frequency',
                        options=[
                            {'label': 'Daily', 'value': 'daily'},
                            {'label': '3-5 times per week', 'value': 'regular'},
                            {'label': '1-2 times per week', 'value': 'weekly'},
                            {'label': 'Rarely', 'value': 'rarely'},
                            {'label': 'Never', 'value': 'never'}
                        ],
                        placeholder='Select exercise frequency',
                        className='form-input'
                    )
                ], className='form-group'),
                
                html.Div([
                    html.Label("Sleep Quality", className='form-label'),
                    dcc.Dropdown(
                        id='sleep-quality',
                        options=[
                            {'label': 'Excellent (7-9 hours, restful)', 'value': 'excellent'},
                            {'label': 'Good (6-7 hours, mostly restful)', 'value': 'good'},
                            {'label': 'Fair (5-6 hours, interrupted)', 'value': 'fair'},
                            {'label': 'Poor (<5 hours, restless)', 'value': 'poor'}
                        ],
                        placeholder='Select sleep quality',
                        className='form-input'
                    )
                ], className='form-group'),
                
                html.Div([
                    html.Label("Smoking Status", className='form-label'),
                    dcc.Dropdown(
                        id='smoking-status',
                        options=[
                            {'label': 'Never smoked', 'value': 'never'},
                            {'label': 'Former smoker', 'value': 'former'},
                            {'label': 'Current smoker', 'value': 'current'},
                            {'label': 'Occasional smoker', 'value': 'occasional'}
                        ],
                        placeholder='Select smoking status',
                        className='form-input'
                    )
                ], className='form-group'),
                
                html.Div([
                    html.Label("Alcohol Consumption", className='form-label'),
                    dcc.Dropdown(
                        id='alcohol-consumption',
                        options=[
                            {'label': 'Never', 'value': 'never'},
                            {'label': 'Occasionally (1-4 drinks/week)', 'value': 'occasional'},
                            {'label': 'Moderately (5-10 drinks/week)', 'value': 'moderate'},
                            {'label': 'Regularly (10+ drinks/week)', 'value': 'regular'},
                            {'label': 'Heavy (15+ drinks/week)', 'value': 'heavy'}
                        ],
                        placeholder='Select alcohol consumption',
                        className='form-input'
                    )
                ], className='form-group'),
                
                html.Div([
                    html.Label("Stress Level", className='form-label'),
                    dcc.Dropdown(
                        id='stress-level',
                        options=[
                            {'label': 'Low', 'value': 'low'},
                            {'label': 'Moderate', 'value': 'moderate'},
                            {'label': 'High', 'value': 'high'},
                            {'label': 'Very High', 'value': 'very_high'}
                        ],
                        placeholder='Select stress level',
                        className='form-input'
                    )
                ], className='form-group')
                
            ], style={'display': 'grid', 'gridTemplateColumns': '1fr 1fr', 'gap': '20px'})
            
        ], className='card', style={'marginBottom': '30px'}),
        
        # Emergency Contact Section
        html.Div([
            html.H2("🚨 Emergency Contact", style={'color': '#6a46f0', 'marginBottom': '20px'}),
            
            html.Div([
                html.Div([
                    html.Label("Emergency Contact Name", className='form-label'),
                    dcc.Input(
                        id='emergency-name', 
                        type='text', 
                        placeholder='Full name of emergency contact', 
                        className='form-input'
                    )
                ], className='form-group'),
                
                html.Div([
                    html.Label("Relationship", className='form-label'),
                    dcc.Input(
                        id='emergency-relationship', 
                        type='text', 
                        placeholder='Relationship to you', 
                        className='form-input'
                    )
                ], className='form-group'),
                
                html.Div([
                    html.Label("Phone Number", className='form-label'),
                    dcc.Input(
                        id='emergency-phone', 
                        type='tel', 
                        placeholder='Emergency contact phone number', 
                        className='form-input'
                    )
                ], className='form-group'),
                
                html.Div([
                    html.Label("Email", className='form-label'),
                    dcc.Input(
                        id='emergency-email', 
                        type='email', 
                        placeholder='Emergency contact email', 
                        className='form-input'
                    )
                ], className='form-group')
                
            ], style={'display': 'grid', 'gridTemplateColumns': '1fr 1fr', 'gap': '20px'})
            
        ], className='card', style={'marginBottom': '30px'}),
        
        # Save Button - THIS IS THE MISSING COMPONENT
        html.Div([
            html.Button(
                '💾 Save Profile Information', 
                id='save-profile-btn', 
                n_clicks=0, 
                className='btn btn-primary', 
                style={'padding': '12px 30px', 'fontSize': '16px'}
            ),
            html.Div(id='profile-save-output', style={'marginTop': '15px'})
        ], style={'textAlign': 'center'})
        
    ])

def create_profile_view():
    return html.Div([
        html.Div([
            # Personal Information Card
            html.Div([
                html.H2("👤 Personal Information", style={'color': '#6a46f0', 'marginBottom': '20px', 'borderBottom': '2px solid #f0f0f0', 'paddingBottom': '10px'}),
                html.Div(id='personal-info-view')
            ], className='card', style={'marginBottom': '30px'}),
            
            # Medical History Card
            html.Div([
                html.H2("🏥 Medical History", style={'color': '#6a46f0', 'marginBottom': '20px', 'borderBottom': '2px solid #f0f0f0', 'paddingBottom': '10px'}),
                html.Div(id='medical-info-view')
            ], className='card', style={'marginBottom': '30px'}),
            
            # Lifestyle Card
            html.Div([
                html.H2("💪 Lifestyle & Habits", style={'color': '#6a46f0', 'marginBottom': '20px', 'borderBottom': '2px solid #f0f0f0', 'paddingBottom': '10px'}),
                html.Div(id='lifestyle-info-view')
            ], className='card', style={'marginBottom': '30px'}),
            
            # Emergency Contact Card
            html.Div([
                html.H2("🚨 Emergency Contact", style={'color': '#6a46f0', 'marginBottom': '20px', 'borderBottom': '2px solid #f0f0f0', 'paddingBottom': '10px'}),
                html.Div(id='emergency-info-view')
            ], className='card', style={'marginBottom': '30px'})
            
        ])
    ])