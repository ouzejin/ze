---
layout: post
title: IDEA初始化SpringBoot项目
slug: IDEA初始化SpringBoot项目
date: 2020/10/01 22:40:15
status: publish
author: LifeAlsoIsGG
categories: 
  - Spring
  - SpringBoot
tags: 
  - SpringBoot
  - IDEA

---



# 1. 使用阿里云镜像作为初始源创建



1. 选择Spring initializr
2. 选择来源链接：https://start.aliyun.com/

![](images/IDEA创建SpringBoot项目/使用阿里云镜像.jpg)





# 2. 项目信息



![](images/IDEA创建SpringBoot项目/project_metadata.jpg)





# 3. 选择依赖



![](images/IDEA创建SpringBoot项目/选择依赖.jpg)





# 4. 配置application.yml(更新中)

在`resources`文件夹下删除`application.properties`,并创建`application.yml`

application.yml基本配置如下

```yml
spring:
  application:
    name: springboot_demo
  datasource:
    username: root
    password: root
    url: jdbc:mysql://localhost:3306/attendance_demo
    driver-class-name: com.mysql.jdbc.Driver


#指定端口号
server:
  port: 8001
```





# 5. 配置pom.xml依赖(更新中)

参考

> - [springboot之依赖集锦pom.xml（更新中）](https://blog.csdn.net/IT_lyd/article/details/76423290?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param)



## springboot相关



```xml
		<!-- springboot相关 -->
		<!-- springboot 基础包 -->
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter</artifactId>
		</dependency>
 
		<!-- springboot 测试包 -->
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-test</artifactId>
			<scope>test</scope>
		</dependency>
 
		<!-- springboot web包 -->
		<dependency>
		  <groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
		</dependency>

		<!--spring-boot-starter-security-->
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-security</artifactId>
     </dependency>
    <dependency>
      <groupId>org.springframework.security</groupId>
      <artifactId>spring-security-test</artifactId>
      <scope>test</scope>
    </dependency>

     <!-- spring aop -->
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-aop</artifactId>
    </dependency>


		<!-- springboot web开发thymeleaf模板 -->
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-thymeleaf</artifactId>
		</dependency>


		<!-- springboot工具 修改代码后不需重启即生效 -->
		<dependency>
			<groupId>org.springframework</groupId>
			<artifactId>springloaded</artifactId>
		</dependency>

        <!-- fastdfs -->
        <dependency>
            <groupId>com.luhuiguo</groupId>
            <artifactId>fastdfs-spring-boot-starter</artifactId>
            <version>0.2.0</version>
        </dependency>
```



## 数据库相关

```xml
    <properties>
      <java.version>1.8</java.version>
      <mybatis.version>2.1.2</mybatis.version>
    </properties>

				<!-- 数据库相关 -->

				<!-- mysql驱动 -->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
        </dependency>

        <!-- jdbc连接工具 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-jdbc</artifactId>
        </dependency>

				<!--mybatis-->
        <dependency>
            <groupId>org.mybatis.spring.boot</groupId>
            <artifactId>mybatis-spring-boot-starter</artifactId>
            <version>${mybatis.version}</version>
        </dependency>

        <!-- redis -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-redis</artifactId>
        </dependency>

<!-- mybatis逆向工程 -->
<!-- https://mvnrepository.com/artifact/org.mybatis.generator/mybatis-generator-core -->
				<dependency>
    				<groupId>org.mybatis.generator</groupId>
    				<artifactId>mybatis-generator-core</artifactId>
    				<version>1.3.7</version>
				</dependency>
```





## 工具相关

```xml
    <properties>
      <java.version>1.8</java.version>
      <swagger.version>2.9.2</swagger.version>	
    </properties>


				<!-- 工具类 -->
				<!-- 日志管理 log4j -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-log4j</artifactId>
        </dependency>

				<!-- fastjson -->
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>fastjson</artifactId>
            <version>1.2.15</version>
        </dependency>

        <!-- lombok -->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
        </dependency>

        <!-- page helper -->
        <dependency>
            <groupId>com.github.pagehelper</groupId>
            <artifactId>pagehelper-spring-boot-starter</artifactId>
            <version>1.2.10</version>
        </dependency>

        <!-- simpleEmail -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-mail</artifactId>
        </dependency>

        <!-- easyexcel -->
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>easyexcel</artifactId>
            <version>2.2.6</version>
        </dependency>

				<!--Swagger依赖-->
        <dependency>
            <groupId>io.springfox</groupId>
            <artifactId>springfox-swagger2</artifactId>
            <version>${swagger.version}</version>
        </dependency>
        <dependency>
            <groupId>io.springfox</groupId>
            <artifactId>springfox-swagger-ui</artifactId>
            <version>${swagger.version}</version>
        </dependency>
```





