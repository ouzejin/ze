# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
# template = {
#     "name": "Galileo",
#     "type": "local",
#     "path": "../Galileo"
# }

template="Kepler"

enable_jsdelivr = {
    "enabled": True,
    "repo": "ouzejin/ze@gh-pages"
}

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "0j0KcckWXNcj4LM9RWVh1nKN-gzGzoHsz",
    "appKey": "TGMR5Eo0w2lsuE1wyO7p5cyv",
    "visitor": True,
    "recordIP": True,
    "placeholder": "略懂"
}


# 站点设置
site_name = "ze"
site_logo = "${static_prefix}avatar.png"
site_build_date = "2020-12-31T15:00+00:00"
author = "ze"
email = "2826708201@qq.com"
author_homepage = "https://blog.ze.online"
description = "The resolution will not change"
key_words = ['Maverick', 'ZE', 'Galileo', 'wiki']
language = 'zh-CN'
external_links = [
    {
        "name": "Blog",
        "url": "https://blog.ze.online",
        "brief": "🏄‍ Go My Own Way."
    },
    {
        "name": "Photos",
        "url": "https://photos.ze.online",
        "brief": "相册。"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/ouzejin",
        "brief": "GitHub。"
    },
    {
        "name": "Twitter",
        "url": "https://twitter.com/ouzejin",
        "brief": "Twitter。"
    }
]
nav = [
    {
        "name": "Home",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "Archives",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "About",
        "url": "${site_prefix}About/",
        "target": "_self"
    },
    {
        "name": "My Project",
        "url": "${site_prefix}My Project/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/ouzejin",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/ouzejin",
        "icon": "gi gi-github"
    }
   
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="icon" href="https://cdn.jsdelivr.net/gh/lifealsoisgg/Wiki@gh-pages/avatar.png" type="images/x-ico" />
'''

footer_addon = r'''
<p><a href="http://www.beian.miit.gov.cn">粤ICP备19126168号</a>
'''

body_addon = ''
