import enum


class BaseEnum(str, enum.Enum):

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def values(cls):
        return [e.value for e in cls]



class SELECTOR_PATHS(object):
    class SECTOR_PATHS(BaseEnum):
        MACRO_SECTOR = '#industryInfo > tbody > tr > td:nth-child(1)'
        SECTOR = '#industryInfo > tbody > tr > td:nth-child(2)'
        INDUSTRY = '#industryInfo > tbody > tr > td:nth-child(3)'
        BASIC_INDUSTRY = '#industryInfo > tbody > tr > td:nth-child(4)'
        NAME = '#quoteName'
        MARKET_CAP = '#orderBookTradeTMC'
        PE_RATIO = '#equityInfo > tbody > tr > td:nth-child(7)'
        SECTOR_PE_RATIO = '#equityInfo > tbody > tr > td:nth-child(8)'
        SHARES_OUTSTANDING = '#orderBookTradeFFMC'
        IPO_DATE = '#equityInfo > tbody > tr > td:nth-child(5)'
        PRICE_BAND = '#pricebandVal'


class URLS(object):
    class NSE_URLS(BaseEnum):
        BASE_URL = "https://www.nseindia.com"
        GET_QUOTES = "/get-quotes/equity"
        STOCKS_URL_SUFFIX = "?symbol={}"
