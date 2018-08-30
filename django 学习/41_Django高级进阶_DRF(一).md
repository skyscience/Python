---
title: 41_Django高级进阶_DRF(一)
tags: 
notebook: Django_Courseware_1803
---
[toc]
# 一、前后端分离优缺点
![qu5dZn1](https://i.loli.net/2018/08/27/5b831b8097910.png)

## 1. 为什么要前后端分离
1. PC,APP,PAD,微信公众号...多端适应
2. SPA开发模型开始流行(单页面)　后端提供API,前段展示
3. 前后端开发职责不清(模板)
    - 模板到低是前端写还是后端写?如果前端写,前端就要懂后端模板语言
    - 如果后端写,那么后端就要懂前段html,css,js甚至更多更多
4. 开发效率问题,前后端相互等待
    - 前端在写的时候,就希望后端全部写好自己再写
    - 后端在写的时候,就希望前端全部写好自己再写
5. 前端一直配合着后端,能力受限(搞来搞去写静态页面,天天给后台写模板)
6. 后台开发语言和模板高度耦合,导致开发语言依赖(一旦用python开发,以后要换成java或者其他语言)

## 2. 前后端分离缺点　
1. 前后端学习门槛增加(比如后台很多模板语法控制前端展示,但是分离以后,需要前端自己去实现,增加前端成本,对后台来说,后端要满足规范)
2. 数据依赖导致文档重要性增加
    - 文档是否详细　
    - 是否及时更新
    - 修改要及时通知其他端
3. 前端工作量加大
4. SEO的难度增加(都是AJAX,像一些初级爬虫全部挡在外面,比如一些搜索引擎,这样你的排名就不靠前了)　
5. 后端开发模式迁移增加成本

## 3. 拓展阅读
[拓展阅读１](https://www.zhihu.com/question/267014376/answer/444793972)

[拓展阅读２](https://segmentfault.com/a/1190000009329474)


# 二、REST ful API
- 简单的说，就是一个规范,就是一个标准,就是目前,前后端分离的最佳实践

## 1. 优点
1. 轻量,直接通过http,不需要额外协议,post/get/put/delete操作　
2. 面向资源,一目了然,具有自解释性(简单来说比如我们有一个商品,商品就是资源,post商品就是提交商品,get商品就是获取商品...)
3. 数据描述简单,一般通过json或者xml做数据通信

# 二、Django REST framework

## 1. Django REST framework 是什么?

![logo](https://i.loli.net/2018/08/14/5b72262c7e54a.png)


## 2. 为什么要用Django REST framework
1. 前后端分离的业务需要搭建API
2. 基于Django 快速开发 Restful API 
![01](https://i.loli.net/2018/08/25/5b817646a862a.png)


## 3. RESTful API 规范是什么?

- GET（SELECT）：从服务器取出资源（一项或多项）。
- POST（CREATE）：在服务器新建一个资源。
- PUT（UPDATE）：在服务器更新资源（客户端提供改变后的完整资源）。
- PATCH（UPDATE）：在服务器更新资源（客户端提供改变的属性）。
- DELETE（DELETE）：从服务器删除资源。
- HEAD：获取资源的元数据。
- OPTIONS：获取信息，关于资源的哪些属性是客户端可以改变的

## 4. 环境以及工具　
1). PyCharm

2). Django (1.11+)

3). djangorestframeowrk (3.6+)

4). httpie (在命令行里面模拟http请求的客户端)

## 5. 一些文档资料

[理解RESTful架构](http://www.ruanyifeng.com/blog/2011/09/restful.html)

[RESTful API设计指南](http://www.ruanyifeng.com/blog/2014/05/restful_api.html)

[HTTP状态码](http://tool.oschina.net/commons?type=5)

[Django REST framework官网](http://www.django-rest-framework.org/)

[Django REST framework中文文档](https://q1mi.github.io/Django-REST-framework-documentation/)
