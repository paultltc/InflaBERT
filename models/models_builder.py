from statsmodels.tsa.arima.model import ARIMA
import statsmodels.api as sm

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

def nowcaster(df, xcols, ycol, start=None, end=None, verbose=True):
    # Select the right timeframe
    if not start is None:
        df = df[df.date >= start]
    if not end is None:
        df = df[df.date <= end]

    # Get our response variable: CPI
    y = df[ycol]

    # Build our regressors
    X = df[xcols]
    X = sm.add_constant(X)

    # Build nowcaster
    nowcaster = sm.OLS(y, X)
    nowcaster_res = nowcaster.fit()

    if verbose:
        print(nowcaster_res.summary())

    return nowcaster, nowcaster_res
