# Copyright (c) yusancky. All rights reserved. 
# Licensed under the Apache License 2.0. See License in the project root for license information. 

from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def configure_chromedriver():
    chrome_options = Options()
    for option in ['--headless','--disable-gpu','--window-size=1920,1200','--ignore-certificate-errors','--disable-extensions','--no-sandbox','--disable-dev-shm-usage']:
        chrome_options.add_argument(option)
    return webdriver.Chrome(options = chrome_options)

def fetch_data(url,need_selenium = False):
    if need_selenium:
        need_selenium.get(url)
        return need_selenium.page_source
    else:
        response = get(url)
        return response.text