---
layout: post
title: Docker deployment
slug: Dock-deployment
date: 2020/05/31 15:39:08
status: publish
author: LifeAlsoIsGG
categories: 
  - Linux
  - Docker
tags: 
  - Linux
  - Docker
---

环境

CentOs 7

# 1.卸载旧版本

```shell
sudo yum remove docker \
 docker-client \
 docker-client-latest \
 docker-common \
 docker-latest \
 docker-latest-logrotate \
 docker-logrotate \
 docker-engine
```



# 参考Reference

[CentOs Docker Install](https://www.runoob.com/docker/centos-docker-install.html)