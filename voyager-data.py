from mwclient import Site
from re import compile, findall
from selenium import webdriver
from time import localtime, strftime

URL = "https://voyager.jpl.nasa.gov/mission/status/"

browser = webdriver.Safari()
browser.get(URL)

page_source = browser.page_source

ids = [1, 2]
sections = ["km", "au", "kms", "aus", "speed", "lt"]

voy_data = "<includenly>{{ #switch: {{{id}}} | t = time | 1 = {{ #switch: {{{section}}} | km = data1 | au = data2 | kms = data3 | aus = data4 | speed = data5 | lt = data6 | #default = 请输入正确的选项名！}} | 2 = {{ #switch: {{{section}}} | km = data7 | au = data8 | kms = data9 | aus = data10 | speed = data11 | lt = data12 | #default = 请输入正确的选项名！}} | #default = 请输入正确的编号！ }}</includeonly><noinclude>[[Category:模板]]{{documentation}}</noinclude>"
voy_data = voy_data.replace("time", strftime("%Y年%m月%d日%H时", localtime()))

cnt = 0

for id in ids:
    for section in sections:
        cnt += 1
        data_re = compile(f'id="voy{id}_{section}">(.*)</div>')
        findall_res = findall(data_re, page_source)
        print(findall_res[0])
        voy_data = voy_data.replace(f"data{cnt} ", f"{findall_res[0]} ")
        print(voy_data)

site = Site("sat.huijiwiki.com", scheme="http")
site = Site(
    "sat.huijiwiki.com",
    clients_useragent="Voyager-data/1.1.1 (umbrellacky@qq.com)",
)
site.login("雨伞CKY", SATWIKI_PASSWORD)
page = site.pages["模板:旅行者距离数据"]
page.save(
    voy_data,
    "Edit via Voyager Data/1.1.1 (umbrellacky@qq.com) powered by GitHub Actions",
)