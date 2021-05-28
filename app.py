import json
import pandas as pd
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State

from main import app
from layout.main import main_layout
from layout.splash import splash_layout
from layout.available import available_layout
from layout.selection import get_selection_layout
from layout.recommendation import get_recommendation_layout

from pypbl.elicitation import BayesPreference
from pypbl.priors import Normal

from config import beer_df, beer_features_df, beer_features_min, beer_features_max
from config import features

# from callbacks import splash  # noqa
from callbacks import available  # noqa
from callbacks import selection  # noqa

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
        return available_layout
    elif pathname == '/selection':
        return get_selection_layout(data)
    elif pathname == '/recommendation':
        available_beers_df = beer_df.loc[data['available'], ['Style'] + features]
        available_beers_df.set_index('Style', inplace=True)
        normalised_available_beers_df = (available_beers_df - beer_features_min) / (
                beer_features_max - beer_features_min)
        model = BayesPreference(data=normalised_available_beers_df, normalise=False)
        model.set_priors([Normal() for _ in features])
        for preference in preference_data['preferences']:
            model.add_strict_preference(beer_df.loc[preference[0], 'Style'], beer_df.loc[preference[1], 'Style'])
        model.infer_weights()
        # table for tasted beers
        tasted_table = model.rank()
        tasted_table['Style'] = tasted_table.index.values

        # table for all beers
        normalised_all_beers_df = (beer_features_df - beer_features_min) / (
                beer_features_max - beer_features_min)
        utilities = [model.weights.dot(row.values) for i, row in normalised_all_beers_df.iterrows()]
        rank_df = pd.DataFrame(utilities, index=normalised_all_beers_df.index.values, columns=['utility'])
        table = rank_df.sort_values(by='utility', ascending=False)
        table['Style'] = table.index.values
        table['Category'] = beer_df.set_index('Style').loc[table.index, 'Category'].values
        table['ABVAvg'] = beer_features_df.loc[table.index, 'ABVAvg'].div(100).values
        table['IBUAvg'] = beer_features_df.loc[table.index, 'IBUAvg'].values
        table['SRMAvg'] = beer_features_df.loc[table.index, 'SRMAvg'].values
        table['ADF(%)'] = beer_features_df.loc[table.index, 'ADF(%)'].values
        table['FGAvg'] = beer_features_df.loc[table.index, 'FGAvg'].values
        table['RelativeBitterness'] = beer_features_df.loc[table.index, 'RelativeBitterness'].values
        table['tasted'] = ["yes" if (beer in tasted_table.index) else "no" for beer in table.index]
        table['Link'] = beer_df.set_index('Style').loc[table.index, 'Link'].values
        cols = ['Style', 'Category', 'utility', 'tasted', 'ABVAvg', 'IBUAvg', 'SRMAvg', 'ADF(%)', 'FGAvg', 'RelativeBitterness', 'Link']
        table = table[cols]
        weights_table = pd.DataFrame({col: [weight] for col, weight in zip(model.data.columns, model.weights)})
        return get_recommendation_layout(tasted_table, table, weights_table)


# update navbar items based on page
@app.callback(
    Output('nav-items', 'children'),
    [Input('url', 'pathname')])
def change_navbar(pathname):  # noqa
    if pathname == '/':
        return []
    elif pathname == '/available':
        navbar_items = [
            dbc.Col(dbc.NavLink("Available", id='available-link', href="available", className='nav_link active')),
            dbc.Col(dbc.NavLink("Selection", id='selection-link', href="selection", className='nav_link')),
            dbc.Col(
                dbc.NavLink("Recommendation", id='recommendation-link', href="recommendation", className='nav_link')
            ),
        ]
    elif pathname == '/selection':
        navbar_items = [
            dbc.Col(dbc.NavLink("Available", id='available-link', href="available", className='nav_link')),
            dbc.Col(dbc.NavLink("Selection", id='selection-link', href="selection", className='nav_link active')),
            dbc.Col(
                dbc.NavLink("Recommendation", id='recommendation-link', href="recommendation", className='nav_link')
            ),
        ]
    elif pathname == '/recommendation':
        navbar_items = [
            dbc.Col(dbc.NavLink("Available", id='available-link', href="available", className='nav_link')),
            dbc.Col(dbc.NavLink("Selection", id='selection-link', href="selection", className='nav_link')),
            dbc.Col(
                dbc.NavLink("Recommendation", id='recommendation-link', href="recommendation",
                            className='nav_link active')
            ),
        ]
    else:
        navbar_items = []
    return navbar_items


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
