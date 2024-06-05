import os
import pandas as pd
import requests
from functools import reduce

from datetime import datetime
import pandas_datareader.data as web
from pytrends.request import TrendReq

# ---------------------------------- ALFRED ---------------------------------- #
def get_alfred_ticker(i):
    index2ticker = {
        "CPI": "CPIAUCSL",
        "CCPI": "CPILFESL",
        "FCPI": "CPIUFDSL",
        "GCPI": "CUSR0000SETB01"
    }

    return index2ticker.get(i, None)

def get_alfred(seid, api_key='env'):
    if api_key == 'env':
        api_key = os.environ['ALFRED_API_KEY']
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={seid}&api_key={api_key}&file_type=json"
    response = requests.get(url).json()
    return response

def get_alfred_data(index, seid, api_key='env'):
    """Get (from Alfred) data and returns it as a DataFrame

    Args:
        seid (str): Series ID

    Returns:
        DataFrame: the time series
    """
    # Get Request
    response = get_alfred(seid, api_key)

    # Only keep the observations part
    data = response['observations']

    # Convert to DF
    df = pd.DataFrame(data)[['date','value']]

    # Make sur that data is well formatted
    df['date'] = pd.to_datetime(df['date'])
    df['value'] = df['value'].astype(float)
    df = df.rename(columns={'value': index})

    return df

def alfred_dataset(indices, api_key='env'):
    dfs = [get_alfred_data(i, get_alfred_ticker(i), api_key) for i in indices]
    df = reduce(lambda x, y: x.merge(y, on='date'), dfs)
    return df


# ---------------------------------- GTrends --------------------------------- #
def gtrend_dataset(keywords, start_date='2010-01-01', end_date=None):
    pytrends = TrendReq(hl='en-US', tz=360)  # hl is the host language for the API, tz is the time zone offset
    end_date = datetime.now().strftime('%Y-%m-%d') if end_date == None else end_date
    timeframe = f'{start_date} {end_date}'
    pytrends.build_payload(kw_list=keywords, timeframe=timeframe)
    data = pytrends.interest_over_time()[keywords].reset_index()
    return data
