from dash import html, dcc, dash_table

def create_predict_layout():
    return html.Div(className='dashboard-container', children=[
        # Navigation header with logout button
        html.Div(className='nav-bar', children=[
            html.H2("NeuroGen Dashboard"),
            html.Div(className='nav-right', children=[
                html.Button('Logout', id='logout-button', className='btn logout')
            ])
        ]),
        
        # Main content
        html.Div(className='main-content', children=[
            html.H1("SNP Prediction"),
            dcc.Input(id='snp-input', type='text', placeholder='Enter SNP (e.g. rs429358)'),
            html.Button('Submit', id='submit-button', className='btn primary'),
            html.Div(id='result-output'),
            
            # History table
            html.H2("Prediction History"),
            dash_table.DataTable(
                id='history-table',
                columns=[
                    {'name': 'SNP Input', 'id': 'snp_input'},
                    {'name': 'Result', 'id': 'result'},
                    {'name': 'Timestamp', 'id': 'timestamp'}
                ],
                data=[]
            )
        ])
    ])