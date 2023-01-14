<!--
Copyright (c) yusancky. All rights reserved. 
Licensed under the Apache License 2.0. See License in the project root for license information. 
-->

# AllUp-Satwiki

![Python: 3.10 | 3.11 | 3.12](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-python?style=social&logo=python&logoColor=blue) ![License: Apache-2.0](https://img.shields.io/github/license/yusancky/AllUp-Satwiki?style=social)

AllUp 项目是由 [雨伞CKY](https://github.com/yusancky) 维护的、自动化爬取并集合数据以便动态更新的项目。AllUp 项目的数据将于每日 $9$ 时 $26$ 分爬取数据并修改。[^1][^2]

# 使用

下载存储库根目录下的 `fetch_make.py`，并在安装所有依赖后运行 Python 代码。

> **Note**
> 在下载根目录下的 `requirements.txt` 后，可以运行 `pip install -r requirements.txt` 安装依赖。

# 贡献

感谢您能抽出宝贵时间为 AllUp-Satwiki 项目做出贡献！

> **Note**
> AllUp-Satwiki 项目是业余项目，对任何非恶意的贡献友好。

此外，欢迎您对存储库已有内容或其他拉取请求提供建议，但请使用客观友好的方式发表评论，而不是打击贡献者的消极负面评论。如果您想加入开发团队，请联系雨伞CKY。

## 操作步骤

下文将假定您较少了解 GitHub，如果您了解 GitHub 并已有帐户，可跳过本节，开始阅读 [格式手册](#格式手册)。

> **Note**
> 您不必担心您的操作造成意外的错误，因为您的修改只在被检查并合并到主存储库后才影响模板的内容。

### GitHub 帐户

如果您需要参与贡献，需要一个 GitHub 个人帐户。如果您还没有帐户，可以前往 [GitHub 的注册页](https://github.com/signup) 注册。

> **Note**
> 注册后，您可能还需要 [验证电子邮件地址](https://docs.github.com/zh/get-started/signing-up-for-github/verifying-your-email-address)。

### 创建存储库分支

1. 点击本存储库页面右上角的「创建分支」按钮（如下图）。
  
  ![](https://docs.github.com/assets/cb-23088/images/help/repository/fork_button.png)
  
2. 在新页面内单击「创建分支」按钮（如下图）。
  
  ![](https://docs.github.com/assets/cb-49879/images/help/repository/fork-create-button.png)

### 在存储库内修改

> **Note**
> 如果您熟悉 Git 的操作，也可以使用 Git 和本地编辑器，但在这里不加赘述。

1. 打开需要修改的文件，点击「编辑文件」按钮（如下图一）。如果需要编辑多个文件，或需要修改较多内容，可以选择在 github.dev 中编辑（如下图二）。
  
  ![](https://docs.github.com/assets/cb-64898/images/help/repository/edit-file-edit-button.png)

  ![](https://docs.github.com/assets/cb-118903/images/help/repository/edit-file-edit-dropdown.png)

2. 在完成修改后，在填写提交标题后选择「新建分支」选项（如下图），然后点击下方的「提议文件更改」按钮。
  
  ![](https://docs.github.com/assets/cb-32137/images/help/repository/choose-commit-branch.png)

  如果您正在使用 github.dev 编辑，请前往 [使用源控制](https://docs.github.com/zh/codespaces/the-githubdev-web-based-editor#using-source-control) 查看提交步骤。

### 创建拉取请求

请前往 [创建拉取请求 - GitHub Docs](https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) 查看相关内容。

## 格式手册

### Markdown

Markdown 内容标准基本与 [Copywriting - 中文文案排版指北（简体中文版）](https://mazhuang.org/wiki/chinese-copywriting-guidelines/) 达成共识，但仍有一定不同（见脚注）。[^3]

### Python

- 代码缩进应使用 $4$ 个半角空格。
- 代码间应有合理的空行，但不应出现超过一个的连续空行。
- `,` 两侧不应有空格，`=` 两侧应有空格。
- 代码中的字符串应尽可能多使用 `'`。
- 对函数的注释，应当在函数内首先按 [Markdown 格式标准](#Markdown) 用跨行的三引号字符串写出，并尽可能不单独解释参数。如下是示例。
  
  ```python
  def calc(a):
      '''
      计算边长为 a 的正方形的周长。
      '''
      return 4 * a
  ```

### 拉取请求信息

不对拉取请求格式进行强制要求，但建议使用英文标题，并使用 `resolved` 等词链接对应议题。

### 注

对于不明确的格式要求，请以已有内容为准。

[^1]: 时间为北京时间。

[^2]: 定时修改基于 GitHub Action 的 `schedule` 事件。但 `schedule` 事件在 Actions 工作流运行期间负载过高时可能会延迟。据以往经历，一般延迟在 $75$ 分钟左右。

[^3]: 对于数字，请尽量使用 $\TeX$ 公式。对于「争议」部分，要求链接之间增加空格、简体中文使用直角引号。特别地，数字与单位间是否需要空格，在阿拉伯数字与计量单位字母符号间应插入一个空格（例：$1 m$、$100 kg$）。