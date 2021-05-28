import dash_html_components as html
import dash_bootstrap_components as dbc

from config import beer_df, available_beers

beer_options = [{"label": beer.Style, "value": beer.Index} for beer in beer_df.itertuples()]
available_beers_index = [row.Index for row in beer_df.itertuples() if row.Style in available_beers]

switches = dbc.FormGroup(
    children=[
        dbc.Label("Available beers for tasting:"),
        dbc.Checklist(
            options=beer_options,
            value=available_beers_index,
            id="switches_input",
            switch=True,
            persistence=True,
            persistence_type='session'
        ),
    ],
)


available_layout = [
    dbc.Row(html.P('Select the beer styles available for tasting.')),
    dbc.Row(
        children=[
            dbc.Col(
                children=[
                    dbc.Form([switches]),
                ],
                md=6
            ),
            dbc.Col(
                children=[
                    dbc.Row(
                        children=[
                            dbc.Col(dbc.Button("Next", id="btn_to_selection", size="lg", block=True,
                                               href="selection", disabled=True, className='beer-btn'))
                        ]
                    ),
                    dbc.Row(
                        children=[
                            dbc.Col(id="available_message", md=12)
                        ]
                    )
                ],
                md=6
            )
        ],
    ),

]
