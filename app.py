import dash
from dash import dcc, html, Input, Output, State
from components.auth_page import create_auth_layout
from components.predict_page import create_predict_layout
from components.profile_page import create_profile_layout
from db.db_utils import insert_input, fetch_input_history, register_user, authenticate_user
from logic.predict import run_prediction
import webbrowser
from threading import Timer

app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "NeuroGen"

# Main layout with URL routing
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Store(id='current-user', data=None),
    html.Div(id='page-content')
])

# Page router callback
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname'),
     Input('current-user', 'data')]
)
def display_page(pathname, user):
    if not user:  # Not logged in
        return create_auth_layout()
    
    if pathname == '/profile':
        return create_profile_layout()
    
    # Default to prediction page
    return create_predict_layout()

# Combined authentication callback for login/logout
@app.callback(
    [Output('current-user', 'data'),
     Output('auth-output', 'children'),
     Output('url', 'pathname')],
    Input('login-button', 'n_clicks'),
    [State('login-username', 'value'),
     State('login-password', 'value')],
    prevent_initial_call=True
)
def handle_login(n_clicks, username, password):
    if not n_clicks:
        return None, "", "/"
    
    if not username or not password:
        return None, "Please enter username and password", "/"
    if authenticate_user(username, password):
        return username, f"Welcome {username}!", "/predict"
    return None, "Invalid credentials", "/"

# Add separate logout callback that only triggers when logout button exists
@app.callback(
    [Output('current-user', 'data', allow_duplicate=True),
     Output('url', 'pathname', allow_duplicate=True)],
    Input('logout-button', 'n_clicks'),
    prevent_initial_call=True
)
def handle_logout(n_clicks):
    return None, "/"

# Register callback
@app.callback(
    [Output('auth-output', 'children', allow_duplicate=True),
     Output('auth-tabs', 'value')],
    Input('register-button', 'n_clicks'),
    [State('reg-username', 'value'),
     State('reg-password', 'value'),
     State('reg-email', 'value')],
    prevent_initial_call=True
)
def handle_register(n_clicks, username, password, email):
    if not n_clicks:
        return "", 'tab-register'
    if not username or not password:
        return "Username and password required", 'tab-register'
    if register_user(username, password, email):
        return "Registration successful! Please login.", 'tab-login'
    return "Username already exists", 'tab-register'

# Prediction callback
@app.callback(
    [Output('result-output', 'children'),
     Output('history-table', 'data')],
    Input('submit-button', 'n_clicks'),
    [State('snp-input', 'value'),
     State('current-user', 'data')],
    prevent_initial_call=True
)
def handle_prediction(n_clicks, snp_input, username):
    if not snp_input:
        return "Please enter SNPs to predict.", []
    
    result = run_prediction(snp_input)
    insert_input(snp_input, result, username)
    
    history = fetch_input_history()
    history_data = [
        {
            "username": row[0] if row[0] else "",
            "snp_input": row[1],
            "result": row[2],
            "timestamp": row[3].strftime("%Y-%m-%d %H:%M") if row[3] else ""
        }
        for row in history
    ]
    
    return f"Prediction Result: {result}", history_data

if __name__ == '__main__':
    Timer(1, lambda: webbrowser.open("http://127.0.0.1:8050")).start()
    app.run(debug=True, port=8050)