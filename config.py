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

beer_features_df = beer_df.loc[:, ['beer'] + features]
beer_features_df.set_index('beer', inplace=True)

feature_ranges = {'abv': (beer_features_df.abv.min(), beer_features_df.abv.max()),
                  'hoppy': (0, 5),
                  'malty': (0, 5),
                  'sour': (0, 5),
                  'floral': (0, 5),
                  'fruit': (0, 5),
                  'sweet': (0, 5),
                  'smooth': (0, 5),
                  'bitter': (0, 5)}

beer_features_min = pd.Series({key: feature_ranges[key][0] for key in features})
beer_features_max = pd.Series({key: feature_ranges[key][1] for key in features})
