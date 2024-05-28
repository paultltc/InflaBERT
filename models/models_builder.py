from statsmodels.tsa.arima.model import ARIMA
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd
from dateutil.relativedelta import relativedelta

def asset_arima(df, asset, ar=0, i=0, ma=12, verbose=True):
    """Create the ARIMA model for the selected asset

    Args:
        df (_type_): _description_
        asset (str): Asset for the arima
        ar (int, optional): AR. Defaults to 0.
        i (int, optional): I. Defaults to 0.
        ma (int, optional): MA. Defaults to 12.
        verbose (bool, optional): If summary wanted. Defaults to True.

    Returns:
        _type_: _description_
    """
    # Create the ARIMA model
    model = ARIMA(endog=df[asset], order=(ar, i, ma))

    # Fit the model to the given data
    model_res = model.fit()

    if verbose:
        print(model_res.summary())

    return model, model_res


def nowcaster(df, xcols, ycol, train_range, tau=60, verbose=True):
    # Get the t-time index
    #t_idx = df[df.date == t].index.values[0]
    
    # Get the rolling-Tau window
    #df = df.iloc[t_idx-tau:t_idx]
    df = df[df.date.isin(train_range)]

    # Get our response variable: CPI
    y = df[ycol]

    # Build our regressors
    X = df[xcols]
    X = sm.add_constant(X)

    # Build nowcaster
    nowcaster = sm.OLS(y, X).fit()

    if verbose:
        print(nowcaster.summary())

    return nowcaster

def forecast_ma(df, indices, t, k=1, J=12, recursive=False):
    # Get the t-time index
    t_idx = df[df.date == t].index.values[0]

    # Recursive computation
    if recursive:
        # Get the rolling-J window
        dfJ = df.iloc[t_idx-J:t_idx][indices].copy()

        for i in range(k):
            fi = dfJ.iloc[-J:].mean() 
            fi['date'] = t + relativedelta(months=i)
            dfJ = dfJ._append(fi, ignore_index=True)

        return dfJ.iloc[-k:]

    else:
        res = []

        for i in range(k):
            # Get the rolling-J window
            dfJ = df.iloc[t_idx+i-J:t_idx+i][indices].copy()
            fi = dfJ.iloc[-J:].mean() 
            fi['date'] = t + relativedelta(months=i)
            res.append(fi)

        return pd.DataFrame(res)

def forecast(df, model, xcols, ycol, t, k=1, J=12, yearly=False, dyn=False):
    # Build nowcaster
    if dyn:
        model = nowcaster(df, xcols, ycol, t - relativedelta(months=1), verbose=False)
    index_forecasts = forecast_ma(df, xcols, t, k, J)
    model_forecast = model.predict(sm.add_constant(index_forecasts[xcols]))
    if yearly:
        model_forecast = (model_forecast + 1)**12 - 1
    return pd.DataFrame({'date': index_forecasts['date'], 'forecast': model_forecast})

