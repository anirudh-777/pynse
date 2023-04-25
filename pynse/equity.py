"""
This file contains functions to get data for stocks in the equity segment of NSE.
"""


import datetime as dt

import pandas as pd

from pynse.constants import URLS
from pynse.request_utils import request_nse_csv, request_nse_json


def get_stock_quote(symbol):
    """
    Get the quote for a stock.
    :param symbol: The symbol for the stock.
    :return: A dictionary with the quote for the stock.
    """

    stock_quote = request_nse_json(URLS.NSE_URLS.STOCK_DATA.format(symbol))

    if not stock_quote:
        print("No data found for: ", symbol)
        return {}

    stock_quote_ext = request_nse_json(URLS.NSE_URLS.STOCK_DATA_EXT.format(symbol))
    stock_quote.update(stock_quote_ext)

    return stock_quote


def get_stock_ohlcv(symbol):
    """
    Get the OHLCV data for a stock.
    :param symbol: The symbol for the stock.
    :return: A dictionary with the OHLCV data for the stock.
    """

    stock_data = get_stock_quote(symbol)

    if not stock_data:
        return {}

    stock_ohlcv = {
        "Open": stock_data["priceInfo"]["open"],
        "High": stock_data["priceInfo"]["intraDayHighLow"]["max"],
        "Low": stock_data["priceInfo"]["intraDayHighLow"]["min"],
        "Close": stock_data["priceInfo"]["lastPrice"],
        "Volume": stock_data["securityWiseDP"]["quantityTraded"]
    }

    return stock_ohlcv


def get_stock_historical_data(symbol, start_date, end_date):
    """
    Get the historical data for a stock.
    :param symbol: The symbol for the stock.
    :param start_date: The start date for the historical data.
    :param end_date: The end date for the historical data.
    :return: A dictionary with the historical data for the stock.
    """

    diff = end_date - start_date
    # check if diff is more than 5 years
    if diff.days > 1825:
        print("The maximum time period for historical data is 5 years. Please reduce the time period.")
        return {}

    if diff.days > 365:
        mid_date = pd.to_datetime(start_date) + dt.timedelta(days=365)
        return pd.concat([get_stock_historical_data(symbol, start_date, mid_date), get_stock_historical_data(symbol, mid_date, end_date)])

    # convert to date format
    start_date = start_date.strftime("%d-%m-%Y")
    end_date = end_date.strftime("%d-%m-%Y")

    stock_historical_data = request_nse_csv(URLS.NSE_URLS.STOCK_HISTORICAL_DATA_CSV.format(symbol, start_date, end_date))

    stock_historical_data.columns = [col.strip() for col in stock_historical_data.columns]
    stock_historical_data = stock_historical_data.set_index("Date")

    return stock_historical_data

