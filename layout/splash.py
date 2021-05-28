import dash_html_components as html
import dash_bootstrap_components as dbc

jumbotron = dbc.Jumbotron(
    children=[
        html.H1("BeerPBL", className="display-3", style={"text-align": "center"}),
        html.P(
            "Beer Preference Based Learning",
            className="lead",
            style={"text-align": "center"}
        ),
        html.Hr(className="my-2"),
        html.P(
            "Get personalised beer recommendations using preference based learning and paired taste tests.",
            style={"text-align": "center"}
        ),
    ],
    fluid=True,
    className="splash-jumbotron"
)

first_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Step 1:", className="card-title"),
            html.P("Select the Beer52 beers available for tasting.")
        ]
    ), color="#fff", outline=True
)

second_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Step 2:", className="card-title"),
            html.P(
                "Have a taste of the beers presented and select your preferred beer."
            )
        ]
    ), color="#fff", outline=True
)

third_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Step 3:", className="card-title"),
            html.P(
                "View your top ranked and recommended beers to buy from the Beer52 shop."
            )
        ]
    ), color="#fff", outline=True
)

cards = dbc.Row([dbc.Col(first_card, md=4), dbc.Col(second_card, md=4), dbc.Col(third_card, md=4)])

get_started = dbc.Row(
    children=[
        dbc.Col(
            dbc.Button("Get started", id="btn_get_started", className="beer-btn", size="lg", block=True, href="available")),
    ],
    className='mt-3 mb-3'
)

splash_layout = [jumbotron, cards, get_started]
