# Copyright (c) yusancky. All rights reserved. 
# Licensed under the Apache License 2.0. See License in the project root for license information. 

from os import environ
from pwiki.wiki import Wiki
from re import compile,findall
from selenium import webdriver
from time import localtime,strftime

chrome_options = webdriver.ChromeOptions()
chrome_options.headless = True
chrome = webdriver.Chrome("/usr/local/share/chrome_driver",options = chrome_options)

chrome.get("https://voyager.jpl.nasa.gov/mission/status/")
page_source = chrome.page_source

sections = ["km","au","kms","aus","speed","lt"]
AllUp_content = "<includeonly>{{ #switch: {{{1|}}} | 1={{ #switch: {{{id}}} | t = time | 1 = {{ #switch: {{{section}}} | km = data1 | au = data2 | kms = data3 | aus = data4 | speed = data5 | lt = data6 | #default = 请输入正确的选项名！}} | 2 = {{ #switch: {{{section}}} | km = data7 | au = data8 | kms = data9 | aus = data10 | speed = data11 | lt = data12 | #default = 请输入正确的选项名！}} | #default = 请输入正确的编号！ }} | #default = 请输入正确的 AllUp 编号！}}</includeonly><noinclude>[[Category:模板]]{{documentation}}</noinclude>".replace("time",strftime("%Y年%m月%d日%H时",localtime()))
cnt = 0
for id in [1,2]:
    for section in sections:
        cnt += 1
        data_re = compile(f'id="voy{id}_{section}">(.*)</div>')
        findall_res = findall(data_re,page_source)
        AllUp_content = AllUp_content.replace(f"data{cnt} ",f"{findall_res[0]} ")

wiki = Wiki("sat.huijiwiki.com","雨伞CKY",environ["SATWIKI_PASSWORD"])
wiki.edit("模板:AllUp",AllUp_content,"Edit via AllUp-Satwiki")