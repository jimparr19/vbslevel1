import dash_html_components as html
import dash_bootstrap_components as dbc

from config import beer_df, srm_color


def beer_style_layout(style):
    beer = beer_df[beer_df['safe_name'] == style]
    card = dbc.Card(
        children=[
            dbc.CardBody(
                children=[
                    dbc.Row(
                        children=[
                            dbc.Col(
                                children=[
                                    html.H5(beer.Style, className="card-title"),
                                    html.P(beer.Region, className="card-text"),
                                    html.Br(),
                                    dbc.ListGroup(
                                        [
                                            dbc.ListGroupItem(
                                                f'PB - {beer["PB Descriptor"].values[0]} (IBU {beer.IBULow.values[0]} - {beer.IBUHigh.values[0]})'),
                                            dbc.ListGroupItem(
                                                f'C - {beer["SRM Descriptor"].values[0]} (SRM {beer.SRMLow.values[0]} - {beer.SRMHigh.values[0]})',
                                                style={'background-color': srm_color(beer.SRMAvg.values[0]),
                                                       'color': '#212529' if beer.SRMAvg.values[0] < 10 else '#FFF'}),
                                            dbc.ListGroupItem(
                                                f'ABV - {beer["ABV Descriptor"].values[0]} ({beer.ABVLow.values[0]}% - {beer.ABVHigh.values[0]}%)'),

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
                                            dbc.CardImg(src=beer.img)
                                        ]
                                    ),
                                    html.P(beer.Example, className="text-center")

                                ],
                                md=6
                            ),

                        ]
                    ),
                    dbc.CardLink("Virtual Beer School", href=beer.Link.values[0], external_link=True),
                    dbc.CardLink("Pints and Panels", href=beer.PintsLink.values[0], external_link=True),
                ]
            ),

        ]
    )
    return [card]
