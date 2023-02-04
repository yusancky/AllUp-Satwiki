# Copyright (c) yusancky. All rights reserved. 
# Licensed under the Apache License 2.0. See License in the project root for license information. 

from os import environ
from pwiki.wiki import Wiki

wiki= Wiki('sat.huijiwiki.com','雨伞CKY',environ['SATWIKI_PASSWORD'])
wiki.edit('模板:AllUp',environ['ALLUP_CONTENT'],'Edit via AllUp-Satwiki')