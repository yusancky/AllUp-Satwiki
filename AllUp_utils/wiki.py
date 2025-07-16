# Copyright (c) yusancky. All rights reserved.
# Licensed under the Apache License 2.0. See License in the project root for license information.

from os import environ
from pwiki.gquery import revisions
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


def build_wikitext_filename(s):
    last_colon_index = s.rfind(":")
    if last_colon_index != -1:
        s = s[last_colon_index + 1 :]
    return s.replace("/", "--")


def push(title: str, content: str):
    with open(
        f"{build_wikitext_filename(title)}.wikitext", "w+", encoding="utf-8"
    ) as f:
        f.write(content)
    with open("preview.md", "w+") as f:
        f.write(
            f"## Preview\n\nThe workflow builds content as shown below. \n\n```go\n{content}\n```"
        )
    if MAIN_REPO_BRANCH or TEST_DISPATCH:
        wiki.edit(title, content, "Edit via AllUp-Satwiki")


def get_last_revision(title: str):
    if MAIN_REPO_BRANCH or TEST_DISPATCH or TEST_PR:
        return next(revisions(wiki, title))[0].revid
    else:
        return -1
