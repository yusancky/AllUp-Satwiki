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

def generate_switch(data_map):
    result = '{{#switch:{{{' + data_map['switch_key'] + '|}}}'
    for data_key,data_value in data_map.items():
        if data_key == 'switch_key':
            continue
        if isinstance(data_value,str):
            result += f'|{data_key}={data_value}'
        elif isinstance(data_value,dict):
            result += f'|{data_key}={generate_switch(data_value)}'
        else:
            raise TypeError(f"an integer or a dictionary is required, not '{type(data_value)}'")
    return result

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
            data['switch_key'] = 'id'
            for id in [str(i + 1) for i in range(2)]:
                data[id] = {}
                data[id]['switch_key'] = 'section'
                for section in ['km','au','kms','aus','speed','lt']:
                    data[id][section] = findall(
                        compile(f'id="voy{id}_{section}">(.*)</div>'),
                        web_data
                    )[0]
                data[id]['#default'] = '请输入正确的选项名！'
            data['#default'] = '请输入正确的编号！'
            return generate_switch(data)
        case 2:
            web_data = fetch_data('https://in-the-sky.org/spacecraft.php?id=6073')
            data = {}
            data['switch_key'] = 'section'
            for section in ['Inclination','Eccentricity','RA ascending node','Argument perihelion','Mean anomaly','Orbital period','Epoch of osculation']:
                data[section] = findall(f'<td>{section}</td>\n *<td>([^<>]*)</td>',web_data)[0].strip()
            data['#default'] = '请输入正确的选项名！'
            return generate_switch(data)
        case _:
            return '请输入正确的AllUp编号！'

if __name__ == '__main__':
    configure_chromedriver()
    AllUp_content = f"<includeonly>{{{{#switch:{{{{{{1|}}}}}}|t={make('t')}|1={make(1)}|2={make(2)}|#default={make('default')}}}}}</includeonly><noinclude>[[Category:模板]]{{{{documentation}}}}</noinclude>"
    system(f'echo "ALLUP_CONTENT={AllUp_content}" >> $GITHUB_OUTPUT')
    print(f'==== AllUp_Content ====\n{AllUp_content}')