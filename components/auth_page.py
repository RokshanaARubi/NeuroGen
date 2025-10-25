from dash import html, dcc

def create_auth_layout():
    return html.Div(className='auth-page', children=[
        html.Div(className='login-card', children=[
            html.Div(className='card-header', children=[
                html.H1("Hello!", className='greeting'),
                html.P("Login your account", className='subtitle')
            ]),
            
            dcc.Tabs(id='auth-tabs', value='tab-login', className='auth-tabs', children=[
                dcc.Tab(label='Login', value='tab-login', children=[
                    html.Div(className='auth-form', children=[
                        dcc.Input(id='login-username', placeholder='Username', type='text', className='input'),
                        dcc.Input(id='login-password', placeholder='Password', type='password', className='input'),
                        html.Div(className='form-row', children=[
                            html.Button('Login', id='login-button', className='btn primary full-width')
                        ]),
                        html.A("Don't have an account? Create one", href='#', id='goto-register', className='link')
                    ])
                ]),
                dcc.Tab(label='Register', value='tab-register', children=[
                    html.Div(className='auth-form', children=[
                        dcc.Input(id='reg-username', placeholder='Username', type='text', className='input'),
                        dcc.Input(id='reg-email', placeholder='Email', type='email', className='input'),
                        dcc.Input(id='reg-password', placeholder='Password', type='password', className='input'),
                        html.Button('Register', id='register-button', className='btn primary full-width')
                    ])
                ])
            ]),
            html.Div(id='auth-output', className='auth-output')
        ])
    ])