---
title: 45_Django高级进阶_DRF(五)
tags: 
notebook: Django_Courseware_1803
---
# 一、基于类的视图（CBV）
## 1. 导入模块
```python
from rest_framework.views import APIView
```
## 2. GET
```python
from .models import Publisher
from app01 import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class PublisherList(APIView):
    """
    列出所有的出版,get
    或者创建一个新的出版社post
    """

    def get(self, request, format=None):
        queryset = Publisher.objects.all()  # 查询出所有出版社
        s = serializers.PublisherSerializer(queryset, many=True)
        return Response(s.data, status=status.HTTP_200_OK)
```

## 2. POST
```python
    def post(self,request,format=None):
        s = serializers.PublisherSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data,status=status.HTTP_201_CREATED)
        else:
            return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)
```

![选区_188](https://i.loli.net/2018/08/26/5b81af1581e8e.png)

## 4. 具体的某一个出版社CBV
```python
class PublisherDetail(APIView):
    """
    具体的某一个出版社　　查看．修改．删除的视图
    """

    # 需要先尝试的从数据库查到　pk对应的数据,如果没有返回404
    def get_object(self, pk):
        try:
            return Publisher.objects.get(pk=pk)
        except Publisher.DoesNotExist:
            raise Http404 # 需要先导入　from django.http import Http404
```
- GET　获取出版社信息(单个)
```python
 def get(self, request, pk, format=None):
        publisher = self.get_object(pk)
        s = serializers.PublisherSerializer(publisher)
        return Response(s.data, status=status.HTTP_200_OK)
```
- PUT 修改出版社信息(单个)
```python
    def put(self, request, pk, format=None):
        publisher = self.get_object(pk)
        s = serializers.PublisherSerializer(publisher, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
```
![选区_189](https://i.loli.net/2018/08/26/5b81b1cc2c3f2.png)
- DELETE 　删除出版社信息(单个)
```python
    def delete(self, request, pk, format=None):
        """删除出版社信息"""
        publisher = self.get_object(pk)
        publisher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```
## 5. 修改url
```python
url(r'^publishers/$', views.PublisherList.as_view()),
url(r'^publishers/(?P<pk>[0-9]+)/$', views.PublisherDetail.as_view()),
```

![选区_190](https://i.loli.net/2018/08/26/5b81b2fde2366.png)


# 二、使用混合（mixins）
使用基于类视图的最大优势之一是它可以轻松地创建可复用的行为。

到目前为止，我们使用的创建/获取/更新/删除操作和我们创建的任何基于模型的API视图非常相似。这些常见的行为是在REST框架的mixin类中实现的。
## 1.导入模块
```python
from rest_framework import mixins
from rest_framework import generics
```

## 2.编写视图
```python
from rest_framework import mixins
from rest_framework import generics


class PublisherList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = Publisher.objects.all()
    serializers_class = serializers.PublisherSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```

![选区_191](https://i.loli.net/2018/08/26/5b824141a04cb.png)

```python
class PublisherDetail(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):

    queryset = Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
```
- 刷新浏览器

![选区_192](https://i.loli.net/2018/08/26/5b8242fae799e.png)

## 3.改进混合视图
```python
class PublisherList(generics.ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer
```

```python
class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer
```

- 刷新浏览器 
![选区_193](https://i.loli.net/2018/08/26/5b82447a8a726.png)

![选区_194](https://i.loli.net/2018/08/26/5b8244afb7ac0.png)

## 4. 此时我们观察,代码已经精简至3行
官方文档一句话说的非常好:仅仅只需要很少的几行代码,就可以完成非常清晰,简洁,地道的Django

![选区_195](https://i.loli.net/2018/08/26/5b8244ea855d2.png)