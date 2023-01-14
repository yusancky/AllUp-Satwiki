<!--
Copyright (c) yusancky. All rights reserved. 
Licensed under the Apache License 2.0. See License in the project root for license information. 
-->

# AllUp-Satwiki

![Python: 3.10 | 3.11 | 3.12](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-python?style=social&logo=python&logoColor=blue) ![License: Apache-2.0](https://img.shields.io/github/license/yusancky/AllUp-Satwiki?style=social)

AllUp 项目是由 [雨伞CKY](https://github.com/yusancky) 维护的、自动化爬取并集合数据以便动态更新的项目。AllUp 项目的数据将于每日 9 时 26 分爬取数据并修改。[^1][^2]

# 使用

下载仓库根目录下的 `fetch_make.py`，并在安装所有依赖（可在下载根目录下的 `requirements.txt` 后使用 `pip install -r requirements.txt` 批量安装）后运行 Python 代码。

# 脚注

[^1]: 时间为北京时间。

[^2]: 定时修改基于 GitHub Action 的 `schedule` 事件。但 `schedule` 事件在 Actions 工作流运行期间负载过高时可能会延迟。据以往经历，一般延迟在 75 分钟左右。