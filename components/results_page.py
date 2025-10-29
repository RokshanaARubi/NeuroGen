from dash import html, dcc

def create_results_layout():
    return html.Div([
        html.Div([
            html.H1("Results & Reports", style={'textAlign': 'center', 'marginBottom': '30px'}),
            
            # Risk Profile Summary
            html.Div([
                html.H3("Your Risk Profile", style={'marginBottom': '20px'}),
                html.Div([
                    html.Div([
                        html.H4("Alzheimer's Disease", style={'color': '#ff6b6b', 'marginBottom': '10px'}),
                        html.P("Risk Level: MODERATE", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                        html.P("Key Factors: APOE2 variant (protective)", style={'color': '#666', 'marginBottom': '10px'}),
                        html.Div([
                            html.Div(style={
                                'width': '60%', 
                                'height': '20px', 
                                'backgroundColor': '#ff6b6b',
                                'borderRadius': '10px'
                            })
                        ], style={'width': '100%', 'backgroundColor': '#e0e0e0', 'borderRadius': '10px'})
                    ], style={
                        'padding': '20px', 
                        'border': '1px solid #ddd', 
                        'margin': '10px', 
                        'borderRadius': '8px',
                        'flex': '1',
                        'minWidth': '300px'
                    }),
                    
                    html.Div([
                        html.H4("Parkinson's Disease", style={'color': '#4ecdc4', 'marginBottom': '10px'}),
                        html.P("Risk Level: LOW", style={'fontWeight': 'bold', 'marginBottom': '5px'}),
                        html.P("Key Factors: No significant variants detected", style={'color': '#666', 'marginBottom': '10px'}),
                        html.Div([
                            html.Div(style={
                                'width': '30%', 
                                'height': '20px', 
                                'backgroundColor': '#4ecdc4',
                                'borderRadius': '10px'
                            })
                        ], style={'width': '100%', 'backgroundColor': '#e0e0e0', 'borderRadius': '10px'})
                    ], style={
                        'padding': '20px', 
                        'border': '1px solid #ddd', 
                        'margin': '10px', 
                        'borderRadius': '8px',
                        'flex': '1',
                        'minWidth': '300px'
                    }),
                ], style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'center'})
            ], style={'marginBottom': '40px'}),
            
            # Download Reports Section
            html.Div([
                html.H3("Download Reports", style={'marginBottom': '20px', 'textAlign': 'center'}),
                html.Div([
                    html.Button("Generate PDF Report", className='btn btn-primary', style={'margin': '10px', 'padding': '12px 24px'}),
                    html.Button("Share with Healthcare Provider", className='btn btn-secondary', style={'margin': '10px', 'padding': '12px 24px'}),
                    html.Button("Export Raw Data", className='btn btn-secondary', style={'margin': '10px', 'padding': '12px 24px'}),
                ], style={'textAlign': 'center', 'marginBottom': '30px'})
            ], style={
                'padding': '20px', 
                'backgroundColor': '#f8f9fa', 
                'borderRadius': '8px',
                'marginBottom': '40px'
            }),
            
            # Timeline Visualization
            html.Div([
                html.H3("Assessment Timeline", style={'marginBottom': '20px'}),
                dcc.Graph(
                    id='results-timeline',
                    figure={
                        'data': [
                            {
                                'x': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'], 
                                'y': [45, 52, 48, 60, 55, 58], 
                                'type': 'scatter', 
                                'name': 'Cognitive Score',
                                'line': {'color': '#6a46f0', 'width': 3},
                                'marker': {'size': 8}
                            }
                        ],
                        'layout': {
                            'title': {'text': 'Cognitive Assessment Scores Over Time', 'font': {'size': 16}},
                            'yaxis': {'title': 'Score', 'range': [0, 100]},
                            'xaxis': {'title': 'Month'},
                            'plot_bgcolor': 'rgba(0,0,0,0)',
                            'paper_bgcolor': 'rgba(0,0,0,0)',
                            'font': {'color': '#333'},
                            'hovermode': 'closest'
                        }
                    },
                    style={'height': '400px'}
                )
            ], style={'marginBottom': '40px'}),
            
            # Recent Predictions Table
            html.Div([
                html.H3("Recent Predictions", style={'marginBottom': '20px'}),
                html.Div(id="results-history-container", children=[
                    dcc.Loading(
                        id="loading-results",
                        type="circle",
                        children=html.Div(id="results-history-table")
                    )
                ])
            ])
            
        ], style={'maxWidth': '1200px', 'margin': '0 auto', 'padding': '20px'})
    ])