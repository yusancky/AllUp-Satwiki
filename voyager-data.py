# Copyright (c) yusancky. All rights reserved. 
# Licensed under the Apache License 2.0. See License in the project root for license information. 

from os import environ
from pwiki.wiki import Wiki
from re import compile,findall
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import localtime,strftime
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

chrome_service = Service(ChromeDriverManager(chrome_type = ChromeType.CHROMIUM).install())
chrome_options = Options()
for option in ["--headless","--disable-gpu","--window-size=1920,1200","--ignore-certificate-errors","--disable-extensions","--no-sandbox","--disable-dev-shm-usage"]:
    chrome_options.add_argument(option)
driver = webdriver.Chrome(service = chrome_service,options = chrome_options)

driver.get("https://voyager.jpl.nasa.gov/mission/status/")
page_source = driver.page_source

sections = ["km","au","kms","aus","speed","lt"]
voy_data = "<includeonly>{{ #switch: {{{id}}} | t = time | 1 = {{ #switch: {{{section}}} | km = data1 | au = data2 | kms = data3 | aus = data4 | speed = data5 | lt = data6 | #default = 请输入正确的选项名！}} | 2 = {{ #switch: {{{section}}} | km = data7 | au = data8 | kms = data9 | aus = data10 | speed = data11 | lt = data12 | #default = 请输入正确的选项名！}} | #default = 请输入正确的编号！ }}</includeonly><noinclude>[[Category:模板]]{{documentation}}</noinclude>".replace("time",strftime("%Y年%m月%d日%H时",localtime()))
cnt = 0
for id in [1,2]:
    for section in sections:
        cnt += 1
        data_re = compile(f'id="voy{id}_{section}">(.*)</div>')
        findall_res = findall(data_re,page_source)
        voy_data = voy_data.replace(f"data{cnt} ",f"{findall_res[0]} ")

wiki = Wiki("sat.huijiwiki.com","雨伞CKY",environ["SATWIKI_PASSWORD"])
wiki.edit("模板:旅行者距离数据",generate_data(),"Edit via auto-update-satwiki@1.3.1 / powered by GitHub Actions")