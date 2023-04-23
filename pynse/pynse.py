import pandas as pd

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

    stock_data = run_spider(stock_list=stock_list)

    # create a stock data dataframe
    stock_data = pd.DataFrame(stock_data)
    stock_data = stock_data.set_index("symbol")
    return stock_data


if __name__ == "__main__":
    stock_list = ["RELIANCE", "ITC", "SBIN"]
    stock_data = get_stock_data(stock_list=stock_list)
    print(stock_data)
