---
layout: post
title: Redis部署与使用
slug: Redis部署与使用
date: 2020/11/21 15:17:13
status: publish
author: LifeAlsoIsGG
categories: 
  - 数据库
  - Redis
tags: 
  - 数据库
  - Redis
---



# 参考

> - [菜鸟笔记Redis](https://www.runoob.com/redis/redis-tutorial.html)



# Redis安装



## 使用Docker在Linux下安装

参考

> - https://www.runoob.com/docker/docker-install-redis.html





## 以配置文件方式启动

参考

> - https://blog.csdn.net/weixin_42456466/article/details/87270959





## 修改密码

参考

> - https://www.cnblogs.com/x-ll123/p/9717351.html







## 使用RedisDesktopManager连接

下载RedisDesktopManager后直接连接即可



![](images/Redis部署与使用/RedisDesktopManager.jpg)





连接后

![](images/Redis部署与使用/RedisDesktopManager-2.jpg)









# Redis性能测试redis-benchmark

参考

> - https://www.runoob.com/redis/redis-benchmarks.html





`Docker`中的`redis-benchmark`测试命令

参考

> - https://blog.csdn.net/jianjun_fei/article/details/95108694



```bash
docker exec -it containerName/containerid redis-benchmark -h 127.0.0.1 -p 6379 -c 100 -n 100000
```



![](images/Redis部署与使用/redis-benchmark.jpg)







# Redis基本命令使用

参考

> - [官方命令文档](https://redis.io/commands)
> - [redis中文文档](http://redisdoc.com/)



## 数据库



切换数据库

```bash
select 0
select 1
```



数据库大小(key数量)

```bash
dbsize
```



清空当前数据库

```bash
flushdb

#清空所有
flushall
```





## 键Key

参考

> - https://www.runoob.com/redis/redis-keys.html



### 查看所有key

```bash
keys *
```



### 设置过期时间

```bash
expire [key] [second]
```



### 查看剩余时间

```bash
ttl [key]
```

两种情况

> - -1：未设置过期时间
> - -2：已过期或不存在key



### 查看key对应的value类型

```bash
type key
```



### 给某个key的value拼接

```bash
append [key] [value]
```



### 获取key对应value的长度

```bash
strlen [key]
```



### 根据range截取

```bash
#截取字符串[0,3]
getrange [key] 0 3
```



### 替换

```bash
#从0开始替换为value
setrange [key] 0 [value]
```





### 对于value为integer类型的操作



#### 自增长++

```bash
incr [key]
```



#### 自减小--

```bash
decr [key]
```



#### 指定增加大小

```bash
incrby [key] [number]
```



#### 指定减小大小

```bash
decrby [key] [number]
```



## List

所有命令以l开头