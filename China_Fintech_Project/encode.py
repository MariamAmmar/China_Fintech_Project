import pandas as pd


def one_hot_counties(df):
    return pd.get_dummies(df, prefix = 'county_', columns = ['county_code_year14'])
