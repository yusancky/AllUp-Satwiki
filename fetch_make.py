# Copyright (c) yusancky. All rights reserved. 
# Licensed under the Apache License 2.0. See License in the project root for license information. 

from os import system
from re import compile,findall
from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import localtime,strftime

def configure_chromedriver():
    chrome_service = Service('/usr/local/share/chrome_driver/chromedriver')
    chrome_options = Options()
    for option in ['--headless','--disable-gpu','--window-size=1920,1200','--ignore-certificate-errors','--disable-extensions','--no-sandbox','--disable-dev-shm-usage']:
        chrome_options.add_argument(option)
    global chromedriver
    chromedriver = webdriver.Chrome(service = chrome_service,options = chrome_options)

def fetch_data(url,need_selenium = False):
    if need_selenium:
        chromedriver.get(url)
        return chromedriver.page_source
    else:
        response = get(url)
        return response.text

def make(id):
    match id:
        case 't':
            return strftime('%Y年%m月%d日%H时',localtime())
        case 1:
            web_data = fetch_data(
                'https://voyager.jpl.nasa.gov/mission/status/',
                True
            )
            data = {}
            for id in [1,2]:
                data[id] = {}
                for section in ['km','au','kms','aus','speed','lt']:
                    data[id][section] = findall(
                        compile(f'id="voy{id}_{section}">(.*)</div>'),
                        web_data
                    )[0]
            return f"{{{{#switch:{{{{{{id|}}}}}}|1={{{{#switch:{{{{{{section|}}}}}}|km={data[1]['km']}|au={data[1]['au']}|kms={data[1]['kms']}|aus={data[1]['aus']}|speed={data[1]['speed']}|lt={data[1]['lt']}|#default=请输入正确的选项名！}}}}|2={{{{#switch:{{{{{{section|}}}}}}|km={data[2]['km']}|au={data[2]['au']}|kms={data[2]['kms']}|aus={data[2]['aus']}|speed={data[2]['speed']}|lt={data[2]['lt']}|#default=请输入正确的选项名！}}}}|#default=请输入正确的编号！}}}}"
        case 2:
            web_data = fetch_data('https://in-the-sky.org/spacecraft.php?id=6073')
            data = {}
            for section in ['Inclination','Eccentricity','RA ascending node','Argument perihelion','Mean anomaly','Orbital period','Epoch of osculation']:
                data[section] = findall(f'<td>{section}</td>\n *<td>([^<>]*)</td>',content)[0].strip()
            return f"{{{{#switch:{{{{{{section|}}}}}}|Inclination={data['Inclination']}|Eccentricity={data['Eccentricity']}|RA ascending node={data['RA ascending node']}|Argument perihelion={data['Argument']}|Mean anomaly={data['Mean anomaly']}|Orbital Period={data['Orbital Period']}|Epoch of osculation={data['Epoch of osculation']}|#default=请输入正确的选项名！}}}}"
        case _:
            return '请输入正确的AllUp编号！'

if __name__ == '__main__':
    configure_chromedriver()
    AllUp_content = f"<includeonly>{{{{#switch:{{{{{{1|}}}}}}|t={make('t')}|1={make(1)}|2={make(2)}|#default={make('default')}}}}}</includeonly><noinclude>[[Category:模板]]{{{{documentation}}}}</noinclude>"
    system(f'echo "ALLUP_CONTENT={AllUp_content}" >> $GITHUB_OUTPUT')
    print(f'==== AllUp_Content ====\n{AllUp_content}')