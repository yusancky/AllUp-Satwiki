# Copyright (c) yusancky. All rights reserved. 
# Licensed under the Apache License 2.0. See License in the project root for license information. 

from os import environ
import requests
from pwiki.wiki import Wiki

def PR_TEST():
    return environ['GITHUB_EVENT_NAME'] == 'pull_request'

def MAIN_REPO_BRANCH():
    return (environ['GITHUB_REF'] == 'refs/heads/main' and environ['GITHUB_REPOSITORY_OWNER'] == 'yusancky')

# Monkeypatch requests.Session to always include X-authkey
_original_session_init = requests.Session.__init__

def _patched_session_init(self, *args, **kwargs):
    _original_session_init(self, *args, **kwargs)
    self.headers["X-authkey"] = environ['X_AUTHKEY']

requests.Session.__init__ = _patched_session_init

def pull(title : str,split_line = False):
    wiki = Wiki('sat.huijiwiki.com', '雨伞CKY', environ['BOT_PASSWORD'])
    return wiki.page_text(title)

def push(title : str,content_id : str,content : str):
    open(f'{title}.wikitext', 'w').write(content)
    if PR_TEST():
        print(f'### {content_id}\n\n```go\n{content}\n```\n\n',file = open('PR_preview.md','a'))
