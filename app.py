import dash
from dash import dcc, html, Input, Output, State
from components.layout import create_layout
from db.db_utils import insert_input, fetch_input_history  # Updated import
from logic.predict import run_prediction
import webbrowser
from threading import Timer

app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "NeuroGen"

# Set the layout from components
app.layout = create_layout()

# Callback to handle user input and prediction
@app.callback(
    Output('result-output', 'children'),
    Input('submit-button', 'n_clicks'),
    State('snp-input', 'value'),
    prevent_initial_call=True
)
def handle_prediction(n_clicks, snp_input):
    if snp_input:
        # 1. Run prediction
        result = run_prediction(snp_input)

        # 2. Insert input and result to DB
        insert_input(snp_input, result)

        # 3. Show result on the page
        return f"Prediction Result: {result}"
    return "Please enter SNPs to predict."


# --- NEW: Callback to update history table ---
@app.callback(
    Output('history-table', 'data'),
    Input('submit-button', 'n_clicks'),  # Refresh on new prediction
    prevent_initial_call=True
)
def update_history(n_clicks):
    rows = fetch_input_history(limit=10)  # List of (snp_input, result, timestamp)
    # Format for DataTable
    return [
        {
            "snp_input": row[0],
            "result": row[1],
            "timestamp": row[2].strftime("%Y-%m-%d %H:%M") if row[2] else ""
        }
        for row in rows
    ]


if __name__ == '__main__':
    Timer(1, lambda: webbrowser.open("http://127.0.0.1:8050")).start()
    app.run(debug=True)