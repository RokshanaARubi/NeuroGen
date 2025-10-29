from dash import html, dcc

def create_feedback_layout():
    return html.Div([
        html.H1("Community & Feedback", style={'textAlign': 'center'}),
        
        html.Div([
            # User Testimonials
            html.Div([
                html.H3("User Experiences"),
                html.Div([
                    html.Div([
                        html.P('"NeuroGen helped me understand my genetic risks and take proactive steps for brain health."'),
                        html.P("- Sarah M., 58", style={'fontStyle': 'italic', 'textAlign': 'right'})
                    ], style={'padding': '20px', 'borderLeft': '4px solid #007BFF', 'backgroundColor': '#f8f9fa', 'margin': '10px'}),
                    
                    html.Div([
                        html.P('"The symptom tracker made it easy to discuss patterns with my neurologist."'),
                        html.P("- James R., 62", style={'fontStyle': 'italic', 'textAlign': 'right'})
                    ], style={'padding': '20px', 'borderLeft': '4px solid #28a745', 'backgroundColor': '#f8f9fa', 'margin': '10px'}),
                ])
            ], style={'marginBottom': '30px'}),
            
            # Research Participation
            html.Div([
                html.H3("Contribute to Research"),
                html.P("Help advance neurological science by anonymously sharing your data:"),
                
                html.Div([
                    html.Label(
                        children=[
                            dcc.Checklist(
                                options=[{'label': ' I agree to contribute anonymous data for research purposes', 'value': 'agree'}],
                                value=[],
                                id='research-consent'
                            )
                        ]
                    )
                ], style={'margin': '15px 0'}),
                
                html.Button("Save Preferences", style={'padding': '10px 20px'})
                
            ], style={'padding': '20px', 'border': '1px solid #ddd', 'borderRadius': '5px', 'marginBottom': '30px'}),
            
            # Support Forums Preview
            html.Div([
                html.H3("Community Support"),
                html.P("Connect with others on similar health journeys:"),
                
                html.Div([
                    html.Div([
                        html.H5("Caregiver Support"),
                        html.P("Share experiences and get support"),
                        html.Small("245 active members")
                    ], style={'padding': '15px', 'border': '1px solid #ddd', 'margin': '10px', 'borderRadius': '5px', 'textAlign': 'center', 'flex': '1'}),
                    
                    html.Div([
                        html.H5("Early Detection Discussion"),
                        html.P("Discuss screening and monitoring"),
                        html.Small("189 active members")
                    ], style={'padding': '15px', 'border': '1px solid #ddd', 'margin': '10px', 'borderRadius': '5px', 'textAlign': 'center', 'flex': '1'}),
                    
                    html.Div([
                        html.H5("Lifestyle Strategies"),
                        html.P("Share tips and success stories"),
                        html.Small("312 active members")
                    ], style={'padding': '15px', 'border': '1px solid #ddd', 'margin': '10px', 'borderRadius': '5px', 'textAlign': 'center', 'flex': '1'})
                ], style={'display': 'flex', 'flexWrap': 'wrap'}),
                
                html.Button("Join Community Forum", 
                          style={'marginTop': '20px', 'padding': '10px 20px', 'backgroundColor': '#007BFF', 'color': 'white'})
                
            ], style={'textAlign': 'center'}),
            
            # Feedback Form
            html.Div([
                html.H3("Share Your Feedback", style={'marginTop': '30px'}),
                html.Label("How can we improve NeuroGen?"),
                dcc.Textarea(
                    placeholder="Your suggestions...",
                    style={'width': '100%', 'height': '100px', 'marginBottom': '10px'}
                ),
                html.Button("Submit Feedback", style={'padding': '10px 20px'})
            ])
            
        ], style={'maxWidth': '1000px', 'margin': '0 auto', 'padding': '20px'})
    ])