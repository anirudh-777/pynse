from pynse.pynse import (get_data_for_stock, get_data_for_stocks,
                         get_stock_symbols)


def test_get_stock_data():
    stock_data = get_data_for_stock("RELIANCE")
    assert stock_data is not None
    assert stock_data.shape[0] == 1
    assert stock_data.shape[1] == 14
    assert stock_data.index.name == "symbol"
    assert stock_data.index[0] == "RELIANCE"


def test_get_data_for_stocks():
    stock_list = ["RELIANCE", "ITC", "SBIN"]
    stock_data = get_data_for_stocks(symbol_list=stock_list)
    assert stock_data is not None
    assert stock_data.shape[0] == 3
    assert stock_data.shape[1] == 14
    assert stock_data.index.name == "symbol"
    assert stock_data.index.tolist().sort() == stock_list.sort()


def test_get_all_stock_symbols():
    symbols = get_stock_symbols()
    assert symbols is not None
    assert len(symbols) > 0
    assert "RELIANCE" in symbols
    assert "ITC" in symbols
    assert "SBIN" in symbols
