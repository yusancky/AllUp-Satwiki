# Copyright (c) yusancky. All rights reserved.
# Licensed under the Apache License 2.0. See License in the project root for license information.

import AllUp_utils.web
import AllUp_utils.wiki
import AllUp_utils.wikitext
from datetime import date
from re import compile, findall
from requests import RequestException
from time import localtime, strftime

SATELLITE_CODES = [
    "star",
    "ow",
    "kp",
    "stsh",
    "xw",
    "qf",
    "ynh",
    "lynk",
    "esp",
    "s1m",
    "pln",
    "iri",
    "gbl",
    "jil",
    "slog",
    "asts",
    "swa",
    "glo",
    "spr",
    "st3",
    "par",
    "gps",
    "bei",
    "oco",
    "hwk",
    "kep",
    "int",
    "ses",
]


def build_satellite_total_row_pattern():
    """Build a reusable regex pattern for Total rows on planet4589 stats pages."""
    cell_specs = [
        ("blue", True, False),
        ("red", False, False),
        ("red", False, False),
        ("red", False, False),
        ("red", False, False),
        ("blue", True, False),
        ("blue", True, False),
        ("red", False, False),
        ("red", False, False),
        ("red", False, False),
        ("blue", True, False),
        ("blue", False, False),
        ("blue", False, False),
        ("blue", False, False),
        ("blue", False, False),
        ("blue", False, False),
        ("green", False, False),
        ("green", False, False),
        ("green", False, False),
        ("green", False, True),
        ("green", False, True),
        ("green", False, True),
    ]

    cells = []
    for color, capture_value, allow_blank in cell_specs:
        value_pattern = r" *" if allow_blank else r"\d*"
        if capture_value:
            value_pattern = f"({value_pattern})"
        cells.append(rf'<TD style="color:{color}" *>{value_pattern}</TD>')

    return r"<TR><TD>Total</TD>" + "".join(cells) + r"</TR>"


SATELLITE_TOTAL_ROW_PATTERN = compile(build_satellite_total_row_pattern())


def fetch_satellite_stats_page(satellite):
    """Fetch a satellite stats page by satellite code."""
    return AllUp_utils.web.fetch_data(
        f"https://planet4589.org/space/con/{satellite}/stats.html"
    )


def extract_satellite_total_counts(web_data: str) -> tuple[str, str, str, str]:
    """Extract four key numeric counters from a planet4589 stats page."""
    dataset = findall(SATELLITE_TOTAL_ROW_PATTERN, web_data)
    if not dataset:
        raise ValueError("未找到 Total 行数据。")
    row = dataset[0]
    return tuple(row[index] for index in range(4))


def build_section_count_map(
    counts: tuple[str, str, str, str],
) -> dict[str, str]:
    """Build section-keyed mapping from four extracted satellite counters."""
    return {str(index + 1): value for index, value in enumerate(counts)}


def fetch_voyager_data():
    """[Deprecated] Fetch Voyager mission data."""
    web_data = AllUp_utils.web.fetch_data(
        "https://voyager.jpl.nasa.gov/mission/status/"
    )
    data = {"switch_key": "id"}
    for id in [str(i + 1) for i in range(2)]:
        data[id] = {"switch_key": "section"}
        for section in ["km", "au", "kms", "aus", "speed", "lt"]:
            data[id][section] = findall(
                compile(f'id="voy{id}_{section}">(.*)</div>'), web_data
            )[0]
        data[id]["#default"] = "请输入正确的选项名！"
    data["#default"] = "请输入正确的编号！"
    return AllUp_utils.wikitext.build_switch(data)


def fetch_orbital_data():
    """Fetch orbital data."""
    web_data = AllUp_utils.web.fetch_data(
        "https://in-the-sky.org/spacecraft.php?id=6073"
    )
    data = {"switch_key": "section"}
    for section in [
        "Inclination",
        "Eccentricity",
        "RA ascending node",
        "Argument perigee",
        "Mean anomaly",
        "Orbital period",
        "Epoch of osculation",
    ]:
        data[section] = findall(
            f"<td>{section}</td>\n *<td>([^<>]*)</td>", web_data
        )[0].strip()
    data["#default"] = "请输入正确的选项名！"
    return AllUp_utils.wikitext.build_switch(data)


def fetch_starlink_data():
    """Fetch Starlink mission data."""
    web_data = fetch_satellite_stats_page("star")
    data = {"switch_key": "section"}
    data.update(build_section_count_map(extract_satellite_total_counts(web_data)))
    data["#default"] = "请输入正确的选项名！"
    return AllUp_utils.wikitext.build_switch(data)


