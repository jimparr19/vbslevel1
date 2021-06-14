import dash_html_components as html
import dash_bootstrap_components as dbc

from config import beer_df, srm_color


def beer_card(style, category, srm):
    card = dbc.Card(
        children=[
            dbc.CardBody(
                [
                    html.A(
                        href=f'/{style.strip().lower().replace(" ", "")}',
                        children=[
                            html.H5(style, className="card-title"),
                            html.P(category, className="card-text")
                        ]
                    )
                ]
            )
        ],
        style={'background-color': srm_color(srm)},
        inverse=False if srm < 10 else True,
    )
    return card


cards = [beer_card(row.Style, row.Category, row.SRMAvg) for row in beer_df.sort_values(by='SRMAvg').itertuples()]

splash_layout = [
    dbc.CardColumns(
        cards
    )
]
