import dash
from dash import dcc, html, Input, Output, State
from components.auth_page import create_auth_layout
from components.predict_page import create_predict_layout
from components.profile_page import create_profile_layout
from db.db_utils import insert_input, fetch_input_history, register_user, authenticate_user
from logic.predict import run_prediction
import json
import webbrowser
from threading import Timer

app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "NeuroGen"

# ------------------- MAIN LAYOUT -------------------
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Store(id='current-user', data=None),
    html.Div(id='page-content')
])

# ------------------- PAGE ROUTER -------------------
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname'),
     Input('current-user', 'data')]
)
def display_page(pathname, user):
    if not user:
        return create_auth_layout()
    if pathname == '/profile':
        return create_profile_layout()
    return create_predict_layout()

# ------------------- LOGIN -------------------
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
    if not username or not password:
        return None, "Please enter username and password", "/"
    if authenticate_user(username, password):
        return username, f"Welcome {username}!", "/predict"
    return None, "Invalid credentials", "/"

# ------------------- LOGOUT -------------------
@app.callback(
    [Output('current-user', 'data', allow_duplicate=True),
     Output('url', 'pathname', allow_duplicate=True)],
    Input('logout-button', 'n_clicks'),
    prevent_initial_call=True
)
def handle_logout(n_clicks):
    return None, "/"

# ------------------- REGISTER -------------------
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
    if not username or not password:
        return "Username and password required", 'tab-register'
    if register_user(username, password, email):
        return "Registration successful! Please login.", 'tab-login'
    return "Username already exists", 'tab-register'

# ------------------- PREDICTION -------------------
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

    try:
        # Run prediction
        result = run_prediction(snp_input)

        # Insert record into DB
        insert_input(snp_input, json.dumps(result), username)

        # Fetch history
        history = fetch_input_history()
        history_data = []
        for row in history:
            username_val = row[0] if row[0] else ""
            snp_val = row[1]
            result_val = row[2]

            # Try to parse JSON for table display
            try:
                parsed = json.loads(result_val)
            except Exception:
                parsed = result_val

            # Format result for table as plain text
            if isinstance(parsed, dict):
                table_text = "\n".join(
                    f"{disease}: {info['risk_level']}\n" +
                    "\n".join(f"- {detail}" for detail in info.get('details', []))
                    for disease, info in parsed.items()
                )
            else:
                table_text = str(parsed)

            history_data.append({
                "username": username_val,
                "snp_input": snp_val,
                "result": table_text,
                "timestamp": row[3].strftime("%Y-%m-%d %H:%M") if row[3] else ""
            })

        # Pretty display for most recent prediction
        result_lines = []
        for disease, info in result.items():
            result_lines.append(html.H4(disease))
            result_lines.append(
                html.Div(f"Risk Level: {info['risk_level']}", style={'fontWeight': 'bold'})
            )
            details_list = html.Ul([html.Li(detail) for detail in info.get('details', [])])
            result_lines.append(details_list)
            result_lines.append(html.Hr())

        pretty_display = html.Div(result_lines)

        return pretty_display, history_data

    except Exception as e:
        return f"Error during prediction: {e}", []

# ------------------- APP LAUNCH -------------------
if __name__ == '__main__':
    Timer(1, lambda: webbrowser.open("http://127.0.0.1:8050")).start()
    app.run(debug=True, port=8050)
