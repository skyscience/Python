---
title: 47_Django高级进阶_DRF(七)
tags: 
notebook: Django_Courseware_1803
---

# 一、超链接API
目前我们的API中的关系是用主键表示的。我们将通过使用超链接来提高我们API的内部联系。

## 1. 新建一张表(模型类)
```python
class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name='书名')
    publisher = models.ForeignKey('Publisher')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '书'
        verbose_name_plural = verbose_name
```
## 2. 生成迁移文件和执行迁移

## 3. 创建书的序列化
```python
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = (
            'id',
            'title',
            'publisher'
        )

```
## 4. 编写Book相关视图
```python
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = (permissions.IsAuthenticated,)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = (permissions.IsAuthenticated)
```

![选区_016](https://i.loli.net/2018/08/26/5b82575877238.png)

## 5. 增加新的路由
```python
    url(r'^books/$',views.BookList.as_view()),
    url(r'^books/(?P<pk>[0-9]+)/$',views.BookDetail.as_view())
```
![选区_017](https://i.loli.net/2018/08/26/5b8257df1ed58.png)

- 没数据

![选区_018](https://i.loli.net/2018/08/26/5b8258361a51c.png)

## 6. 增加几条数据
![选区_019](https://i.loli.net/2018/08/26/5b82586d1705d.png)

![选区_020](https://i.loli.net/2018/08/26/5b8258abc7c12.png)

## 7. 通过外键重写显示字段转化为字符串(StringRelatedField)
```python
publisher = serializers.StringRelatedField(source='publisher.name')
```
![选区_021](https://i.loli.net/2018/08/26/5b8259571a0d9.png)

![选区_022](https://i.loli.net/2018/08/26/5b8259d5ef386.png)

## 8.设置超链接
![选区_023](https://i.loli.net/2018/08/26/5b825a18759cc.png)

- 解决报错

![选区_024](https://i.loli.net/2018/08/26/5b825a4b6fc4e.png)

![选区_025](https://i.loli.net/2018/08/26/5b825af61424f.png)

![选区_026](https://i.loli.net/2018/08/26/5b825b3579fc8.png)

# 二、浏览API
## 1. 导入模块
```python
from rest_framework.reverse import reverse
```
## 2. 编写视图函数　
```python
@api_view(['GET'])
def api_root(request, format=None):
    return Response(
        {
            'publishers': reverse('publisher-list', request=request, format=format),
            'books': reverse('books_list', request=request, format=format)
        }
    )
```

![选区_030](https://i.loli.net/2018/08/26/5b825fe68a9fc.png)

## 3. 在app下面单独创建一个urls
![选区_027](https://i.loli.net/2018/08/26/5b825cf1a3682.png)

```python
from django.conf.urls import url, include
from app01 import views


urlpatterns = [

    url(r'^publishers/$', views.PublisherList.as_view(), name='publisher-list'),
    url(r'^publishers/(?P<pk>[0-9]+)/$', views.PublisherDetail.as_view(), name='publisher-detail'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest-framework')),
    url(r'^books/$', views.BookList.as_view(), name='books_list'),
    url(r'^books/(?P<pk>[0-9]+)/$', views.BookDetail.as_view(), name='books-detail')

]


```

![选区_028](https://i.loli.net/2018/08/26/5b825e963782a.png)

![选区_029](https://i.loli.net/2018/08/26/5b825eeca402e.png)

- 刷新浏览器，展示所有api

![选区_031](https://i.loli.net/2018/08/26/5b82602aaf128.png)

# 三、分页
![选区_032](https://i.loli.net/2018/08/26/5b8260b341eee.png)

![选区_033](https://i.loli.net/2018/08/26/5b8260d207cd2.png)

![选区_034](https://i.loli.net/2018/08/26/5b8260f17943d.png)


