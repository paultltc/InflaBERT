import pandas as pd
import requests
from functools import reduce

def get_ticker(i):
    index2ticker = {
        "CPI": "CPIAUCSL",
        "CCPI": "CPILFESL",
        "FCPI": "CPIUFDSL",
        "GCPI": "CUSR0000SETB01"
    }

    return index2ticker.get(i, None)

def get_alfred(seid, api_key="5a44914abc36f51a44be01898453aa15"):
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={seid}&api_key={api_key}&file_type=json"
    response = requests.get(url).json()
    return response

def get_alfred_data(index, seid, api_key="5a44914abc36f51a44be01898453aa15"):
    """Get (from Alfred) data and returns it as a DataFrame

    Args:
        seid (str): Series ID
        api_key (str, optional): API KEY. Defaults to "5a44914abc36f51a44be01898453aa15".

    Returns:
        DataFrame: the time series
    """
    # Get Request
    response = get_alfred(seid)

    # Only keep the observations part
    data = response['observations']

    # Convert to DF
    df = pd.DataFrame(data)[['date','value']]

    # Make sur that data is well formatted
    df['date'] = pd.to_datetime(df['date'])
    df['value'] = df['value'].astype(float)
    df = df.rename(columns={'value': index})

    return df

def alfred_dataset(indices):
    dfs = [get_alfred_data(i, get_ticker(i)) for i in indices]
    df = reduce(lambda x, y: x.merge(y, on='date'), dfs)
    return df

