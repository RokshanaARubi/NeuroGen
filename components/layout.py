from dash import html, dcc

def create_layout():
    return html.Div([
        html.H1("🧠 NeuroGen - Neurological Disorder Predictor"),
        html.Label("Enter SNP IDs (comma-separated):"),
        dcc.Input(id='snp-input', type='text', placeholder='e.g. rs123, rs456', style={'width': '60%'}),
        html.Button("Predict", id='submit-button'),
        html.Div(id='result-output', style={'marginTop': 20})
    ])
