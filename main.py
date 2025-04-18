# Copyright (c) yusancky. All rights reserved. 
# Licensed under the Apache License 2.0. See License in the project root for license information. 

import AllUp_utils.wiki
import AllUp_utils.web
import AllUp_utils.wikitext
from datetime import date
from re import compile, findall
from time import localtime, strftime


def fetch_voyager_data():
  """Fetch Voyager mission data."""
  web_data = AllUp_utils.web.fetch_data('https://voyager.jpl.nasa.gov/mission/status/')
  data = {'switch_key': 'id'}
  for id in [str(i + 1) for i in range(2)]:
    data[id] = {'switch_key': 'section'}
    for section in ['km', 'au', 'kms', 'aus', 'speed', 'lt']:
      data[id][section] = findall(
        compile(f'id="voy{id}_{section}">(.*)</div>'),
        web_data
      )[0]
    data[id]['#default'] = '请输入正确的选项名！'
  data['#default'] = '请输入正确的编号！'
  return AllUp_utils.wikitext.build_switch(data)


def fetch_orbital_data():
  """Fetch orbital data."""
  web_data = AllUp_utils.web.fetch_data('https://in-the-sky.org/spacecraft.php?id=6073')
  data = {'switch_key': 'section'}
  for section in ['Inclination', 'Eccentricity', 'RA ascending node', 'Argument perigee', 'Mean anomaly', 'Orbital period', 'Epoch of osculation']:
    data[section] = findall(f'<td>{section}</td>\n *<td>([^<>]*)</td>', web_data)[0].strip()
  data['#default'] = '请输入正确的选项名！'
  return AllUp_utils.wikitext.build_switch(data)


def fetch_starlink_data():
  """Fetch Starlink mission data."""
  web_data = AllUp_utils.web.fetch_data('https://planet4589.org/space/con/star/stats.html')
  data = {'switch_key': 'section'}
  dataset = findall(r'<TR><TD>Total</TD><TD style="color:blue" *>(\d*)</TD><TD style="color:red" *>\d*</TD><TD style="color:red" *>\d*</TD><TD style="color:red" *>\d*</TD><TD style="color:red" *>\d*</TD></TR>', web_data)
  for section in range(4):
    data[str(section + 1)] = dataset[0][section]
  data['#default'] = '请输入正确的选项名！'
  return AllUp_utils.wikitext.build_switch(data)


def build_tiangong_chart():
  """Build Tiangong missions chart."""
  missions = []
  today = date.today()
  dataset = [line.strip() for line in open('TSS-data/TSS-data.wikitext')]

  for row in dataset:
    data = row.split(',')
    start_date = date.fromisoformat(data[2])
    end_date = date.fromisoformat(data[3]) if data[3] != 'future' else today
    delta_days = (end_date - start_date).days
    missions.append([
      data[0],
      start_date,
      delta_days,
      '#fdba74' if data[1] == 'main' else ('#6ee7b7' if data[3] != 'future' else '#fcd34d')
    ])

  data_name = [mission[0] for mission in missions]
  start_date = [(mission[1] - date.fromisoformat('20210429')).days for mission in missions]
  delta_days_with_data_color = [
    {"value": mission[2], "itemStyle": {"color": mission[3]}} for mission in missions
  ]

  return f'''{{{{#echarts:option={{
"title": {{
  "text": "天宫空间站任务列表",
  "subtext": "上次更新：{today.year}年{today.month}月{today.day}日（{(today - date.fromisoformat('20210429')).days}天）"
}},
"tooltip": {{
  "trigger": "axis",
  "axisPointer": {{
    "type": "shadow"
  }}
}},
"grid": {{
  "left": "3%",
  "right": "4%",
  "bottom": "3%",
  "containLabel": true
}},
"xAxis": {{
  "type": "value"
}},
"yAxis": {{
  "type": "category",
  "splitLine": {{
    "show": false
  }},
  "data": {data_name}
}},
"series": [
  {{
    "name": "发射时间",
    "type": "bar",
    "stack": "Total",
    "itemStyle": {{
      "borderColor": "transparent",
      "color": "transparent"
    }},
    "emphasis": {{
      "itemStyle": {{
        "borderColor": "transparent",
        "color": "transparent"
      }}
    }},
    "data": {start_date}
  }},
  {{
    "name": "已进行任务天数",
    "type": "bar",
    "stack": "Total",
    "label": {{
      "show": true,
      "position": "inside"
    }},
    "data": {delta_days_with_data_color}
  }}
]
}}}}}}'''


def make(id):
  """Main switch function."""
  match id:
    case 't':
      return strftime('%Y年%m月%d日%H时', localtime())
    case '1':
      return fetch_voyager_data()
    case '2':
      return fetch_orbital_data()
    case '3':
      return fetch_starlink_data()
    case '4':
      return build_tiangong_chart()
    case _:
      return '请输入正确的AllUp编号！'


if __name__ == '__main__':
  chromedriver = AllUp_utils.web.configure_chromedriver()
  AllUp_data = {'switch_key': '1'}
  for dataset in ['t'] + [str(i + 1) for i in range(5)] + ['#default']:
    AllUp_data[dataset] = make(dataset)
  AllUp_content = f'<includeonly>{AllUp_utils.wikitext.build_switch(AllUp_data)}</includeonly><noinclude>[[Category:模板]]{{{{documentation}}}}</noinclude>'
  AllUp_utils.wiki.push('AllUp', 'MAIN', AllUp_content)