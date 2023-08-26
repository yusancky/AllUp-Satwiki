# Copyright (c) yusancky. All rights reserved. 
# Licensed under the Apache License 2.0. See License in the project root for license information. 

import AllUp_utils.push
import csv
from datetime import date

missions = []

today = date.today()

with open('TSS-data.csv',encoding = 'utf-8',newline = '') as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        start_date = date.fromisoformat(row['发射时间'])
        end_date = date.fromisoformat(row['再入时间']) if row['再入时间'] != 'future' else date.today()
        delta_days = (end_date - start_date).days
        missions.append([
            row['中文名称'],
            start_date,
            delta_days,
            '#fdba74' if row['类型'] == 'main' else ('#6ee7b7' if row['再入时间'] != 'future' else '#fcd34d')
        ])

data_name,start_date,delta_days_with_data_color = [],[],''

for mission in missions:
    data_name.insert(0,mission[0])
    start_date.insert(0,(mission[1] - date.fromisoformat('20210429')).days)
    delta_days_with_data_color = f'{{"value": {mission[2]}, "itemStyle": {{"color": "{mission[3]}"}} }},{delta_days_with_data_color}'

delta_days_with_data_color = delta_days_with_data_color[:-1]

output_content = f'''{{{{#echarts:option={{
  "title": {{
    "text": "天宫空间站任务列表",
    "subtext": "上次更新：{date.today().year}年{date.today().month}月{date.today().day}日（{(date.today() - date.fromisoformat('20210429')).days}）"
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
    "data": {str(data_name).replace("'",'"')}
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
      "data": [
        {delta_days_with_data_color}
      ]
    }}
  ]
}}
|style=min-height:380px}}}}'''

AllUp_utils.push.push('模板:天宫空间站任务列表/echarts','TSS',output_content)