import os
import pandas as pd
import dash_bootstrap_components as dbc

config_path = os.path.dirname(__file__)

# Style
THEME = dbc.themes.BOOTSTRAP

# Data
beer_df = pd.read_pickle(os.path.join(config_path, 'beer_df_1.pickle'))

# Default beers
available_beers = beer_df[beer_df.issue_number == 59]['beer'].values


features = ['abv', 'hoppy', 'malty', 'sour', 'floral', 'fruit', 'sweet', 'smooth', 'bitter']
