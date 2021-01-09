import copy
import json

import numpy as np

from dash.dependencies import Input, Output, State
from main import app
from config import beer_df


@app.callback(
    [
        Output("preference_data", "children"),
        Output("left_button", "disabled"),
        Output("right_button", "disabled")
    ],
    [

        Input("left_button", "n_clicks_timestamp"),
        Input("right_button", "n_clicks_timestamp")

    ],
    [
        State("left_card_title", "children"),
        State("right_card_title", "children"),
        State("preference_data", "children"),
        State("hidden_data", "children")
    ]
)
def pbl_update(n_clicks_left, n_clicks_right, left_beer_name, right_beer_name,
               previous_preference_data_str, available_data_str):
    previous_preference_data = json.loads(previous_preference_data_str) if previous_preference_data_str else None
    available_data = json.loads(available_data_str) if available_data_str else None

    # get indexes used
    left_index = int(beer_df[beer_df.beer == left_beer_name].index.values)
    right_index = int(beer_df[beer_df.beer == right_beer_name].index.values)

    n_clicks_left = n_clicks_left if n_clicks_left is not None else 0
    n_clicks_right = n_clicks_right if n_clicks_right is not None else 0

    if n_clicks_left > n_clicks_right:
        preference = [left_index, right_index]
        choice = 'left'
    elif n_clicks_right > n_clicks_left:
        preference = [right_index, left_index]
        choice = 'right'
    else:
        return None, False, False

    if previous_preference_data:
        preference_data = copy.deepcopy(previous_preference_data)
        preference_data['preferences'].append(preference)
        preference_data['tasted'] = list(set(previous_preference_data['tasted'] + preference))
    else:
        preference_data = dict()
        preference_data['preferences'] = [preference]
        preference_data['tasted'] = preference

    preference_data['not_tasted'] = list(set(available_data['available']) - set(preference_data['tasted']))
    preference_data['choice'] = choice
    preference_data['right'] = right_index
    preference_data['left'] = left_index

    if len(preference_data['not_tasted']) > 0:
        return json.dumps(preference_data), False, False
    else:
        print(preference_data)
        return json.dumps(preference_data), True, True


@app.callback(
    [
        Output("left_image", "src"),
        Output("left_card_title", "children"),
        Output("left_description", "children")
    ],
    [
        Input("preference_data", "children")
    ],
    [
        State("left_image", "src"),
        State("left_card_title", "children"),
        State("left_description", "children")
    ]
)
def update_left_beer(preference_data_str, left_image, left_card_title, left_description):
    if preference_data_str:
        preference_data = json.loads(preference_data_str) if preference_data_str else None
        if (preference_data['choice'] == 'right') & (len(preference_data['not_tasted']) > 0):
            if len(preference_data['not_tasted']) > 1:
                next_choice = np.random.choice(preference_data['not_tasted'])
            else:
                next_choice = preference_data['not_tasted'][0]
            return beer_df.loc[next_choice, 'img'], beer_df.loc[next_choice, 'beer'], beer_df.loc[
                next_choice, 'style']
        else:
            return beer_df.loc[preference_data['left'], 'img'], beer_df.loc[preference_data['left'], 'beer'], \
                   beer_df.loc[preference_data['left'], 'style']
    else:
        return left_image, left_card_title, left_description


@app.callback(
    [
        Output("right_image", "src"),
        Output("right_card_title", "children"),
        Output("right_description", "children")
    ],
    [
        Input("preference_data", "children")
    ],
    [
        State("right_image", "src"),
        State("right_card_title", "children"),
        State("right_description", "children")
    ]
)
def update_right_beer(preference_data_str, right_image, right_card_title, right_description):
    if preference_data_str:
        preference_data = json.loads(preference_data_str) if preference_data_str else None
        if (preference_data['choice'] == 'left') & (len(preference_data['not_tasted']) > 0):
            if len(preference_data['not_tasted']) > 1:
                next_choice = np.random.choice(preference_data['not_tasted'])
            else:
                next_choice = preference_data['not_tasted'][0]
            return beer_df.loc[next_choice, 'img'], beer_df.loc[next_choice, 'beer'], beer_df.loc[
                next_choice, 'style']
        else:
            return beer_df.loc[preference_data['right'], 'img'], beer_df.loc[preference_data['right'], 'beer'], \
                   beer_df.loc[
                       preference_data['right'], 'style']
    else:
        return right_image, right_card_title, right_description


@app.callback(
    Output("btn_to_recommendation", "disabled"),
    [
        Input("left_button", "n_clicks"),
        Input("right_button", "n_clicks")

    ]
)
def update_next_btn(left_clicks, right_clicks):
    if left_clicks or right_clicks:
        return False
    else:
        return True
