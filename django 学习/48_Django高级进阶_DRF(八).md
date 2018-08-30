---
title: 48_Django高级进阶_DRF(八)
tags: 
notebook: Django_Courseware_1803
---

# 一、视图集和路由器
EST框架包括一个用于处理ViewSets的抽象，它允许开发人员集中精力对API的状态和交互进行建模，并根据常规约定自动处理URL构造。

ViewSet类与View类几乎相同，不同之处在于它们提供诸如read或update之类的操作，而不是get或put等方法处理程序。

最后一个ViewSet类只绑定到一组方法处理程序，当它被实例化成一组视图的时候，通常通过使用一个Router类来处理自己定义URL conf的复杂性。

## 1. 导入模块
```python
from rest_framework import viewsets
```
## 2. 重构视图
```python
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly)

```
![选区_036](https://i.loli.net/2018/08/26/5b826c4dd9d3e.png)

## 3. 配置路由
```python
book_list = views.BookViewSet.as_view(
    {
        'get': 'list',
        'post': 'create'
    }
)

book_detail = views.BookViewSet.as_view(
    {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destory'
    }
)

urlpatterns = [
   ...
    # 使用viewset
    url(r'^books/$',book_list,name='book-list'),
    url(r'^books/(?P<pk>[0-9])/$',book_detail,name='book-detail')
    ....
]
```

![选区_037](https://i.loli.net/2018/08/26/5b826e2880472.png)

- 刷新浏览器

![选区_038](https://i.loli.net/2018/08/26/5b8272fe0e551.png)

## 4. 改进代码(路由器)
-　导入模块
```python
from rest_framework.routers import DefaultRouter
```

- 注册路由器
```python
router = DefaultRouter()
router.register(r'^books/$',views.BookViewSet)
```

![选区_040](https://i.loli.net/2018/08/26/5b8274df7bcc7.png)


- 刷新浏览器

![选区_041](https://i.loli.net/2018/08/26/5b827502c9831.png)


```python
class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
```

```python
router.register(r'publishers', views.Publisher)
```

![选区_043](https://i.loli.net/2018/08/26/5b82765dad281.png)


![选区_044](https://i.loli.net/2018/08/26/5b827681e702e.png)

![选区_045](https://i.loli.net/2018/08/26/5b827692e99a5.png)