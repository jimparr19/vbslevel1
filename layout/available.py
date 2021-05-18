import dash_html_components as html
import dash_bootstrap_components as dbc

from config import beer_df

box_options = [{"label": box, "value": box} for box in beer_df.issue.unique()]

beer_options = [{"label": beer.beer, "value": beer.Index} for beer in beer_df.itertuples()]
default_box = beer_df.issue.unique()[0]

radio_options = dbc.FormGroup(
    children=[
        dbc.Label("Beer52 box:"),
        dbc.RadioItems(
            options=box_options,
            value=default_box,
            id="radio_input",
            persistence=True,
            persistence_type='session'
        ),
    ],
)

switches = dbc.FormGroup(
    children=[
        dbc.Label("Available beers for tasting:"),
        dbc.Checklist(
            options=beer_options,
            value=[],
            id="switches_input",
            switch=True,
            persistence=True,
            persistence_type='session'
        ),
    ],
)

# form = dbc.Form([radio_options, switches])

available_layout = [
    dbc.Row(html.P('Select the Beer52 beers available for tasting.')),
    dbc.Row(
        children=[
            dbc.Col(
                children=[
                    dbc.Form([radio_options])
                ],
                md=4
            ),
            dbc.Col(
                children=[
                    dbc.Form([switches]),
                ],
                md=4
            ),
            dbc.Col(
                children=[
                    dbc.Row(
                        children=[
                            dbc.Col(dbc.Button("Next", id="btn_to_selection", size="lg", block=True,
                                               href="selection", disabled=True, className='beer52-btn'))
                        ]
                    ),
                    dbc.Row(
                        children=[
                            dbc.Col(id="available_message", md=12)
                        ]
                    )
                ],
                md=4
            )
        ],
    ),

]
