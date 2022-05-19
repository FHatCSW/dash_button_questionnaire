import dash_bootstrap_components as dbc
from dash import Input, Output, html, Dash, callback_context, dcc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

q1_frame = {
    "question": "This is question 1. What is the answer?",
    "answers": {
        "q1_answer_1": "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. ",
        "q1_answer_2": "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. ",
        "q1_answer_3": "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. ",
    },
    "result": "q1_answer_1"
}

app.layout = html.Div(dbc.Container([
    dbc.Row([
        dbc.Col(
            dbc.Button(
                "1.", id="q1_answer_1", n_clicks=0, class_name="questionnaire_button"
            ),
            width=2
        ),
        dbc.Col(
            html.P(q1_frame['answers']['q1_answer_1'], className="questionnaire_text")
        )
    ]),
    dbc.Row([
        dbc.Col(
            dbc.Button(
                "2.", id="q1_answer_2", n_clicks=0, class_name="questionnaire_button"
            ),
            width=2
        ),
        dbc.Col(
            html.P(q1_frame['answers']['q1_answer_2'], className="questionnaire_text")
        )
    ]),
    dbc.Row([
        dbc.Col(
            dbc.Button(
                "3.", id="q1_answer_3", n_clicks=0, class_name="questionnaire_button"
            ),
            width=2
        ),
        dbc.Col(
            html.P(q1_frame['answers']['q1_answer_3'], className="questionnaire_text")
        )
    ]),
    html.Div(id="result_question_1")
])
)


@app.callback(Output("result_question_1", "children"),
              [Input("q1_answer_1", "n_clicks"),
               Input("q1_answer_2", "n_clicks"),
               Input("q1_answer_3", "n_clicks")])
def output_text(button_1, button_2, button_3):
    ctx = callback_context
    changed_id = ctx.triggered[0]['prop_id'].split('.')[0]
    res = ""
    if button_1 or button_2 or button_3:
        if q1_frame['result'] in changed_id:
            res = "True answer"
        else:
            res = "Wrong answer"

    return res


if __name__ == "__main__":
    app.run_server()
