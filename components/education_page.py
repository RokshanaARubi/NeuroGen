from dash import html, dcc, Input, Output, State, callback, no_update
import dash

def create_education_layout():
    return html.Div([
        html.H1("Educational Resources", style={'textAlign': 'center', 'marginBottom': '30px'}),
        
        # Modal for displaying detailed content
        html.Div([
            html.Div([
                html.Div([
                    html.H3(id="modal-title", style={'marginBottom': '20px', 'color': '#333'}),
                    html.Div(id="modal-content"),
                    html.Button("Close", id="close-modal", 
                               style={
                                   'marginTop': '20px', 
                                   'padding': '10px 20px',
                                   'backgroundColor': '#6c757d',
                                   'color': 'white',
                                   'border': 'none',
                                   'borderRadius': '5px',
                                   'cursor': 'pointer'
                               })
                ], style={'padding': '30px', 'maxHeight': '80vh', 'overflowY': 'auto'})
            ], style={
                'position': 'fixed', 
                'top': '50%', 
                'left': '50%', 
                'transform': 'translate(-50%, -50%)',
                'backgroundColor': 'white',
                'padding': '20px',
                'borderRadius': '10px',
                'boxShadow': '0 4px 8px rgba(0,0,0,0.2)',
                'zIndex': '1000',
                'maxWidth': '600px',
                'width': '90%',
                'maxHeight': '90vh',
                'overflow': 'hidden'
            })
        ], id="modal", style={
            'display': 'none',
            'position': 'fixed',
            'top': '0',
            'left': '0',
            'width': '100%',
            'height': '100%',
            'backgroundColor': 'rgba(0,0,0,0.5)',
            'zIndex': '999'
        }),
        
        html.Div([
            # Resource Categories
            html.Div([
                html.H3("Neurological Disorders", style={'color': '#2c3e50', 'marginBottom': '20px'}),
                
                html.Div([
                    html.Div([
                        html.H4("Alzheimer's Disease", style={'color': '#2c3e50', 'marginBottom': '10px'}),
                        html.P("Learn about symptoms, progression, and management strategies.", style={'color': '#666', 'lineHeight': '1.5'}),
                        html.Button("Read More", id="btn-alzheimers", 
                                   style={
                                       'marginTop': '10px',
                                       'padding': '10px 20px',
                                       'backgroundColor': '#3498db',
                                       'color': 'white',
                                       'border': 'none',
                                       'borderRadius': '5px',
                                       'cursor': 'pointer',
                                       'transition': 'background-color 0.3s'
                                   })
                    ], style={
                        'padding': '20px', 
                        'border': '1px solid #ddd', 
                        'margin': '10px', 
                        'borderRadius': '8px', 
                        'flex': '1',
                        'minWidth': '300px',
                        'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
                        'transition': 'transform 0.2s'
                    }, className='resource-card'),
                    
                    html.Div([
                        html.H4("Parkinson's Disease", style={'color': '#2c3e50', 'marginBottom': '10px'}),
                        html.P("Information on tremors, treatment options, and lifestyle adjustments.", style={'color': '#666', 'lineHeight': '1.5'}),
                        html.Button("Read More", id="btn-parkinsons",
                                   style={
                                       'marginTop': '10px',
                                       'padding': '10px 20px',
                                       'backgroundColor': '#3498db',
                                       'color': 'white',
                                       'border': 'none',
                                       'borderRadius': '5px',
                                       'cursor': 'pointer',
                                       'transition': 'background-color 0.3s'
                                   })
                    ], style={
                        'padding': '20px', 
                        'border': '1px solid #ddd', 
                        'margin': '10px', 
                        'borderRadius': '8px', 
                        'flex': '1',
                        'minWidth': '300px',
                        'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
                        'transition': 'transform 0.2s'
                    }, className='resource-card'),
                    
                    html.Div([
                        html.H4("Multiple Sclerosis", style={'color': '#2c3e50', 'marginBottom': '10px'}),
                        html.P("Understanding MS symptoms and modern treatment approaches.", style={'color': '#666', 'lineHeight': '1.5'}),
                        html.Button("Read More", id="btn-ms",
                                   style={
                                       'marginTop': '10px',
                                       'padding': '10px 20px',
                                       'backgroundColor': '#3498db',
                                       'color': 'white',
                                       'border': 'none',
                                       'borderRadius': '5px',
                                       'cursor': 'pointer',
                                       'transition': 'background-color 0.3s'
                                   })
                    ], style={
                        'padding': '20px', 
                        'border': '1px solid #ddd', 
                        'margin': '10px', 
                        'borderRadius': '8px', 
                        'flex': '1',
                        'minWidth': '300px',
                        'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
                        'transition': 'transform 0.2s'
                    }, className='resource-card')
                ], style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'center'})
            ]),
            
            # Video Resources
            html.Div([
                html.H3("Video Explanations", style={'marginTop': '40px', 'color': '#2c3e50', 'marginBottom': '20px'}),
                html.Div([
                    html.Div([
                        html.H5("Understanding Alzheimer's Progression", style={'color': '#2c3e50', 'marginBottom': '10px'}),
                        html.P("3:45 min video", style={'color': '#666'}),
                        html.Button("Watch Video", id="btn-video-alzheimers",
                                   style={
                                       'marginTop': '10px',
                                       'padding': '10px 20px',
                                       'backgroundColor': '#e74c3c',
                                       'color': 'white',
                                       'border': 'none',
                                       'borderRadius': '5px',
                                       'cursor': 'pointer',
                                       'transition': 'background-color 0.3s'
                                   })
                    ], style={
                        'padding': '20px', 
                        'border': '1px solid #ddd', 
                        'margin': '10px', 
                        'borderRadius': '8px', 
                        'textAlign': 'center',
                        'minWidth': '250px',
                        'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'
                    }),
                    
                    html.Div([
                        html.H5("Parkinson's Exercise Guidelines", style={'color': '#2c3e50', 'marginBottom': '10px'}),
                        html.P("5:20 min video", style={'color': '#666'}),
                        html.Button("Watch Video", id="btn-video-parkinsons",
                                   style={
                                       'marginTop': '10px',
                                       'padding': '10px 20px',
                                       'backgroundColor': '#e74c3c',
                                       'color': 'white',
                                       'border': 'none',
                                       'borderRadius': '5px',
                                       'cursor': 'pointer',
                                       'transition': 'background-color 0.3s'
                                   })
                    ], style={
                        'padding': '20px', 
                        'border': '1px solid #ddd', 
                        'margin': '10px', 
                        'borderRadius': '8px', 
                        'textAlign': 'center',
                        'minWidth': '250px',
                        'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'
                    }),
                ], style={'display': 'flex', 'justifyContent': 'center', 'flexWrap': 'wrap'})
            ]),
            
            # FAQ Section
            html.Div([
                html.H3("Frequently Asked Questions", style={'marginTop': '40px', 'color': '#2c3e50', 'marginBottom': '20px'}),
                html.Div([
                    html.Details([
                        html.Summary("What is the difference between normal aging and dementia?", 
                                   style={'fontWeight': 'bold', 'cursor': 'pointer', 'padding': '10px'}),
                        html.P("Normal aging involves occasional memory lapses, while dementia affects daily functioning and involves progressive cognitive decline.", 
                              style={'padding': '15px', 'backgroundColor': '#f8f9fa', 'borderRadius': '5px', 'marginTop': '5px'})
                    ], style={'margin': '15px 0', 'border': '1px solid #ddd', 'borderRadius': '5px'}),
                    
                    html.Details([
                        html.Summary("Can lifestyle changes reduce neurological disease risk?", 
                                   style={'fontWeight': 'bold', 'cursor': 'pointer', 'padding': '10px'}),
                        html.P("Yes, regular exercise, cognitive stimulation, and a healthy diet can help reduce risk and slow progression.", 
                              style={'padding': '15px', 'backgroundColor': '#f8f9fa', 'borderRadius': '5px', 'marginTop': '5px'})
                    ], style={'margin': '15px 0', 'border': '1px solid #ddd', 'borderRadius': '5px'}),
                    
                    html.Details([
                        html.Summary("How accurate are genetic predictions for neurological diseases?", 
                                   style={'fontWeight': 'bold', 'cursor': 'pointer', 'padding': '10px'}),
                        html.P("Genetic markers provide risk probabilities, not certainties. They should be interpreted alongside other clinical factors.", 
                              style={'padding': '15px', 'backgroundColor': '#f8f9fa', 'borderRadius': '5px', 'marginTop': '5px'})
                    ], style={'margin': '15px 0', 'border': '1px solid #ddd', 'borderRadius': '5px'})
                ])
            ])
            
        ], style={'maxWidth': '1200px', 'margin': '0 auto', 'padding': '20px'})
    ])

