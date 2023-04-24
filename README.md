# pynse
Python library to get stock data from the NSE website.

## Basic Usage

Get a stock's data as a pandas dataframe.

```
In [1]: from pynse import get_stock_data

In [2]: data = get_stock_data(['SBIN', 'RELIANCE'])
Fetching data for:  RELIANCE
Fetching data for:  SBIN

In [3]: print(data)
         exchange        macro_sector                      sector            industry          basic_industry                           name    market_cap  pe_ratio  sector_pe_ratio  shares_outstanding     ipo_date price_band
symbol
RELIANCE      NSE              Energy  Oil Gas & Consumable Fuels  Petroleum Products  Refineries & Marketing   Reliance Industries Limited   1.590590e+08     35.91            21.46         79460671.55  29-Nov-1995    No Band
SBIN          NSE  Financial Services          Financial Services               Banks      Public Sector Bank           State Bank of India   4.839817e+07     10.80            15.98         20843832.78  01-Mar-1995    No Band
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