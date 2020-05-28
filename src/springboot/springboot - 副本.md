---
layout: post
title: import excel to mysql2
slug: import-excel-to-mysql2
date: 2020-05-28 12:35
status: publish
author: LifeAlsoIsGG
categories: 
  - Springboot
tags: 
  - Springboot
excerpt: import excel to mysql in springboot
---



Github:[import excel to mysql](https://github.com/LifeAlsoIsGG/MyPractice-Neusoft/tree/master/import-Excel)



## 1.准备

### 1.1添加所需要的的依赖





### 1.2根据excel的字段添加对应字段的表

excel表



mysql表





### 1.3在IDEA使用easycode插件对此表使用生成MVC

目录图如下

 

## 2.核心代码

### 2.1创建能处理excel转换为`List<Object>`的方法

创建`ExcelForList`类并创建`ExcelForList`方法用于处理excel表各个记录并返回





### 2.1创建接口

> - 获取到文件
> - 调用上述方法获取到List<Object>
> - 循环List<Object>转换为一个个course对象再插入到数据库中







## 3.Console

### 3.1POSTMAN

调用接口http://localhost:8886/course/import

method="POST"

> - HEADERS中添加KEY:`Content-Type`,VALUE:`multipart/form-data`
> - BODY中选择类型为`form-data`并上传文件



### 3.2MYSQL



### 3.3IDEA

