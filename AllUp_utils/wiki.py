# Copyright (c) yusancky. All rights reserved.
# Licensed under the Apache License 2.0. See License in the project root for license information.

from os import environ
from pwiki.wiki import Wiki
import requests

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

_original_session_init = requests.Session.__init__


def _patched_session_init(self, *args, **kwargs):
    _original_session_init(self, *args, **kwargs)
    self.headers["X-authkey"] = environ["X_AUTHKEY"]


requests.Session.__init__ = _patched_session_init

if MAIN_REPO_BRANCH or TEST_DISPATCH or TEST_PR:
    wiki = Wiki("sat.huijiwiki.com", "雨伞CKY", environ["BOT_PASSWORD"])


def pull(title: str, split_line=False):
    if MAIN_REPO_BRANCH or TEST_DISPATCH or TEST_PR:
        return wiki.page_text(title)
    else:
        return ""


def extract_after_last_colon(s):
    last_colon_index = s.rfind(":")
    return s[last_colon_index + 1 :] if last_colon_index != -1 else s


def push(title: str, content_id: str, content: str):
    with open(
        f"{extract_after_last_colon(title)}.wikitext", "w", encoding="utf-8"
    ) as f:
        f.write(content)
    if MAIN_REPO_BRANCH or TEST_DISPATCH:
        wiki.edit(title, content, "Edit via AllUp-Satwiki")
    if TEST_PR:
        print(
            f"### {content_id}\n\n```go\n{content}\n```\n\n",
            file=open("PR_preview.md", "a"),
        )
