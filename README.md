# AllUp-Satwiki

![Python: 3.12 | 3.13](https://img.shields.io/badge/Python-3.12%20%7C%203.13-python?style=social&logo=python&logoColor=blue) ![License: Apache-2.0](https://img.shields.io/github/license/yusancky/AllUp-Satwiki?style=social)

AllUp 项目是由 [雨伞CKY](https://github.com/yusancky) 维护的、自动化爬取并集合数据以便动态更新的项目。AllUp 项目的数据将于每日北京时间 9 时 26 分爬取数据并修改。[^1]

![Contributions in the Last 30 Days](https://repobeats.axiom.co/api/embed/3c013245586cfcc386dd553450db134d7617991c.svg)

# 使用

克隆或下载本存储库后，（切换到本项目根目录后）使用 `pip install -r requirements.txt` 安装所有依赖。之后，你可以分别通过运行 `main.py` 和 `TSS/main.py` 生成主模板内容、天宫空间站任务列表的 Apache ECharts 模板内容。生成的内容不会主动输出。

# 贡献

请前往 [贡献文档](/.github/CONTRIBUTING.md) 查看贡献相关内容。

[^1]: 定时进行任务基于 GitHub Action 的 `schedule` 事件。但 `schedule` 事件在 Actions 工作流运行期间负载过高时可能会延迟。据以往经历，一般延迟在 30 分钟至 45 分钟。