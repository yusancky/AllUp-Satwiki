# Copyright (c) yusancky. All rights reserved.
# Licensed under the Apache License 2.0. See License in the project root for license information.

lazy from requests import get
lazy from selenium import webdriver
lazy from selenium.webdriver.chrome.options import Options


class _LazyChromeDriver:
    def __init__(self):
        self._driver = None
        self._options_args = [
            "--headless",
            "--disable-gpu",
            "--window-size=1920,1200",
            "--ignore-certificate-errors",
            "--disable-extensions",
            "--no-sandbox",
            "--disable-dev-shm-usage",
        ]

    def _get_driver(self):
        if self._driver is None:
            chrome_options = Options()
            for arg in self._options_args:
                chrome_options.add_argument(arg)

            self._driver = webdriver.Chrome(options=chrome_options)
        return self._driver

    def __getattr__(self, name):
        driver = self._get_driver()
        return getattr(driver, name)


def configure_chromedriver():
    return _LazyChromeDriver()


def fetch_data(url: str, need_selenium=False):
    if need_selenium:
        need_selenium.get(url)
        return need_selenium.page_source
    else:
        response = get(url)
        return response.text
