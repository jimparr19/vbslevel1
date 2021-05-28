import dash_html_components as html
import dash_bootstrap_components as dbc

from config import beer_df


def get_selection_layout(data):
    selection_layout = [
        dbc.Row(html.P('Have a taste of the beers presented and select your preferred beer:')),
        dbc.Row(
            children=[
                dbc.Col(
                    children=[
                        dbc.Card(
                            children=[
                                dbc.CardImg(
                                    id='left_image',
                                    src=beer_df.loc[data['start_left'], 'Image'],
                                    className='selection_img',
                                    top=True,
                                ),
                                dbc.CardBody(
                                    id='left_body',
                                    children=[
                                        dbc.Button(
                                            id='left_button',
                                            children="Select",
                                            block=True,
                                            className='beer-btn mb-3'),
                                        html.H4(beer_df.loc[data['start_left'], 'Style'], id='left_card_title',
                                                className="card-title"),
                                        html.P(beer_df.loc[data['start_left'], 'Category'], id='left_description',
                                               className="card-text"),

                                    ]
                                ),
                            ],
                        )
                    ],
                    md=6,
                ),
                dbc.Col(
                    children=[
                        dbc.Card(
                            children=[
                                dbc.CardImg(
                                    id='right_image',
                                    src=beer_df.loc[data['start_right'], 'Image'],
                                    className='selection_img',
                                    top=True,
                                ),
                                dbc.CardBody(
                                    id='right_body',
                                    children=[
                                        dbc.Button(
                                            id='right_button',
                                            children="Select",
                                            block=True,
                                            className='beer-btn mb-3'),
                                        html.H4(beer_df.loc[data['start_right'], 'Style'], id='right_card_title',
                                                className="card-title"),
                                        html.P(beer_df.loc[data['start_right'], 'Category'], id='right_description',
                                               className="card-text"),

                                    ]
                                ),
                            ],
                        )
                    ],
                    md=6,
                ),
            ],
        ),
        dbc.Row(
            children=[
                dbc.Col(
                    md=9
                ),
                dbc.Col(
                    children=[
                        dbc.Col(dbc.Button("Next",
                                           id="btn_to_recommendation",
                                           className='beer-btn',
                                           size="lg",
                                           block=True,
                                           disabled=True,
                                           href="recommendation")),
                    ],
                    md=12
                )
            ],
            className='mt-3 mb-3')
    ]
    return selection_layout
