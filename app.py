import json
import pandas as pd
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State

from main import app
from layout.main import main_layout
from layout.splash import splash_layout
from layout.beer_style import beer_style_layout

from config import beer_df

# from callbacks import splash  # noqa
# from callbacks import available  # noqa
# from callbacks import selection  # noqa

app.layout = main_layout
server = app.server


# update page based on url
@app.callback(
    Output('page_content', 'children'),
    [Input('url', 'pathname')],
    [State('hidden_data', 'children'),
     State('preference_data', 'children')])
def display_page(pathname, data_str, preference_data_str):  # noqa
    data = json.loads(data_str) if data_str else None
    preference_data = json.loads(preference_data_str) if preference_data_str else None
    if pathname == '/':
        return splash_layout
    elif pathname == '/available':
        return splash_layout
    else:
        return beer_style_layout(pathname.split('/')[1])


# update navbar items based on page
@app.callback(
    Output('shuffle-link', 'href'),
    [Input('url', 'pathname')],
    [State('shuffle-link', 'href')])
def change_shuffle_link(pathname, previous_link):  # noqa
    href = beer_df[beer_df['safe_name'] != previous_link].sample()['safe_name'].values[0]
    return href


# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server(debug=True)