# Callback to handle all button clicks and modal display
@callback(
    [Output("modal", "style"),
     Output("modal-title", "children"),
     Output("modal-content", "children")],
    [Input("btn-alzheimers", "n_clicks"),
     Input("btn-parkinsons", "n_clicks"),
     Input("btn-ms", "n_clicks"),
     Input("btn-video-alzheimers", "n_clicks"),
     Input("btn-video-parkinsons", "n_clicks"),
     Input("close-modal", "n_clicks")],
    prevent_initial_call=True
)
def toggle_modal(alz_clicks, park_clicks, ms_clicks, vid_alz_clicks, vid_park_clicks, close_clicks):
    ctx = dash.callback_context
    
    if not ctx.triggered:
        return no_update, no_update, no_update
    
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    # Close modal if close button is clicked
    if button_id == "close-modal":
        return {'display': 'none'}, no_update, no_update
    
    # Define content for each button
    content_map = {
        "btn-alzheimers": {
            "title": "Alzheimer's Disease - Detailed Information",
            "content": html.Div([
                html.H4("Symptoms", style={'color': '#2c3e50', 'marginBottom': '15px'}),
                html.Ul([
                    html.Li("Memory loss that disrupts daily life"),
                    html.Li("Challenges in planning or solving problems"),
                    html.Li("Difficulty completing familiar tasks"),
                    html.Li("Confusion with time or place"),
                    html.Li("Trouble understanding visual images and spatial relationships"),
                    html.Li("New problems with words in speaking or writing")
                ], style={'lineHeight': '1.6', 'marginBottom': '20px'}),
                
                html.H4("Progression", style={'color': '#2c3e50', 'marginBottom': '15px'}),
                html.P("Alzheimer's typically progresses through three main stages: mild (early-stage), moderate (middle-stage), and severe (late-stage). Each stage brings different challenges and requires different care approaches.", 
                      style={'lineHeight': '1.6', 'marginBottom': '20px'}),
                
                html.H4("Management Strategies", style={'color': '#2c3e50', 'marginBottom': '15px'}),
                html.Ul([
                    html.Li("Medications to manage symptoms (cholinesterase inhibitors, memantine)"),
                    html.Li("Cognitive stimulation activities and therapy"),
                    html.Li("Regular physical exercise and mobility support"),
                    html.Li("Healthy diet (Mediterranean diet recommended)"),
                    html.Li("Safety modifications at home"),
                    html.Li("Caregiver support and education programs")
                ], style={'lineHeight': '1.6'})
            ])
        },
        "btn-parkinsons": {
            "title": "Parkinson's Disease - Detailed Information",
            "content": html.Div([
                html.H4("Common Symptoms", style={'color': '#2c3e50', 'marginBottom': '15px'}),
                html.Ul([
                    html.Li("Tremors or shaking (usually starting in hands)"),
                    html.Li("Bradykinesia (slowness of movement)"),
                    html.Li("Muscle rigidity and stiffness"),
                    html.Li("Impaired balance and coordination"),
                    html.Li("Changes in speech and writing"),
                    html.Li("Loss of automatic movements")
                ], style={'lineHeight': '1.6', 'marginBottom': '20px'}),
                
                html.H4("Treatment Options", style={'color': '#2c3e50', 'marginBottom': '15px'}),
                html.Ul([
                    html.Li("Levodopa and other dopamine-enhancing medications"),
                    html.Li("Deep brain stimulation (DBS) for advanced cases"),
                    html.Li("Physical therapy for mobility and balance"),
                    html.Li("Occupational therapy for daily activities"),
                    html.Li("Speech therapy for communication challenges")
                ], style={'lineHeight': '1.6', 'marginBottom': '20px'}),
                
                html.H4("Lifestyle Adjustments", style={'color': '#2c3e50', 'marginBottom': '15px'}),
                html.Ul([
                    html.Li("Regular exercise program (tai chi, yoga, walking)"),
                    html.Li("Balanced nutrition with adequate fiber"),
                    html.Li("Fall prevention strategies at home"),
                    html.Li("Stress management techniques"),
                    html.Li("Support groups and counseling services")
                ], style={'lineHeight': '1.6'})
            ])
        },
        "btn-ms": {
            "title": "Multiple Sclerosis - Detailed Information",
            "content": html.Div([
                html.H4("Common Symptoms", style={'color': '#2c3e50', 'marginBottom': '15px'}),
                html.Ul([
                    html.Li("Fatigue that worsens as the day progresses"),
                    html.Li("Walking difficulties and balance problems"),
                    html.Li("Numbness or tingling in various body parts"),
                    html.Li("Muscle spasms and weakness"),
                    html.Li("Vision problems (blurred vision, pain with eye movement)"),
                    html.Li("Bladder and bowel problems"),
                    html.Li("Cognitive changes and emotional symptoms")
                ], style={'lineHeight': '1.6', 'marginBottom': '20px'}),
                
                html.H4("Modern Treatment Approaches", style={'color': '#2c3e50', 'marginBottom': '15px'}),
                html.Ul([
                    html.Li("Disease-modifying therapies (DMTs) to reduce relapses"),
                    html.Li("Corticosteroids for acute relapses"),
                    html.Li("Symptom-specific medications for pain, spasms, etc."),
                    html.Li("Physical and occupational therapy"),
                    html.Li("Lifestyle management strategies")
                ], style={'lineHeight': '1.6', 'marginBottom': '20px'}),
                
                html.H4("Disease Management", style={'color': '#2c3e50', 'marginBottom': '15px'}),
                html.P("MS management focuses on treating relapses, managing symptoms, and modifying disease progression through comprehensive care approaches including regular monitoring and adaptive strategies.", 
                      style={'lineHeight': '1.6'})
            ])
        },
        "btn-video-alzheimers": {
            "title": "Understanding Alzheimer's Progression",
            "content": html.Div([
                html.P("This 3:45 minute video explains the stages of Alzheimer's disease progression and what to expect at each stage.", 
                      style={'lineHeight': '1.6', 'marginBottom': '20px'}),
                
                html.Div([
                    html.Div([
                        html.Img(
                            src="/assets/video-placeholder-alzheimers.jpg",
                            style={'width': '100%', 'maxWidth': '500px', 'height': 'auto', 'borderRadius': '8px'}
                        ),
                        html.P("Video: Understanding Alzheimer's Progression", 
                              style={'textAlign': 'center', 'color': '#666', 'marginTop': '10px'})
                    ], style={'textAlign': 'center', 'margin': '20px 0'})
                ]),
                
                html.P("Key topics covered in this video:", style={'fontWeight': 'bold', 'marginBottom': '10px'}),
                html.Ul([
                    html.Li("Early signs and symptoms to watch for"),
                    html.Li("Middle stage changes and care needs"),
                    html.Li("Late stage progression and support requirements"),
                    html.Li("Management strategies for each stage"),
                    html.Li("Caregiver tips and resources")
                ], style={'lineHeight': '1.6', 'marginBottom': '20px'}),
                
                html.Div([
                    html.Button("Play Video", 
                               style={
                                   'padding': '12px 24px',
                                   'backgroundColor': '#e74c3c',
                                   'color': 'white',
                                   'border': 'none',
                                   'borderRadius': '5px',
                                   'cursor': 'pointer',
                                   'fontSize': '16px'
                               })
                ], style={'textAlign': 'center'})
            ])
        },
        "btn-video-parkinsons": {
            "title": "Parkinson's Exercise Guidelines",
            "content": html.Div([
                html.P("This 5:20 minute video demonstrates recommended exercises for Parkinson's disease patients to maintain mobility and quality of life.", 
                      style={'lineHeight': '1.6', 'marginBottom': '20px'}),
                
                html.Div([
                    html.Div([
                        html.Img(
                            src="/assets/video-placeholder-parkinsons.jpg",
                            style={'width': '100%', 'maxWidth': '500px', 'height': 'auto', 'borderRadius': '8px'}
                        ),
                        html.P("Video: Parkinson's Exercise Guidelines", 
                              style={'textAlign': 'center', 'color': '#666', 'marginTop': '10px'})
                    ], style={'textAlign': 'center', 'margin': '20px 0'})
                ]),
                
                html.P("Exercise types covered:", style={'fontWeight': 'bold', 'marginBottom': '10px'}),
                html.Ul([
                    html.Li("Balance and coordination exercises"),
                    html.Li("Strength training for core stability"),
                    html.Li("Flexibility and stretching routines"),
                    html.Li("Aerobic activities for cardiovascular health"),
                    html.Li("Voice and breathing exercises"),
                    html.Li("Functional movement practice")
                ], style={'lineHeight': '1.6', 'marginBottom': '20px'}),
                
                html.P("Always consult with your healthcare provider before starting any new exercise program.", 
                      style={'fontStyle': 'italic', 'color': '#666', 'marginBottom': '20px'}),
                
                html.Div([
                    html.Button("Play Video", 
                               style={
                                   'padding': '12px 24px',
                                   'backgroundColor': '#e74c3c',
                                   'color': 'white',
                                   'border': 'none',
                                   'borderRadius': '5px',
                                   'cursor': 'pointer',
                                   'fontSize': '16px'
                               })
                ], style={'textAlign': 'center'})
            ])
        }
    }
    
    if button_id in content_map:
        return {'display': 'block'}, content_map[button_id]["title"], content_map[button_id]["content"]
    
    return no_update, no_update, no_update