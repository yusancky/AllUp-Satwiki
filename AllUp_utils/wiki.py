# Copyright (c) yusancky. All rights reserved. 
# Licensed under the Apache License 2.0. See License in the project root for license information. 

from os import environ
from pwiki.wiki import Wiki

def PR_TEST():
    return environ['GITHUB_EVENT_NAME'] == 'pull_request'

def MAIN_REPO_BRANCH():
    return (environ['GITHUB_REF'] == 'refs/heads/main' and environ['GITHUB_REPOSITORY_OWNER'] == 'yusancky')
    
def pull(title : str,split_line = False):
    if MAIN_REPO_BRANCH() or PR_TEST():
        match title:
            case '模板:天宫空间站任务列表/echarts/data':
                return [line.replace('\n','') for line in open('TSS-data/TSS-data.wikitext')]
            case _:
                print('Unable to find test sources.')
                try:
                    wiki = Wiki('sat.huijiwiki.com')
                    return wiki.page_text(title)
                except:
                    print(f'You do not have permission to get password.\nREF: {environ["GITHUB_REF"]}\nREPO_OWNER: {environ["GITHUB_REPOSITORY_OWNER"]}')
    else:
        try:
            wiki = Wiki('sat.huijiwiki.com')
            return wiki.page_text(title)
        except:
            print(f'You do not have permission to get password.\nREF: {environ["GITHUB_REF"]}\nREPO_OWNER: {environ["GITHUB_REPOSITORY_OWNER"]}')

def push(title : str,content_id : str,content : str):
    open(f'{title}.wikitext', 'w').write(content)
    if PR_TEST():
        print(f'### {content_id}\n\n```go\n{content}\n```\n\n',file = open('PR_preview.md','a'))
