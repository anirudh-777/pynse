"""
pynse - This module contains functions to fetch data from the NSE website
"""

import pandas as pd

from pynse.constants import URLS
from pynse.request_utils import make_nse_request
from pynse.scraping import NseStockSpider, run_spider


def get_stock_data(stock_list=None):
    """get stock data for a list of stocks
    Args:
        stock_list (List, optional): List of stocks to fetch data for. Defaults to None.
    Returns:
        DataFrame: Returns a dataframe with data for stocks in stock_list
    """
    stock_list = stock_list or []
    if not stock_list:
        return

    stock_data_list = []

    for stock in stock_list:
        stock_data = make_nse_request(URLS.NSE_URLS.STOCK_DATA.format(stock))
        if not stock_data:
            print("No data found for: ", stock)
            continue
        stock_data_dict = {
            "exchange": "NSE",
            "symbol": stock,
            "name": stock_data["info"]["companyName"],
            "last_price": stock_data["priceInfo"]["lastPrice"],
            "last_price_time": stock_data["metadata"]["lastUpdateTime"],
            "price_change": stock_data["priceInfo"]["change"],
            "percent_change": stock_data["priceInfo"]["pChange"],
            "price_band": stock_data["priceInfo"]["pPriceBand"],
            "macro_sector": stock_data["industryInfo"]["macro"],
            "sector": stock_data["industryInfo"]["sector"],
            "industry": stock_data["industryInfo"]["industry"],
            "basic_industry": stock_data["industryInfo"]["basicIndustry"],
            "pe_ratio": stock_data["metadata"]["pdSymbolPe"],
            "sector_pe_ratio": stock_data["metadata"]["pdSectorPe"],
            "ipo_date": stock_data["metadata"]["listingDate"],
        }
        stock_data_list.append(stock_data_dict)

    # create a stock data dataframe
    stock_data = pd.DataFrame(stock_data_list)
    stock_data = stock_data.set_index("symbol")
    return stock_data


def get_nse_advances_declines():
    """Get advance decline data for the current day
    Returns:
        Dict: Returns a dict with advance decline data
    """
    adv_dec = make_nse_request(URLS.NSE_URLS.ADV_DEC_ALL)

    adv_dec_dict = {
        "advances": adv_dec["advances"],
        "declines": adv_dec["declines"],
        "unchanged": adv_dec["unchanged"],
        "total": adv_dec["total"],
        "datetime": adv_dec["as_on_date"],
    }
    return adv_dec_dict


if __name__ == "__main__":
    stock_list = ["RELIANCE", "ITC", "SBIN"]
    stock_data = get_stock_data(stock_list=stock_list)
    print(stock_data)
