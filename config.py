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

beer_color_dict = {
    (0, 2): '#F0EEBC',
    (2, 4): '#E8D77D',
    (4, 5): '#DCB332',
    (5, 7): '#D6A531',
    (7, 9): '#C98B28',
    (9, 13): '#BC752C',
    (13, 17): '#A85629',
    (17, 22): '#994320',
    (22, 27): '#812C1E',
    (27, 34): '#671F12',
    (34, 44): '#4D0D0F',
    (44, 100): '#2C0E0F'
}


def srm_color(srm):
    color = [value for key, value in beer_color_dict.items() if ((srm >= key[0]) & (srm < key[1]))]
    return color[0]


def abv_descriptor(abv):
    if abv < 4.5:
        return 'Lower'
    elif (abv >= 4.5) and (abv <= 6):
        return 'Normal'
    elif (abv > 6) and (abv <= 7.5):
        return 'Elevated'
    elif (abv > 7.5) and (abv <= 10):
        return 'High'
    else:
        return 'Very high'
