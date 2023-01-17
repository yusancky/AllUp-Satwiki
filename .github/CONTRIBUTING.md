感谢您能抽出宝贵时间为本项目做出贡献！

# 友好与善意

本项目是业余项目，对任何非恶意的贡献友好。

欢迎对存储库已有内容或未合并拉取请求内容提供建议，但请注意使用客观友好的方式发表评论，而不是消极负面评论。

> **Warning**
> 开发团队有权折叠或删除恶意的评论。

# 贡献步骤

> **Note**
> 
> 下文假定您较少了解 GitHub。
> 
> 如果您了解 GitHub 并已有帐户，可跳过本节，开始阅读 [格式手册](#格式手册)。

> **Note**
> 
> 您不必担心您的操作造成意外的错误，因为您的修改只会在被开发团队合并后才影响模板的内容。

## GitHub 帐户

您需要使用一个 GitHub 个人帐户进行贡献。如果您还没有帐户，可以前往 [GitHub 个人帐户注册页](https://github.com/signup) 注册。

> **Note**
> 您可能还需根据实情 [验证电子邮件地址](https://docs.github.com/zh/get-started/signing-up-for-github/verifying-your-email-address)。

## 存储库分支

1. 点击本存储库页面右上角的「创建分支」按钮（如下图）。
  
  ![](https://docs.github.com/assets/cb-23088/images/help/repository/fork_button.png)
  
2. 在新页面内单击「创建分支」按钮（如下图）。
  
  ![](https://docs.github.com/assets/cb-49879/images/help/repository/fork-create-button.png)

## 修改

> **Note**
> 
> 如果您熟悉 Git 的操作，也可以使用 Git 和本地编辑器，但在这里不加赘述。

1. 打开需要修改的文件，点击「编辑文件」按钮（如下图一）。如果需要编辑多个文件，或需要修改较多内容，可以选择在 github.dev 中编辑（如下图二）。
  
  ![](https://docs.github.com/assets/cb-64898/images/help/repository/edit-file-edit-button.png)

  ![](https://docs.github.com/assets/cb-118903/images/help/repository/edit-file-edit-dropdown.png)

2. 在完成修改后，在填写提交标题后选择「新建分支」选项（如下图），然后点击下方的「提议文件更改」按钮。
  
  ![](https://docs.github.com/assets/cb-32137/images/help/repository/choose-commit-branch.png)

  如果您正在使用 github.dev 编辑，请前往 [使用源控制](https://docs.github.com/zh/codespaces/the-githubdev-web-based-editor#using-source-control) 查看提交步骤。

## 拉取请求

请前往 [创建拉取请求 - GitHub Docs](https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) 查看相关内容。

# 格式手册

## Markdown

Markdown 内容标准基本与 [Copywriting - 中文文案排版指北（简体中文版）](https://mazhuang.org/wiki/chinese-copywriting-guidelines/) 达成共识，但仍有一定不同。

> **Note**
> 
> 以下是格式上的不同：
> 1. 对于数字，请尽量使用 TeX 公式。
> 2. 在阿拉伯数字与计量单位字母符号间应插入一个空格（例：$1 m$、$100 kg$）。
> 3. 对于文档中「争议」部分，要求链接之间增加空格、简体中文使用直格式角引号。

## Python

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

## 拉取请求信息

不对拉取请求格式进行强制要求，但建议使用英文标题，并使用 `resolved` 等词链接对应议题。

## 注

对仍不明确的格式要求，请以已有内容格式为准。

# 开发团队

如果您想加入开发团队，请联系雨伞CKY。