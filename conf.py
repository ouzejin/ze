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
    "repo": "lifealsoisgg/Wiki@gh-pages"
}


# 站点设置
site_name = "LifeAlsoIsGG-Wiki"
site_logo = "${static_prefix}avatar.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "LifeAlsoIsGG"
email = "1138312802@qq.com"
author_homepage = "https://blog.lifeisgg.online"
description = "Do not go gentle in that good night"
key_words = ['Maverick', 'LifeAlsoIsGG', 'Galileo', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "Blog",
        "url": "https://blog.lifeisgg.online",
        "brief": "🏄‍ Go My Own Way."
    },
    {
        "name": "Photos",
        "url": "https://photo.lifeisgg.online",
        "brief": "相册。"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/LifeAlsoIsGG",
        "brief": "GitHub。"
    },
    {
        "name": "Twitter",
        "url": "https://twitter.com/LifeAlsoIsGG",
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
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/LifeAlsoIsGG",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/LifeAlsoIsGG",
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
