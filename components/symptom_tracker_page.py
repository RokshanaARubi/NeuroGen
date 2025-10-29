from dash import html, dcc, Input, Output

def create_symptom_tracker_layout():
    return html.Div([
        html.H1("Symptom Tracker", style={'textAlign': 'center'}),
        
        html.Div([
            # Symptom Log Form
            html.Div([
                html.H3("Log New Symptom"),
                html.Label("Symptom Type"),
                dcc.Dropdown(
                    id='symptom-type',
                    options=[
                        {'label': 'Memory Lapse', 'value': 'memory_lapse'},
                        {'label': 'Tremor', 'value': 'tremor'},
                        {'label': 'Headache', 'value': 'headache'},
                        {'label': 'Vision Problems', 'value': 'vision'},
                        {'label': 'Speech Difficulty', 'value': 'speech'},
                        {'label': 'Balance Issues', 'value': 'balance'},
                    ],
                    placeholder="Select symptom type"
                ),
                
                html.Label("Severity (1-10)", style={'marginTop': '10px'}),
                dcc.Slider(
                    id='symptom-severity',
                    min=1,
                    max=10,
                    value=5,
                    marks={i: str(i) for i in range(1, 11)}
                ),
                
                html.Label("Notes", style={'marginTop': '10px'}),
                dcc.Textarea(
                    id='symptom-notes',
                    placeholder="Describe your symptoms...",
                    style={'width': '100%', 'height': '100px'}
                ),
                
                html.Button("Log Symptom", id='log-symptom', n_clicks=0,
                          style={'marginTop': '10px', 'padding': '10px 20px'}),
                
                html.Div(id='symptom-output')
                
            ], style={'padding': '20px', 'backgroundColor': '#f8f9fa', 'borderRadius': '5px', 'marginBottom': '20px'}),
            
            # Symptom History Chart
            html.Div([
                html.H3("Symptom History"),
                dcc.Graph(
                    figure={
                        'data': [
                            {'x': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], 
                             'y': [3, 5, 2, 6, 4, 3, 2], 
                             'type': 'line', 
                             'name': 'Memory Lapses'},
                            {'x': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], 
                             'y': [1, 2, 1, 3, 2, 1, 1], 
                             'type': 'line', 
                             'name': 'Tremors'},
                        ],
                        'layout': {
                            'title': 'Weekly Symptom Trends'
                        }
                    }
                )
            ])
            
        ], style={'maxWidth': '1000px', 'margin': '0 auto', 'padding': '20px'})
    ])