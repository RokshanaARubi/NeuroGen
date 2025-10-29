from dash import html, dcc

def create_recommendations_layout():
    return html.Div([
        html.H1("Recommendations & Next Steps", style={'textAlign': 'center'}),
        
        html.Div([
            # Lifestyle Recommendations
            html.Div([
                html.H3("Personalized Lifestyle Suggestions"),
                
                html.Div([
                    html.Div([
                        html.H4("💤 Sleep Optimization", style={'color': '#6f42c1'}),
                        html.P("• Aim for 7-8 hours of quality sleep nightly"),
                        html.P("• Maintain consistent sleep schedule"),
                        html.P("• Create dark, quiet sleeping environment")
                    ], style={'padding': '15px', 'backgroundColor': '#f8f9fa', 'margin': '10px', 'borderRadius': '5px', 'flex': '1'}),
                    
                    html.Div([
                        html.H4("🏃 Physical Activity", style={'color': '#20c997'}),
                        html.P("• 150 minutes moderate exercise weekly"),
                        html.P("• Include balance and coordination training"),
                        html.P("• Consider: walking, swimming, yoga")
                    ], style={'padding': '15px', 'backgroundColor': '#f8f9fa', 'margin': '10px', 'borderRadius': '5px', 'flex': '1'}),
                    
                    html.Div([
                        html.H4("🧠 Cognitive Training", style={'color': '#fd7e14'}),
                        html.P("• Daily puzzles or brain games"),
                        html.P("• Learn new skills or languages"),
                        html.P("• Social engagement activities")
                    ], style={'padding': '15px', 'backgroundColor': '#f8f9fa', 'margin': '10px', 'borderRadius': '5px', 'flex': '1'})
                ], style={'display': 'flex', 'flexWrap': 'wrap'}),
                
                html.Div([
                    html.Div([
                        html.H4("🍎 Nutrition", style={'color': '#dc3545'}),
                        html.P("• Mediterranean diet recommended"),
                        html.P("• Omega-3 fatty acids from fish"),
                        html.P("• Antioxidant-rich fruits and vegetables")
                    ], style={'padding': '15px', 'backgroundColor': '#f8f9fa', 'margin': '10px', 'borderRadius': '5px', 'flex': '1'}),
                    
                    html.Div([
                        html.H4("😊 Stress Management", style={'color': '#6f42c1'}),
                        html.P("• Daily meditation or mindfulness"),
                        html.P("• Regular social connections"),
                        html.P("• Hobbies and leisure activities")
                    ], style={'padding': '15px', 'backgroundColor': '#f8f9fa', 'margin': '10px', 'borderRadius': '5px', 'flex': '1'})
                ], style={'display': 'flex', 'flexWrap': 'wrap'})
            ]),
            
            # Healthcare Professional Referral
            html.Div([
                html.H3("Specialist Referral Suggestions", style={'marginTop': '30px'}),
                html.Div([
                    html.Ul([
                        html.Li("Neurologist: For comprehensive neurological assessment"),
                        html.Li("Neuropsychologist: For detailed cognitive testing"),
                        html.Li("Geriatrician: For age-related health management (if applicable)"),
                        html.Li("Genetic Counselor: For understanding genetic risk factors")
                    ])
                ]),
                html.Button("Find Local Specialists", style={'marginTop': '15px', 'padding': '10px 20px'})
            ], style={'padding': '20px', 'border': '2px solid #007BFF', 'borderRadius': '5px'}),
            
            # Monitoring Schedule
            html.Div([
                html.H3("Recommended Monitoring Schedule", style={'marginTop': '30px'}),
                html.Table([
                    html.Thead(html.Tr([html.Th("Assessment"), html.Th("Frequency"), html.Th("Next Due")])),
                    html.Tbody([
                        html.Tr([html.Td("Cognitive Screening"), html.Td("6 months"), html.Td("April 2024")]),
                        html.Tr([html.Td("Symptom Review"), html.Td("Monthly"), html.Td("March 15, 2024")]),
                        html.Tr([html.Td("Lifestyle Assessment"), html.Td("3 months"), html.Td("May 2024")]),
                        html.Tr([html.Td("Medical Check-up"), html.Td("Annual"), html.Td("December 2024")])
                    ])
                ], style={'width': '100%', 'borderCollapse': 'collapse'}),
                
                html.Div(id='reminder-setup', style={'marginTop': '20px'}),
                html.Button("Set Reminders", style={'marginTop': '10px', 'padding': '10px 20px'})
            ])
            
        ], style={'maxWidth': '1200px', 'margin': '0 auto', 'padding': '20px'})
    ])