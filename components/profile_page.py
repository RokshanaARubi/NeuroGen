from dash import html, dcc

def create_profile_layout():
    return html.Div(className='dashboard-container', children=[
        # Same navigation as predict page
        html.Div(className='dashboard-nav', children=[
            html.H2("NeuroGen", className='brand'),
            html.Div(className='nav-links', children=[
                html.A("Predict", href='/predict', className='nav-link'),
                html.A("Profile", href='/profile', className='nav-link active'),
                html.Button('Logout', id='logout-button', className='btn ghost')
            ]),
            html.Div(id='welcome-user', className='welcome-text')
        ]),
        
        # Profile content
        html.Div(className='dashboard-content', children=[
            html.Div(className='profile-card', children=[
                html.H1("My Profile"),
                html.Div(id='profile-info', className='profile-info', children=[
                    html.P(id='profile-username', className='profile-field'),
                    html.P(id='profile-email', className='profile-field'),
                    html.P(id='profile-joined', className='profile-field')
                ])
            ]),
            
            html.Div(className='activity-card', children=[
                html.H2("Prediction Activity"),
                html.Div(id='prediction-stats', className='stats-grid'),
                html.Div(id='recent-predictions', className='recent-list')
            ])
        ])
    ])