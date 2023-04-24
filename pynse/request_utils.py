"""
This file contains utility functions to make requests to the NSE website.
"""

import requests


def get_nse_headers():
    headers = {
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "Sec-Fetch-User": "?1",
        "Accept": "*/*",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
    }
    return headers


def make_nse_request(url):
    headers = get_nse_headers()
    try:
        res = requests.get(url, headers=headers).json()
    except ValueError:
        s = requests.Session()
        res = s.get("http://nseindia.com", headers=headers)
        res = s.get(url, headers=headers).json()
    return res
