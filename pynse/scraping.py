import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.reactor import install_reactor

from pynse.constants import SELECTOR_PATHS, URLS


class NseStockSpider(scrapy.Spider):
    name = "stocks"
    allowed_domains = ["www.nseindia.com"]
    url = "".join(URLS.NSE_URLS.values())

    def __init__(self, stock_list, stock_data) -> None:
        self.stock_list = stock_list
        self.stock_data = stock_data
        super().__init__()

    def start_requests(self):
        all_stocks = self.stock_list

        for symbol in all_stocks:
            symbol = symbol.replace("&", "%26")
            yield scrapy.Request(
                url=self.url.format(symbol),
                callback=self.parse,
                meta={"playwright": True, "playwright_include_page": True},
                errback=self.errback_close_page,
            )

    async def parse(self, response):
        stock_name = response.url.split("=")[-1]
        print("Fetching data for: ", stock_name)
        page = response.meta["playwright_page"]

        for selector in SELECTOR_PATHS.SECTOR_PATHS:
            await page.wait_for_selector(selector)

        macro_sector = await page.locator(
            SELECTOR_PATHS.SECTOR_PATHS.MACRO_SECTOR
        ).all_text_contents()
        sector = await page.locator(
            SELECTOR_PATHS.SECTOR_PATHS.SECTOR
        ).all_text_contents()
        industry = await page.locator(
            SELECTOR_PATHS.SECTOR_PATHS.INDUSTRY
        ).all_text_contents()
        basic_industry = await page.locator(
            SELECTOR_PATHS.SECTOR_PATHS.BASIC_INDUSTRY
        ).all_text_contents()
        name = await page.locator(SELECTOR_PATHS.SECTOR_PATHS.NAME).all_text_contents()
        market_cap = await page.locator(
            SELECTOR_PATHS.SECTOR_PATHS.MARKET_CAP
        ).all_text_contents()
        pe_ratio = await page.locator(
            SELECTOR_PATHS.SECTOR_PATHS.PE_RATIO
        ).all_text_contents()
        sector_pe_ratio = await page.locator(
            SELECTOR_PATHS.SECTOR_PATHS.SECTOR_PE_RATIO
        ).all_text_contents()
        shares_outstanding = await page.locator(
            SELECTOR_PATHS.SECTOR_PATHS.SHARES_OUTSTANDING
        ).all_text_contents()
        ipo_date = await page.locator(
            SELECTOR_PATHS.SECTOR_PATHS.IPO_DATE
        ).all_text_contents()
        price_band = await page.locator(
            SELECTOR_PATHS.SECTOR_PATHS.PRICE_BAND
        ).all_text_contents()

        stock_name = stock_name.replace("%26", "&")

        self.stock_data.append(
            {
                "exchange": "NSE",
                "symbol": stock_name,
                "macro_sector": macro_sector[0],
                "sector": sector[0],
                "industry": industry[0],
                "basic_industry": basic_industry[0],
                "name": name[0],
                "market_cap": float(
                    market_cap[0].replace(",", "")
                    if market_cap[0] not in ["NA", "-"]
                    else 0
                ),
                "pe_ratio": float(
                    pe_ratio[0].replace(",", "")
                    if pe_ratio[0] not in ["NA", "-"]
                    else 0
                ),
                "sector_pe_ratio": float(
                    sector_pe_ratio[0].replace(",", "")
                    if sector_pe_ratio[0] not in ["NA", "-"]
                    else 0
                ),
                "shares_outstanding": float(
                    shares_outstanding[0].replace(",", "")
                    if shares_outstanding[0] not in ["NA", "-"]
                    else 0
                ),
                "ipo_date": ipo_date[0],
                "price_band": price_band[0],
            }
        )

        await page.close()

    async def errback_close_page(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()


def run_spider(stock_list):
    stock_data = []
    install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")
    crawler_process = CrawlerProcess(
        settings={
            "DOWNLOAD_HANDLERS": {
                "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
                "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            }
        }
    )
    stock_data = []
    crawler_process.crawl(NseStockSpider, stock_list=stock_list, stock_data=stock_data)
    crawler_process.start()
    crawler_process.join()

    return stock_data
