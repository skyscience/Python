---
title: 49_Django高级进阶_DRF(九)
tags: 
notebook: Django_Courseware_1803
---

# 一、概要和文档
## 1. 安装包
```sh
 pip install coreapi
```

## 2. 在urls里面导入
```python
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Pastebin API')

....

url(r'^schema/$',schema_view),
```

![选区_046](https://i.loli.net/2018/08/26/5b8279cacfb1f.png)

- 刷新浏览器

![选区_047](https://i.loli.net/2018/08/26/5b827a2299452.png)

## 3. 改进
```python
from rest_framework.documentation import include_docs_urls
....

urlpatterns = [
    url(r'^docs/',include_docs_urls(title='图书管理系统')),
....
```
![选区_048](https://i.loli.net/2018/08/26/5b827ae2af5c6.png)

- 刷新浏览器

![选区_049](https://i.loli.net/2018/08/26/5b827b09783c2.png)


![选区_050](https://i.loli.net/2018/08/26/5b827be84f662.png)