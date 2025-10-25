import dash
from dash import html, dcc, dash_table

def create_layout():
    return html.Div(className='page-root', children=[

        dcc.Store(id='current-user', data=None),

        # Centered compact card (image-2 style)
        html.Div(className='center-card', children=[

            # Illustration / top banner
            html.Div(className='card-illustration', children=[
                html.Div(className='illus-inner', children=[
                    html.H1("NeuroGen"),
                    html.P("Predict neurological disorder risk from SNPs")
                ])
            ], style={'display':'none'}),

            # Body with Login / Register tabs and prediction area
            html.Div(className='card-body', children=[
                dcc.Tabs(id='auth-tabs', value='tab-login', children=[
                    dcc.Tab(label='Login', value='tab-login', children=[
                        html.Div(className='auth-form', children=[
                            dcc.Input(id='login-username', placeholder='Username', type='text', className='input'),
                            dcc.Input(id='login-password', placeholder='Password', type='password', className='input'),
                            html.Div(className='form-row', children=[
                                html.Button('Login', id='login-button', className='btn primary'),
                                html.Button('Logout', id='logout-button', className='btn ghost')
                            ]),
                            html.Div(html.A("Don't have an account? Create one", href='#', id='goto-register', className='link'))
                        ])
                    ]),
                    dcc.Tab(label='Register', value='tab-register', children=[
                        html.Div(className='auth-form', children=[
                            dcc.Input(id='reg-username', placeholder='Username', type='text', className='input'),
                            dcc.Input(id='reg-email', placeholder='Email (optional)', type='email', className='input'),
                            dcc.Input(id='reg-password', placeholder='Password', type='password', className='input'),
                            html.Div(className='form-row', children=[
                                html.Button('Register', id='register-button', className='btn primary'),
                                html.Button('Back to Login', id='back-to-login', className='btn ghost')
                            ]),
                        ])
                    ]),
                ]),

                html.Div(id='auth-output', className='auth-output'),

                html.Hr(),

                html.Div(id='predict-area', style={'display':'none'}, children=[
                    html.Div(id='welcome-user', className='welcome'),
                    dcc.Input(id='snp-input', type='text', placeholder='e.g. rs429358, rs7412', className='input full'),
                    html.Button('Submit', id='submit-button', className='btn primary'),
                    html.Div(id='result-output', className='result'),
                    html.H3("Prediction History"),
                    dash_table.DataTable(
                        id='history-table',
                        columns=[
                            {'name': 'User', 'id': 'username'},
                            {'name': 'SNP Input', 'id': 'snp_input'},
                            {'name': 'Result', 'id': 'result'},
                            {'name': 'Timestamp', 'id': 'timestamp'}
                        ],
                        data=[],
                        style_table={'overflowX': 'auto'},
                        style_cell={'textAlign': 'left', 'padding': '6px'}
                    )
                ])
            ])
        ])
    ])