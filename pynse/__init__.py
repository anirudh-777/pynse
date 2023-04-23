import logging
import warnings

# disable all external logging
warnings.filterwarnings("ignore")
logging.disable(logging.DEBUG)
logging.getLogger("scrapy").propagate = False
logging.getLogger("sctapy-playwright").propagate = False
logging.getLogger("scrapy-playwright").setLevel(logging.CRITICAL)
logging.getLogger("scrapy").setLevel(logging.CRITICAL)

from .pynse import get_stock_data
