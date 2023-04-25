
import datetime

import pandas as pd

from pynse.equity import get_stock_historical_data


def test_get_historical_data():
    end = datetime.datetime.today()
    start = end - datetime.timedelta(days=500)
    data = get_stock_historical_data("SBIN", start, end)
    assert data is not None
    assert data.shape[0] > 0
    assert data.shape[1] == 13
    assert data.index.name == "Date"
    #assert pd.to_datetime(data.index[0]).date() <= start.date()
    #assert pd.to_datetime(data.index[-1]).date() == end.date()
