# Copyright (c) yusancky. All rights reserved. 
# Licensed under the Apache License 2.0. See License in the project root for license information. 

import AllUp-utils.web
import AllUp-utils.wikitext
from os import system
from re import compile,findall
from time import localtime,strftime

def make(id):
    match id:
        case 't':
            return strftime('%Y年%m月%d日%H时',localtime())
        case '1':
            web_data = AllUp-utils.web.fetch_data(
                'https://voyager.jpl.nasa.gov/mission/status/',
                chromedriver
            )
            data = {'switch_key': 'id'}
            for id in [str(i + 1) for i in range(2)]:
                data[id] = {'switch_key': 'section'}
                for section in ['km','au','kms','aus','speed','lt']:
                    data[id][section] = findall(
                        compile(f'id="voy{id}_{section}">(.*)</div>'),
                        web_data
                    )[0]
                data[id]['#default'] = '请输入正确的选项名！'
            data['#default'] = '请输入正确的编号！'
            return AllUp-utils.wikitext.switch(data)
        case '2':
            web_data = AllUp-utils.web.fetch_data('https://in-the-sky.org/spacecraft.php?id=6073')
            data = {'switch_key': 'section'}
            for section in ['Inclination','Eccentricity','RA ascending node','Argument perihelion','Mean anomaly','Orbital period','Epoch of osculation']:
                data[section] = findall(f'<td>{section}</td>\n *<td>([^<>]*)</td>',web_data)[0].strip()
            data['#default'] = '请输入正确的选项名！'
            return AllUp-utils.wikitext.switch(data)
        case _:
            return '请输入正确的AllUp编号！'

if __name__ == '__main__':
    chromedriver = AllUp-utils.web.configure_chromedriver()
    AllUp_data = {'switch_key': '1'}
    for dataset in ['t'] + [str(i + 1) for i in range(2)] + ['#default']:
        AllUp_data[dataset] = make(dataset)
    AllUp_content = f"<includeonly>{AllUp-utils.wikitext.switch(AllUp_data)}</includeonly><noinclude>[[Category:模板]]{{{{documentation}}}}</noinclude>"
    system(f'echo "ALLUP_CONTENT={AllUp_content}" >> $GITHUB_OUTPUT')
    print(f'==== AllUp_Content ====\n{AllUp_content}')