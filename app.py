import dash
from dash import dcc, html, Input, Output, State
from components.layout import create_layout
from db.db_utils import insert_input, fetch_results
from logic.predict import run_prediction

app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "NeuroGen"

app.layout = create_layout()

@app.callback(
    Output('result-output', 'children'),
    Input('submit-button', 'n_clicks'),
    State('snp-input', 'value'),
    prevent_initial_call=True
)
def handle_prediction(n_clicks, snp_input):
    if snp_input:
        result = run_prediction(snp_input)
        insert_input(snp_input, result)
        return result
    return "Please enter SNPs to predict."

if __name__ == '__main__':
    app.run(debug=True)
