# AllUp-Satwiki

![Python: 3.10 | 3.11 | 3.12](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-python?style=social&logo=python&logoColor=blue) ![License: Apache-2.0](https://img.shields.io/github/license/yusancky/AllUp-Satwiki?style=social)

AllUp 项目是由 [雨伞CKY](https://github.com/yusancky) 维护的、自动化爬取并集合数据以便动态更新的项目。AllUp 项目的数据将于每日 $9$ 时 $26$ 分爬取数据并修改。[^1][^2]

# 使用

## 在本地使用

下载存储库根目录下的 `fetch_make.py`，并在安装所有依赖后运行 Python 代码。

> **Note**
> 
> 在下载根目录下的 `requirements.txt` 后，可以运行 `pip install -r requirements.txt` 安装依赖。

## 在 GitHub Actions 工作流中使用

在设置存储库机密后，即可运行工作流。

# 贡献

请前往 [贡献文档](/.github/CONTRIBUTING.md) 查看贡献相关内容。

[^1]: 时间为北京时间。

[^2]: 定时修改基于 GitHub Action 的 `schedule` 事件。但 `schedule` 事件在 Actions 工作流运行期间负载过高时可能会延迟。据以往经历，一般延迟在 75 分钟左右。