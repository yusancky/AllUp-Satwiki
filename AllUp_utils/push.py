# Copyright (c) yusancky. All rights reserved. 
# Licensed under the Apache License 2.0. See License in the project root for license information. 

from os import environ
from pwiki.wiki import Wiki

def push(title : str,content_id : str,content : str):
    print(
        f'### {content_id}\n\n```go\n{content}\n```\n\n',
        file = open('../PR_preview.md','a')
    )
    try:
        if environ['GITHUB_REF'] == 'refs/heads/main' and environ['GITHUB_REPOSITORY_OWNER'] == 'yusancky':
            wiki = Wiki('sat.huijiwiki.com','雨伞CKY',environ['SATWIKI_PASSWORD'])
            wiki.edit(title,content,'Edit via AllUp-Satwiki')
        else:
            print(f'You do not have permission to get password.\nREF: {environ["GITHUB_REF"]}\nREPO_OWNER: {environ["GITHUB_REPOSITORY_OWNER"]}')
    except:
        pass