---
title: 44_Django高级进阶_DRF(四)
tags: 
notebook: Django_Courseware_1803
---

# 一、请求和响应
## 1. 请求对象（Request objects）拓展了Django自带的HttpRequest
REST框架引入了一个扩展了常规HttpRequest的Request对象，并提供了更灵活的请求解析。Request对象的核心功能是request.data属性，它与request.POST类似，但对于使用Web API更为有用。
```python
request.POST  # 只处理表单数据  只适用于'POST'方法
request.data  # 处理任意数据  适用于'POST'，'PUT'和'PATCH'方法
```
## 2. 响应对象（Response objects）
REST框架还引入了一个Response对象，这是一种获取未渲染（unrendered）内容的TemplateResponse类型，并使用内容协商来确定返回给客户端的正确内容类型。
```python
return Response(data)  # 渲染成客户端请求的内容类型。
```

## 3. 状态码（Status codes）

在你的视图（views）中使用纯数字的HTTP 状态码并不总是那么容易被理解。而且如果错误代码出错，很容易被忽略。REST框架为status模块中的每个状态代码（``如HTTP_400_BAD_REQUEST``）提供更明确的标识符。使用它们来代替纯数字的HTTP状态码是个很好的主意。

## 4. 包装（wrapping）API视图

REST框架提供了两个可用于编写API视图的包装器（wrappers）。

``1. 用于基于函数视图的@api_view装饰器。``

``2. 用于基于类视图的APIView类。``

这些包装器提供了一些功能，例如确保你在视图中接收到Request实例，并将上下文添加到Response，以便可以执行内容协商。

包装器还提供了诸如在适当时候返回405 Method Not Allowed响应，并处理在使用格式错误的输入来访问request.data时发生的任何ParseError异常。

# 二、应用
## 1. 导入模块
```python
from .models import Publisher
from rest_framework.decorators import api_view
from app01 import serializers
from rest_framework.response import Response
```
## 2. 编写视图
- GET
```python
from .models import Publisher
from rest_framework.decorators import api_view
from app01 import serializers
from rest_framework.response import Response


# 列表里面的参数是被允许的操作,比如只有GET/POST请求,如果不是get或者post会报405－－－>405 Method Not Allowed
@api_view(['GET', 'POST'])
def publisher_list(request):
    """
    列出所有出版社,get
    或者创建一个新的出版社 post
    """
    if request.method == 'GET':
        # 所有的出版社
        queryset = Publisher.objects.all()
        # 把所有从数据库取出来的出版社信息数据进行序列化
        s = serializers.PublisherSerializer(queryset, many=True)
        return Response(s.data)
```
- POST

```python
     if request.method == 'POST':
        # post请求就是---->创建出版社
        # 跟上面不同,从数据转化成序列化的参数
        # 说白了就是把客户端传过来的数据,用序列化生成实例对象
        s = serializers.PublisherSerializer(data=request.data)
        if s.is_valid():  # 如果数据没问题
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        else:
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
```

![选区_178](https://i.loli.net/2018/08/26/5b81a31869527.png)

## 3.获取、更新或者删除一个(单个)出版社信息
-　GET
```python
# GET 获取出版社　
@api_view(['GET', 'PUT', 'DELETE'])
def publisher_detail(request, pk):
    try:
        # 从数据库里面找你要找的pk
        publisher = Publisher.objects.get(pk=pk)
    except Publisher.DoesNotExist:  # 如果找不到浏览器传来的pk对应的数据,返回４０４
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # 从数据库里面取出来的publisher进行序列化
        s = serializers.PublisherSerializer(publisher)
        return Response(s.data)
```

- POST
```python
 if request.method == 'PUT':
        # publisher使我们查出来的出版社信息　　request.data是客户端传过来的
        s = serializers.PublisherSerializer(publisher, data=request.data)
        if s.is_valid():# 如果数据没有问题
            s.save()
            return Response(s.data)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
```
![选区_179](https://i.loli.net/2018/08/26/5b81a5cac5a18.png)

- DELETE
```python
 if request.method == 'DELETE':
        publisher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```
## 4. 给我们的网址添加可选的格式后缀
为了充分利用我们的响应不再与单一内容类型连接，我们可以为API路径添加对格式后缀的支持。使用格式后缀给我们明确指定了给定格式的URL，这意味着我们的API将能够处理诸如http://example.com/api/items/4.json之类的URL。

### 4.1 设置路由
```python
url(r'^publishers/(?P<pk>[0-9]+)/$', views.publisher_detail)
```
![选区_180](https://i.loli.net/2018/08/26/5b81a74cc3c2e.png)

### 4.2 刷新浏览器(无法访问数据,无权限)
![选区_181](https://i.loli.net/2018/08/26/5b81a7a53c689.png)

### 4.3 创建一个账号
![选区_182](https://i.loli.net/2018/08/26/5b81a81a89113.png)

- 接下来我们可以通过两种方式访问
方式一: httpie
```
pip install httpie
```
然后在命令行访问

![选区_183](https://i.loli.net/2018/08/26/5b81a9143e1d4.png)

![选区_184](https://i.loli.net/2018/08/26/5b81aac04e4ad.png)

方式二:（调出登录)
```python
url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
```

![选区_186](https://i.loli.net/2018/08/26/5b81ac7e449f0.png)

![选区_185](https://i.loli.net/2018/08/26/5b81ac60e9c43.png)

![选区_187](https://i.loli.net/2018/08/26/5b81acb0c69cc.png)

