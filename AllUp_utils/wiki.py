# Copyright (c) yusancky. All rights reserved. 
# Licensed under the Apache License 2.0. See License in the project root for license information. 

from os import environ
from pwiki.wiki import Wiki

def PR_TEST():
    return environ['GITHUB_EVENT_NAME'] == 'pull_request'

def MAIN_REPO_BRANCH():
    return (environ['GITHUB_REF'] == 'refs/heads/main' and environ['GITHUB_REPOSITORY_OWNER'] == 'yusancky')

# Subclass Wiki to inject X-authkey header prior to first request
class AuthWiki(Wiki):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client.headers["X-authkey"] = environ['X_AUTHKEY']

def pull(title: str, split_line=False):
    # Use AuthWiki instead of Wiki
    wiki = AuthWiki('sat.huijiwiki.com', '雨伞CKY', environ['BOT_PASSWORD'])
    return wiki.page_text(title)

def push(title: str, content_id: str, content: str):
    open(f'{title}.wikitext', 'w').write(content)
    if PR_TEST():
        print(f'### {content_id}\n\n```go\n{content}\n```\n\n', file=open('PR_preview.md', 'a'))
