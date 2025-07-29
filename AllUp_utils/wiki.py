# Copyright (c) yusancky. All rights reserved.
# Licensed under the Apache License 2.0. See License in the project root for license information.

from os import environ
from pwiki.gquery import GQuery
from pwiki.wiki import Wiki
import requests
from unittest.mock import patch

try:
    MAIN_REPO_BRANCH = (
        environ["GITHUB_REPOSITORY_OWNER"] == "yusancky"
        and environ["GITHUB_REF"] == "refs/heads/main"
    )
    TEST_DISPATCH = (
        environ["GITHUB_REPOSITORY_OWNER"] == "yusancky"
        and environ["GITHUB_EVENT_NAME"] == "workflow_dispatch"
    )
    TEST_PR = environ["GITHUB_EVENT_NAME"] == "pull_request"
except Exception:
    MAIN_REPO_BRANCH, TEST_DISPATCH, TEST_PR = False, False, False


def create_wiki():
    original_session_init = requests.Session.__init__
    def patched_session_init(self, *args, **kwargs):
        original_session_init(self, *args, **kwargs)
        self.headers["X-authkey"] = environ["X_AUTHKEY"]
    with patch("requests.Session.__init__", new=patched_session_init):
        return Wiki("sat.huijiwiki.com", "雨伞CKY", environ["BOT_PASSWORD"])


if MAIN_REPO_BRANCH or TEST_DISPATCH or TEST_PR:
    wiki = create_wiki()


def pull(title: str, split_line=False):
    if MAIN_REPO_BRANCH or TEST_DISPATCH or TEST_PR:
        return wiki.page_text(title)
    else:
        return ""


def push(title: str, content: str):
    last_colon_index = title.rfind(":")
    wikitext_filename = (
        title[last_colon_index + 1 :] if last_colon_index != -1 else title
    ).replace("/", "--") + ".wikitext"
    with open(wikitext_filename, "w+", encoding="utf-8") as f:
        f.write(content)
    with open("preview.md", "w+") as f:
        f.write(
            f"## Preview\n\nThe workflow builds content as shown below. \n\n```go\n{content}\n```"
        )
    if MAIN_REPO_BRANCH or TEST_DISPATCH:
        wiki.edit(title, content, "Edit via AllUp-Satwiki")
