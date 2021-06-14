import dash_html_components as html
import dash_bootstrap_components as dbc

from config import beer_df, abv_descriptor


def beer_style_layout(style):
    beer = beer_df[beer_df['strip_style'] == style]
    card = dbc.Card(
        children=[
            dbc.CardBody(
                children=[
                    dbc.Row(
                        children=[
                            dbc.Col(
                                children=[
                                    html.Br(),
                                    dbc.ListGroup(
                                        [
                                            dbc.ListGroupItem(beer.Style),
                                            dbc.ListGroupItem(beer.Category),
                                            dbc.ListGroupItem(f'{beer["Region (on CC syllabus)"].values[0]}'),
                                            dbc.ListGroupItem(
                                                f'SRM = {beer.SRMLow.values[0]} - {beer.SRMHigh.values[0]}'),
                                            dbc.ListGroupItem(
                                                f'IBU = {beer.IBULow.values[0]} - {beer.IBUHigh.values[0]} ({beer["PB Descriptor"].values[0]})'),
                                            dbc.ListGroupItem(
                                                f'ABV = {beer.ABVLow.values[0]}% - {beer.ABVHigh.values[0]}% ({abv_descriptor(beer.ABVAvg.values[0])})'),
                                        ],
                                        flush=True,
                                    ),
                                ],
                                md=6
                            ),
                            dbc.Col(
                                children=[
                                    html.A(
                                        href=beer.Link.values[0],
                                        children=[
                                            dbc.CardImg(src=beer.Image)
                                        ]
                                    )
                                ],
                                md=6
                            ),

                        ]
                    )
                ]
            ),

        ]
    )
    return [card]
