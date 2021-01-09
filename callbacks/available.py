import json
import numpy as np

import dash_bootstrap_components as dbc

from config import beer_df
from dash.dependencies import Input, Output
from main import app


@app.callback(
    Output("switches_input", "value"),
    [
        Input("radio_input", "value"),
    ]
)
def update_available_beers(radio_value):
    available_beers = beer_df[beer_df.issue == radio_value]['beer'].values
    available_beers_index = [row.Index for row in beer_df.itertuples() if row.beer in available_beers]
    return available_beers_index


@app.callback(
    [
        Output("hidden_data", "children"),
        Output("btn_to_selection", "disabled"),
        Output('available_message', 'children')
    ],
    [
        Input("switches_input", "value"),
    ]
)
def update_hidden_data(switches_value):
    if len(switches_value) > 1:
        data = dict()
        data['available'] = switches_value
        chosen_beers = np.random.choice(switches_value, 2, replace=False)
        data['start_left'] = int(chosen_beers[0])
        data['start_right'] = int(chosen_beers[1])
        return json.dumps(data), False, None
    else:
        message = dbc.Alert("A minimum of two beers must be selected.", color="warning")
        return None, True, message
