from pynse.pynse import get_stock_data


def test_get_stock_data():
    stock_list = ["RELIANCE", "ITC", "SBIN"]
    stock_data = get_stock_data(stock_list=stock_list)
    assert stock_data is not None
    assert stock_data.shape[0] == 3
    assert stock_data.shape[1] == 14
    assert stock_data.index.name == "symbol"
    assert stock_data.index.tolist().sort() == stock_list.sort()