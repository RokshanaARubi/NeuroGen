from dash import html, dcc

def create_auth_layout():
    return html.Div(className='auth-page', children=[
        html.Div(className='auth-bg', children=[
            # animated bubbles (pure CSS)
            html.Div(className='bubbles', children=[
                html.Span(className='bubble'),
                html.Span(className='bubble'),
                html.Span(className='bubble'),
                html.Span(className='bubble'),
                html.Span(className='bubble'),
                html.Span(className='bubble'),
                html.Span(className='bubble'),
                html.Span(className='bubble'),
                html.Span(className='bubble'),
                html.Span(className='bubble'),
                html.Span(className='bubble'),
                html.Span(className='bubble')
            ]),

            # FIXED: Using correct class name 'auth-sentence' instead of 'modern-auth-sentence'
            html.Div(className='auth-sentence', children=[
                "Protect Your Cognitive Health",
                html.Br(),
                "Check your neurological risk in minutes with AI-powered assessment",
                html.Br(),
                "🔒 Secure & Private  🧠 Science-Backed  ⚡ Instant Results"
            ]),

            # Modern transparent login/register card
            html.Div(className='auth-glass-card', children=[
                # App Logo and Welcome
                html.Div(className='card-header', children=[
                    html.Div("🧠", className='app-logo'),
                    html.H1("Welcome to NeuroGen", className='greeting'),
                    html.P("Your neurological health companion", className='subtitle')
                ]),
                
                # Modern tab navigation
                dcc.Tabs(id='auth-tabs', value='tab-login', className='modern-tabs', children=[
                    dcc.Tab(label='Sign In', value='tab-login', className='modern-tab', selected_className='modern-tab-selected', children=[
                        html.Div(className='auth-form', children=[
                            html.Div(className='input-group', children=[
                                html.Div("👤", className='input-icon'),
                                dcc.Input(
                                    id='login-username', 
                                    placeholder='Username', 
                                    type='text', 
                                    className='modern-input'
                                )
                            ]),
                            html.Div(className='input-group', children=[
                                html.Div("🔒", className='input-icon'),
                                dcc.Input(
                                    id='login-password', 
                                    placeholder='Password', 
                                    type='password', 
                                    className='modern-input'
                                )
                            ]),
                            html.Button('Sign In', id='login-button', className='modern-btn primary'),
                            html.Div(className='auth-divider', children=[
                                html.Span(className='divider-line'),
                                html.Span("or", className='divider-text'),
                                html.Span(className='divider-line')
                            ]),
                            html.Div(className='switch-auth', children=[
                                html.Span("Don't have an account? ", className='switch-text'),
                                html.A("Create one", href='#', id='goto-register', className='switch-link')
                            ])
                        ])
                    ]),
                    dcc.Tab(label='Sign Up', value='tab-register', className='modern-tab', selected_className='modern-tab-selected', children=[
                        html.Div(className='auth-form', children=[
                            html.Div(className='input-group', children=[
                                html.Div("👤", className='input-icon'),
                                dcc.Input(
                                    id='reg-username', 
                                    placeholder='Username', 
                                    type='text', 
                                    className='modern-input'
                                )
                            ]),
                            html.Div(className='input-group', children=[
                                html.Div("📧", className='input-icon'),
                                dcc.Input(
                                    id='reg-email', 
                                    placeholder='Email', 
                                    type='email', 
                                    className='modern-input'
                                )
                            ]),
                            html.Div(className='input-group', children=[
                                html.Div("🔒", className='input-icon'),
                                dcc.Input(
                                    id='reg-password', 
                                    placeholder='Password', 
                                    type='password', 
                                    className='modern-input'
                                )
                            ]),
                            html.Button('Create Account', id='register-button', className='modern-btn primary'),
                            html.Div(className='auth-divider', children=[
                                html.Span(className='divider-line'),
                                html.Span("or", className='divider-text'),
                                html.Span(className='divider-line')
                            ]),
                            html.Div(className='switch-auth', children=[
                                html.Span("Already have an account? ", className='switch-text'),
                                html.A("Sign in", href='#', id='goto-login', className='switch-link')
                            ])
                        ])
                    ])
                ]),
                html.Div(id='auth-output', className='modern-auth-output')
            ])
        ])
    ])