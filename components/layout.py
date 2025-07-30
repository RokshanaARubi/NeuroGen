from dash import html, dcc, dash_table

def create_layout():
    return html.Div([
        html.H1("🧠 NeuroGen - Neurological Disorder Predictor", style={
            "textAlign": "center",
            "marginBottom": "1rem",
            "color": "#2d3e50"
        }),
        html.Div([
            html.Label("Enter SNP IDs (comma-separated):", style={"marginRight": "10px"}),
            dcc.Input(
                id='snp-input',
                type='text',
                placeholder='e.g. rs123, rs456',
                style={'width': '60%', "marginRight": "10px"}
            ),
            html.Button("Predict", id='submit-button', n_clicks=0, style={
                "backgroundColor": "#0074D9",
                "color": "white",
                "border": "none",
                "padding": "8px 16px",
                "borderRadius": "4px"
            }),
            html.Div(id='input-error', style={"color": "red", "marginTop": "8px"}),
        ], style={"display": "flex", "flexWrap": "wrap", "alignItems": "center", "marginBottom": "20px"}),

        html.Div([
            html.Label("Or upload CSV for batch prediction:", style={"marginRight": "10px"}),
            dcc.Upload(
                id='upload-csv',
                children=html.Button('Upload CSV', style={
                    "backgroundColor": "#FF851B",
                    "color": "white",
                    "border": "none",
                    "padding": "8px 16px",
                    "borderRadius": "4px"
                }),
                multiple=False,
                style={"marginBottom": "20px"}
            ),
            html.Div(id='csv-upload-error', style={"color": "red", "marginTop": "8px"}),
        ], style={"display": "flex", "alignItems": "center", "marginBottom": "20px"}),

        dcc.Loading(
            id="loading-results",
            type="circle",
            children=html.Div(id='result-output', style={'marginTop': 20})
        ),

        html.Hr(),

        html.H2("Prediction History", style={"marginTop": "2rem"}),
        dcc.Loading(
            id="loading-history",
            type="dot",
            children=dash_table.DataTable(
                id='history-table',
                columns=[
                    {"name": "SNP Input", "id": "snp_input"},
                    {"name": "Result", "id": "result"},
                    {"name": "Timestamp", "id": "timestamp"},
                ],
                data=[],  # Will be populated by callback
                style_table={'overflowX': 'auto'},
                style_cell={'textAlign': 'left', "padding": "6px"},
                page_size=10,
                style_header={
                    "backgroundColor": "#f8f9fa",
                    "fontWeight": "bold"
                },
            )
        ),

    ], style={
        "maxWidth": "700px",
        "margin": "auto",
        "padding": "32px",
        "backgroundColor": "#f4f7fa",
        "borderRadius": "12px",
        "boxShadow": "0 4px 24px rgba(0,0,0,0.06)"
    })