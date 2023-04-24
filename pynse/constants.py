import enum


class BaseEnum(str, enum.Enum):

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def values(cls):
        return [e.value for e in cls]

class URLS(object):
    class NSE_URLS(BaseEnum):
        BASE_URL = "https://www.nseindia.com"
        GET_QUOTES = "/get-quotes/equity"
        STOCKS_URL_SUFFIX = "?symbol={}"
        ADV_DEC_ALL = "https://www.nseindia.com/api/snapshot-capital-market-ews"
        STOCK_DATA = "https://www.nseindia.com/api/quote-equity?symbol={}"
        MARKET_STATUS = "https://www.nseindia.com/api/marketStatus"
        SECURITIES_CSV = "https://archives.nseindia.com/content/equities/EQUITY_L.csv"
        INDICES_CSV = "https://www.nseindia.com/api/allIndices"