def build_tiangong_chart():
    """[Deprecated] Build Tiangong Space Station missions chart."""
    missions = []
    today = date.today()
    with open("TSS-data/TSS-data.wikitext", encoding="utf-8") as file:
        dataset = [line.strip() for line in file]
    for row in dataset:
        data = row.split(",")
        start_date = date.fromisoformat(data[2])
        end_date = (
            date.fromisoformat(data[3]) if data[3] != "future" else today
        )
        delta_days = (end_date - start_date).days
        missions.append(
            [
                data[0],
                start_date,
                delta_days,
                (
                    "#fdba74"
                    if data[1] == "main"
                    else ("#6ee7b7" if data[3] != "future" else "#fcd34d")
                ),
            ]
        )
    data_name, start_date, delta_days_with_data_color = [], [], ""
    for mission in missions:
        data_name.insert(0, mission[0])
        start_date.insert(
            0, (mission[1] - date.fromisoformat("20210429")).days
        )
        delta_days_with_data_color = (
            f'{{"value": {mission[2]}, "itemStyle": {{"color": "{mission[3]}"}} }},'
            f"{delta_days_with_data_color}"
        )
    delta_days_with_data_color = delta_days_with_data_color[:-1]
    return f"""{{{{#echarts:option={{
  "title": {{
    "text": "天宫空间站任务列表",
    "subtext": "上次更新：{date.today().year}年{date.today().month}月{date.today().day}日（{(date.today() - date.fromisoformat('20210429')).days}）"
  }},
  "tooltip": {{
    "trigger": "axis",
    "axisPointer": {{"type": "shadow"}}
  }},
  "grid": {{"left": "3%", "right": "4%", "bottom": "3%", "containLabel": true}},
  "xAxis": {{"type": "value"}},
  "yAxis": {{
    "type": "category",
    "splitLine": {{"show": false}},
    "data": {str(data_name).replace("'", '"')}
  }},
  "series": [
    {{
      "name": "发射时间",
      "type": "bar",
      "stack": "Total",
      "itemStyle": {{"borderColor": "transparent", "color": "transparent"}},
      "emphasis": {{
        "itemStyle": {{"borderColor": "transparent", "color": "transparent"}}
      }},
      "data": {start_date}
    }},
    {{
      "name": "已进行任务天数",
      "type": "bar",
      "stack": "Total",
      "label": {{"show": true, "position": "inside"}},
      "data": [
        {delta_days_with_data_color}
      ]
    }}
  ]
}}
|style=min-height:580px}}}}"""


def build_satellite_switch(satellite):
    """Build switch data for one satellite code with resilient parsing."""
    data_inner = {"switch_key": "section"}
    try:
        counts = extract_satellite_total_counts(
            fetch_satellite_stats_page(satellite)
        )
        data_inner.update(build_section_count_map(counts))
    except (RequestException, ValueError) as exception:
        for section in range(4):
            data_inner[str(section + 1)] = str(exception)
    data_inner["#default"] = "请输入正确的选项名！"
    return AllUp_utils.wikitext.build_switch(data_inner)


def fetch_satellite_data():
    """Fetch data for multiple satellites."""
    data = {"switch_key": "sat"}
    for satellite in SATELLITE_CODES:
        data[satellite] = build_satellite_switch(satellite)
    data["#default"] = "请输入正确的卫星名！"
    return AllUp_utils.wikitext.build_switch(data)


def make(id):
    """Main switch function."""
    match id:
        case "t":
            return strftime("%Y年%m月%d日%H时", localtime())
        case "1":
            return "因上游数据进行格式调整，<code><nowiki>{{AllUp|1}}</nowiki></code> 暂时停用！{{需要更新}}"
        case "2":
            return fetch_orbital_data()
        case "3":
            return fetch_starlink_data()
        case "4":
            return "天宫空间站任务列表 ECharts 的生成已迁移到 [[:Module:EChartsTSS]]，可以通过 <code><nowiki>{{#invoke:EChartsTSS|main}}</nowiki></code> 调用。AllUp 不再提供 ECharts 的生成。{{需要更新}}"
        case "5":
            return fetch_satellite_data()
        case _:
            return "请输入正确的AllUp编号！"


def build_allup_content(allup_data):
    """Build final template content for AllUp."""
    switch_content = AllUp_utils.wikitext.build_switch(allup_data)
    return (
        f"<includeonly>{switch_content}</includeonly>"
        "<noinclude>[[Category:模板]]{{documentation}}</noinclude>"
    )


if __name__ == "__main__":
    chromedriver = AllUp_utils.web.configure_chromedriver()
    allup_data = {"switch_key": "1"}
    for dataset in ["t"] + [str(i + 1) for i in range(5)] + ["#default"]:
        allup_data[dataset] = make(dataset)
    allup_content = build_allup_content(allup_data)
    AllUp_utils.wiki.push("Template:AllUp", allup_content)
