import os
import pandas as pd
import dash_bootstrap_components as dbc

config_path = os.path.dirname(__file__)

# Style
THEME = dbc.themes.BOOTSTRAP

# Data
beer_df = pd.read_pickle(os.path.join(config_path, 'beer_df_1.pickle'))

# Default beers
available_beers = beer_df[beer_df.Syllabus == 'all']['Style'].values

available_beers = [
    'Best Bitter',
    'Czech Premium Pale Lager',
    'Gueuze',
    'German Pils',
    'Irish Stout',
    'Kölsch',
    'Sweet Stout',
    'Weissbier',
    'Witbier',
]

features = ['ABVAvg', 'IBUAvg', 'SRMAvg', 'ADF(%)', 'FGAvg', 'RelativeBitterness']

beer_features_df = beer_df.loc[:, ['Style'] + features]
beer_features_df.set_index('Style', inplace=True)

feature_ranges = {i: (beer_features_df[i].min(), beer_features_df[i].max()) for i in features}

beer_features_min = pd.Series({key: feature_ranges[key][0] for key in features})
beer_features_max = pd.Series({key: feature_ranges[key][1] for key in features})
