# Copyright (c) yusancky. All rights reserved. 
# Licensed under the Apache License 2.0. See License in the project root for license information. 

import AllUp_utils.wiki

if __name__ == '__main__':
    AllUp_utils.wiki.push(open('AllUp.wikitext','r').read())
