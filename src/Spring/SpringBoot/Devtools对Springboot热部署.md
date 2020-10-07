---
layout: post
title: Devtools对Springboot热部署
slug: Devtools对Springboot热部署
date: 2020/10/07 23:05:45
status: publish
author: LifeAlsoIsGG
categories: 
  - Spring
  - SpringBoot
tags: 
  - IDEA
  - SpringBoot
---



这种方式是属于项目重启（速度比较快的项目重启），会清空session中的值，也就是如果有用户登陆的话，项目重启后需要重新登陆。



# 参考

> - https://blog.csdn.net/chachapaofan/article/details/88697452





# 1. 引入依赖

```xml
<!--devtools热部署-->
<dependency>
	<groupId>org.springframework.boot</groupId>
	<artifactId>spring-boot-devtools</artifactId>
	<optional>true</optional>
  <scope>runtime</scope>
</dependency>


<build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <fork>true</fork>
                  	<addResources>true</addResources>
                </configuration>
            </plugin>
        </plugins>
    </build>
```





# 2. 配置application.yml

```yml
spring:
  devtools:
    restart:
      enabled: true  #设置开启热部署
      additional-paths: src/main/java #重启目录
      exclude: WEB-INF/**
  freemarker:
    cache: false    #页面不加载缓存，修改即时生效
```





# 3. IDEA配置



## 3.1 第一步

File-Settings-Compiler-Build Project automatically



![](images/Devtools对Springboot热部署/热部署IDEA配置_1.jpg)



## 3.2 第二步

ctrl + shift + alt + / ,选择Registry,勾上 Compiler autoMake allow when app running

![](images/Devtools对Springboot热部署/热部署IDEA配置_2.jpg)



# 4. 热部署

修改文件后`Ctrl + F9`，即Build Project便会快速重启项目