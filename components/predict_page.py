from dash import html, dcc, dash_table

def create_predict_layout():
    return html.Div(className='dashboard-container', children=[
        # REMOVED the duplicate navigation header - it's already handled in app.py
        
        # Main content
        html.Div(className='main-content', children=[
            html.H1("SNP Prediction", style={'textAlign': 'center', 'marginBottom': '30px'}),
            
            html.Div([
                html.Label("Enter SNP Variant:", style={'fontWeight': 'bold', 'marginBottom': '10px', 'display': 'block'}),
                dcc.Input(
                    id='snp-input', 
                    type='text', 
                    placeholder='Enter SNP (e.g. rs429358, rs6265)',
                    style={
                        'width': '100%',
                        'maxWidth': '400px',
                        'padding': '12px',
                        'border': '2px solid #ddd',
                        'borderRadius': '8px',
                        'fontSize': '16px',
                        'marginBottom': '20px'
                    }
                ),
                html.Button(
                    'Submit', 
                    id='submit-button', 
                    className='btn primary',
                    style={
                        'padding': '12px 30px',
                        'fontSize': '16px',
                        'backgroundColor': '#3498db',
                        'color': 'white',
                        'border': 'none',
                        'borderRadius': '8px',
                        'cursor': 'pointer'
                    }
                ),
            ], style={'textAlign': 'center', 'marginBottom': '40px'}),
            
            html.Div(id='result-output', style={'marginBottom': '40px'}),
            
            # History table
            html.H2("Prediction History", style={'textAlign': 'center', 'marginBottom': '20px', 'color': '#2c3e50'}),
            html.Div([
                dash_table.DataTable(
                    id='history-table',
                    columns=[
                        {'name': 'SNP Input', 'id': 'snp_input'},
                        {'name': 'Result', 'id': 'result'},
                        {'name': 'Timestamp', 'id': 'timestamp'}
                    ],
                    data=[],
                    style_cell={
                        'textAlign': 'left',
                        'padding': '12px',
                        'border': '1px solid #ddd'
                    },
                    style_header={
                        'backgroundColor': '#2c3e50',
                        'color': 'white',
                        'fontWeight': 'bold'
                    },
                    style_data={
                        'backgroundColor': '#f8f9fa'
                    },
                    page_size=10
                )
            ], style={'marginBottom': '40px'})
        ], style={'maxWidth': '1000px', 'margin': '0 auto', 'padding': '20px'})
    ])