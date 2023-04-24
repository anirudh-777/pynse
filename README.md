# pynse
Python library to get stock data from the NSE website.

## Basic Usage

Get a stock's info as a pandas dataframe.

```
In [1]: from pynse import get_data_for_stock

In [2]: data = get_data_for_stock("RELIANCE")

In [3]: print(data)
         exchange                         name  last_price       last_price_time  price_change  percent_change  ...                      sector            industry          basic_industry pe_ratio sector_pe_ratio     ipo_date
symbol                                                                                                          ...
RELIANCE      NSE  Reliance Industries Limited      2360.5  24-Apr-2023 16:00:00          11.5         0.48957  ...  Oil Gas & Consumable Fuels  Petroleum Products  Refineries & Marketing    35.95           21.58  29-Nov-1995

[1 rows x 14 columns]
```

Fetch data for multiple stocks

```
In [4]: from pynse import get_data_for_stocks

In [5]: data = get_data_for_stocks(["RELIANCE", "ITC", "SBIN"])

In [6]: print(data)
         exchange                         name  last_price       last_price_time  price_change  percent_change  ...                      sector            industry          basic_industry pe_ratio sector_pe_ratio     ipo_date
symbol                                                                                                          ...
RELIANCE      NSE  Reliance Industries Limited      2360.5  24-Apr-2023 16:00:00         11.50        0.489570  ...  Oil Gas & Consumable Fuels  Petroleum Products  Refineries & Marketing    35.95           21.58  29-Nov-1995
ITC           NSE                  ITC Limited       408.3  24-Apr-2023 16:00:00          0.05        0.012247  ...  Fast Moving Consumer Goods    Diversified FMCG        Diversified FMCG    28.38           21.58  23-Aug-1995
SBIN          NSE          State Bank of India       553.8  24-Apr-2023 16:00:00         10.65        1.960784  ...          Financial Services               Banks      Public Sector Bank    10.77           16.17  01-Mar-1995

[3 rows x 14 columns]
```


## Dev Setup

### Prerequisites
* Have python 3.8+ installed.
* Create and activate a python virtual env to install pynse and its related packages.

### Setup
* Run `export BASE_REPO_PATH="Folder where nsepy checked out"`
* Install the required packages - `pip install -r $BASE_REPO_PATH/requirements.txt`
* Build the pynse package - `cd $BASE_REPO_PATH; python setup.py develop`

### Run Tests
```
cd $BASE_REPO_PATH/tests
pytest -svvv --log-level=INFO --log-cli-level=INFO <test_file.py>
```
