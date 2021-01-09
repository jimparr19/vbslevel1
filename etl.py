import pandas as pd

data_file = 'data/beers.csv'


def get_beer_df():
    beer_df = pd.read_csv(data_file)
    return beer_df


def clean_data(df):
    df['img'] = df['img'].apply(lambda x: '/assets/beers/' + x)
    df['buy'] = df['buy'].apply(lambda x: '[shop](' + x + ')')
    return pd.DataFrame.copy(df, deep=True)


if __name__ == '__main__':
    beer_df = get_beer_df()
    beer_df_clean = clean_data(beer_df)
    unique_id = '1'#pd.datetime.now().strftime('%Y%m%d%H%M')
    beer_df_clean.to_pickle('beer_df_{}.pickle'.format(unique_id))
