from dash import html, dcc

def create_dashboard_layout():
    return html.Div([
        html.Div([
            # Welcome Section
            html.Div([
                html.H1("Welcome to NeuroGen", style={
                    'textAlign': 'center', 
                    'color': '#2c3e50', 
                    'marginBottom': '10px',
                    'fontSize': '2.5rem',
                    'fontWeight': '300'
                }),
                html.P("Your personal neurological health companion", style={
                    'textAlign': 'center', 
                    'color': '#7f8c8d', 
                    'fontSize': '1.2rem',
                    'marginBottom': '40px'
                })
            ]),
            
            # Quick Stats Cards
            html.Div([
                html.Div([
                    html.Div([
                        html.Div("📊", style={'fontSize': '2rem', 'marginBottom': '10px'}),
                        html.H3("Recent Assessments", style={'color': '#2c3e50', 'marginBottom': '10px', 'fontSize': '1.1rem'}),
                        html.H2("3", style={'margin': '10px 0', 'color': '#3498db', 'fontSize': '2.5rem', 'fontWeight': 'bold'}),
                        html.P("Last: Today", style={'color': '#7f8c8d', 'margin': '0'})
                    ], style={
                        'padding': '25px',
                        'textAlign': 'center',
                        'backgroundColor': 'white',
                        'borderRadius': '12px',
                        'boxShadow': '0 4px 12px rgba(0,0,0,0.1)',
                        'transition': 'transform 0.2s ease'
                    })
                ], style={'flex': '1', 'minWidth': '250px', 'margin': '10px'}),
                
                html.Div([
                    html.Div([
                        html.Div("📝", style={'fontSize': '2rem', 'marginBottom': '10px'}),
                        html.H3("Symptoms Tracked", style={'color': '#2c3e50', 'marginBottom': '10px', 'fontSize': '1.1rem'}),
                        html.H2("12", style={'margin': '10px 0', 'color': '#27ae60', 'fontSize': '2.5rem', 'fontWeight': 'bold'}),
                        html.P("This week", style={'color': '#7f8c8d', 'margin': '0'})
                    ], style={
                        'padding': '25px',
                        'textAlign': 'center',
                        'backgroundColor': 'white',
                        'borderRadius': '12px',
                        'boxShadow': '0 4px 12px rgba(0,0,0,0.1)',
                        'transition': 'transform 0.2s ease'
                    })
                ], style={'flex': '1', 'minWidth': '250px', 'margin': '10px'}),
                
                html.Div([
                    html.Div([
                        html.Div("⚠️", style={'fontSize': '2rem', 'marginBottom': '10px'}),
                        html.H3("Risk Level", style={'color': '#2c3e50', 'marginBottom': '10px', 'fontSize': '1.1rem'}),
                        html.H2("Moderate", style={'margin': '10px 0', 'color': '#f39c12', 'fontSize': '2.5rem', 'fontWeight': 'bold'}),
                        html.P("Alzheimer's", style={'color': '#7f8c8d', 'margin': '0'})
                    ], style={
                        'padding': '25px',
                        'textAlign': 'center',
                        'backgroundColor': 'white',
                        'borderRadius': '12px',
                        'boxShadow': '0 4px 12px rgba(0,0,0,0.1)',
                        'transition': 'transform 0.2s ease'
                    })
                ], style={'flex': '1', 'minWidth': '250px', 'margin': '10px'}),
                
                html.Div([
                    html.Div([
                        html.Div("🎯", style={'fontSize': '2rem', 'marginBottom': '10px'}),
                        html.H3("Next Check-up", style={'color': '#2c3e50', 'marginBottom': '10px', 'fontSize': '1.1rem'}),
                        html.H2("7", style={'margin': '10px 0', 'color': '#9b59b6', 'fontSize': '2.5rem', 'fontWeight': 'bold'}),
                        html.P("Days remaining", style={'color': '#7f8c8d', 'margin': '0'})
                    ], style={
                        'padding': '25px',
                        'textAlign': 'center',
                        'backgroundColor': 'white',
                        'borderRadius': '12px',
                        'boxShadow': '0 4px 12px rgba(0,0,0,0.1)',
                        'transition': 'transform 0.2s ease'
                    })
                ], style={'flex': '1', 'minWidth': '250px', 'margin': '10px'})
            ], style={
                'display': 'flex', 
                'flexWrap': 'wrap', 
                'justifyContent': 'center', 
                'margin': '30px 0',
                'gap': '15px'
            }),
            
            # Two Column Layout for Activity and Health Overview
            html.Div([
                # Recent Activity Section
                html.Div([
                    html.H3("Recent Activity", style={
                        'color': '#2c3e50', 
                        'marginBottom': '20px',
                        'borderBottom': '2px solid #3498db',
                        'paddingBottom': '10px'
                    }),
                    html.Div([
                        html.Div([
                            html.Div("✓", style={'color': '#27ae60', 'fontWeight': 'bold', 'marginRight': '10px'}),
                            html.Div([
                                html.Strong("Completed Cognitive Assessment"),
                                html.P("Alzheimer's screening - Today", style={'color': '#7f8c8d', 'margin': '0', 'fontSize': '0.9rem'})
                            ])
                        ], style={'display': 'flex', 'padding': '15px', 'borderBottom': '1px solid #ecf0f1'}),
                        
                        html.Div([
                            html.Div("✓", style={'color': '#27ae60', 'fontWeight': 'bold', 'marginRight': '10px'}),
                            html.Div([
                                html.Strong("Logged Symptom"),
                                html.P("Memory lapse - Yesterday", style={'color': '#7f8c8d', 'margin': '0', 'fontSize': '0.9rem'})
                            ])
                        ], style={'display': 'flex', 'padding': '15px', 'borderBottom': '1px solid #ecf0f1'}),
                        
                        html.Div([
                            html.Div("✓", style={'color': '#27ae60', 'fontWeight': 'bold', 'marginRight': '10px'}),
                            html.Div([
                                html.Strong("Updated Health Data"),
                                html.P("Sleep patterns - 2 days ago", style={'color': '#7f8c8d', 'margin': '0', 'fontSize': '0.9rem'})
                            ])
                        ], style={'display': 'flex', 'padding': '15px', 'borderBottom': '1px solid #ecf0f1'}),
                        
                        html.Div([
                            html.Div("📚", style={'marginRight': '10px'}),
                            html.Div([
                                html.Strong("Viewed Resources"),
                                html.P("Alzheimer's education - 3 days ago", style={'color': '#7f8c8d', 'margin': '0', 'fontSize': '0.9rem'})
                            ])
                        ], style={'display': 'flex', 'padding': '15px'})
                    ], style={
                        'backgroundColor': 'white',
                        'borderRadius': '12px',
                        'boxShadow': '0 2px 8px rgba(0,0,0,0.1)',
                        'overflow': 'hidden'
                    })
                ], style={'flex': '1', 'minWidth': '300px', 'margin': '10px'}),
                
                # Health Overview Section
                html.Div([
                    html.H3("Health Overview", style={
                        'color': '#2c3e50', 
                        'marginBottom': '20px',
                        'borderBottom': '2px solid #e74c3c',
                        'paddingBottom': '10px'
                    }),
                    html.Div([
                        # Sleep Quality
                        html.Div([
                            html.Div([
                                html.Strong("Sleep Quality", style={'color': '#2c3e50'}),
                                html.Div("Good", style={
                                    'color': '#27ae60', 
                                    'fontWeight': 'bold',
                                    'padding': '4px 12px',
                                    'backgroundColor': '#d5f4e6',
                                    'borderRadius': '20px',
                                    'fontSize': '0.9rem'
                                })
                            ], style={'display': 'flex', 'justifyContent': 'space-between', 'alignItems': 'center', 'marginBottom': '15px'}),
                            html.Div([
                                html.Span("7.5", style={'fontSize': '1.5rem', 'fontWeight': 'bold', 'color': '#2c3e50'}),
                                html.Span(" hours/night", style={'color': '#7f8c8d'})
                            ]),
                            # Custom progress bar for sleep
                            html.Div([
                                html.Div(style={
                                    'width': '75%',
                                    'height': '8px',
                                    'backgroundColor': '#27ae60',
                                    'borderRadius': '10px'
                                })
                            ], style={
                                'width': '100%',
                                'height': '8px',
                                'backgroundColor': '#ecf0f1',
                                'borderRadius': '10px',
                                'overflow': 'hidden'
                            })
                        ], style={
                            'padding': '20px',
                            'borderBottom': '1px solid #ecf0f1'
                        }),
                        
                        # Physical Activity
                        html.Div([
                            html.Div([
                                html.Strong("Physical Activity", style={'color': '#2c3e50'}),
                                html.Div("Active", style={
                                    'color': '#3498db', 
                                    'fontWeight': 'bold',
                                    'padding': '4px 12px',
                                    'backgroundColor': '#d6eaf8',
                                    'borderRadius': '20px',
                                    'fontSize': '0.9rem'
                                })
                            ], style={'display': 'flex', 'justifyContent': 'space-between', 'alignItems': 'center', 'marginBottom': '15px'}),
                            html.Div([
                                html.Span("85%", style={'fontSize': '1.5rem', 'fontWeight': 'bold', 'color': '#2c3e50'}),
                                html.Span(" of weekly goal", style={'color': '#7f8c8d'})
                            ]),
                            # Custom progress bar for activity
                            html.Div([
                                html.Div(style={
                                    'width': '85%',
                                    'height': '8px',
                                    'backgroundColor': '#3498db',
                                    'borderRadius': '10px'
                                })
                            ], style={
                                'width': '100%',
                                'height': '8px',
                                'backgroundColor': '#ecf0f1',
                                'borderRadius': '10px',
                                'overflow': 'hidden'
                            })
                        ], style={
                            'padding': '20px',
                            'borderBottom': '1px solid #ecf0f1'
                        }),
                        
                        # Mental Wellbeing
                        html.Div([
                            html.Div([
                                html.Strong("Mental Wellbeing", style={'color': '#2c3e50'}),
                                html.Div("Stable", style={
                                    'color': '#9b59b6', 
                                    'fontWeight': 'bold',
                                    'padding': '4px 12px',
                                    'backgroundColor': '#e8daef',
                                    'borderRadius': '20px',
                                    'fontSize': '0.9rem'
                                })
                            ], style={'display': 'flex', 'justifyContent': 'space-between', 'alignItems': 'center', 'marginBottom': '15px'}),
                            html.Div([
                                html.Span("8/10", style={'fontSize': '1.5rem', 'fontWeight': 'bold', 'color': '#2c3e50'}),
                                html.Span(" mood score", style={'color': '#7f8c8d'})
                            ]),
                            # Custom progress bar for mental wellbeing
                            html.Div([
                                html.Div(style={
                                    'width': '80%',
                                    'height': '8px',
                                    'backgroundColor': '#9b59b6',
                                    'borderRadius': '10px'
                                })
                            ], style={
                                'width': '100%',
                                'height': '8px',
                                'backgroundColor': '#ecf0f1',
                                'borderRadius': '10px',
                                'overflow': 'hidden'
                            })
                        ], style={
                            'padding': '20px'
                        })
                        
                    ], style={
                        'backgroundColor': 'white',
                        'borderRadius': '12px',
                        'boxShadow': '0 2px 8px rgba(0,0,0,0.1)',
                        'overflow': 'hidden'
                    })
                ], style={'flex': '1', 'minWidth': '300px', 'margin': '10px'})
            ], style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'center', 'gap': '30px', 'margin': '30px 0'}),
            
            # Health Tips Section
            html.Div([
                html.H3("Health Tips", style={
                    'color': '#2c3e50', 
                    'textAlign': 'center',
                    'marginBottom': '20px'
                }),
                html.Div([
                    html.Div([
                        html.H4("💤 Sleep Well", style={'color': '#3498db', 'marginBottom': '10px'}),
                        html.P("Aim for 7-9 hours of quality sleep each night to support brain health and cognitive function.", style={'color': '#7f8c8d', 'lineHeight': '1.5'})
                    ], style={
                        'padding': '20px',
                        'backgroundColor': 'white',
                        'borderRadius': '10px',
                        'boxShadow': '0 2px 6px rgba(0,0,0,0.1)',
                        'textAlign': 'center'
                    }),
                    
                    html.Div([
                        html.H4("🏃 Stay Active", style={'color': '#27ae60', 'marginBottom': '10px'}),
                        html.P("Regular physical activity improves blood flow to the brain and can reduce neurological risk factors.", style={'color': '#7f8c8d', 'lineHeight': '1.5'})
                    ], style={
                        'padding': '20px',
                        'backgroundColor': 'white',
                        'borderRadius': '10px',
                        'boxShadow': '0 2px 6px rgba(0,0,0,0.1)',
                        'textAlign': 'center'
                    }),
                    
                    html.Div([
                        html.H4("🧠 Mental Exercise", style={'color': '#9b59b6', 'marginBottom': '10px'}),
                        html.P("Challenge your brain with puzzles, reading, or learning new skills to maintain cognitive vitality.", style={'color': '#7f8c8d', 'lineHeight': '1.5'})
                    ], style={
                        'padding': '20px',
                        'backgroundColor': 'white',
                        'borderRadius': '10px',
                        'boxShadow': '0 2px 6px rgba(0,0,0,0.1)',
                        'textAlign': 'center'
                    })
                ], style={
                    'display': 'flex',
                    'flexWrap': 'wrap',
                    'justifyContent': 'center',
                    'gap': '20px'
                })
            ], style={'marginTop': '40px'})
            
        ], style={'maxWidth': '1200px', 'margin': '0 auto', 'padding': '20px'})
    ], style={'backgroundColor': '#f8f9fa', 'minHeight': '100vh'})