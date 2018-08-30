---
title: 43_Django高级进阶_DRF(三)
tags: 
notebook: Django_Courseware_1803
---

# 一、序列化

## 1. 创建表

- 以出版社的表为例子,例如出版社有名字和所属地区

![选区_051](https://i.loli.net/2018/08/26/5b82a9cf79842.png)

```python
class Publisher(models.Model):
    name = models.CharField(max_length=32, verbose_name='名称', unique=True)
    address = models.CharField(max_length=128, verbose_name='地址')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '出版社'
        verbose_name_plural = verbose_name
```

![选区_162](https://i.loli.net/2018/08/26/5b81807f43e86.png)

## 2. 生成迁移文件和执行迁移
- 在这里我们暂时用sqlite数据库
```sh
python manage.py makemigrations
python manage.py migrate
```

## 3. 什么是序列化
[维基百科资料关于序列化的介绍](https://zh.wikipedia.org/wiki/%E5%BA%8F%E5%88%97%E5%8C%96)

### 3.1 关于序列化的解释:
在程序运行的过程中，所有的变量都是在内存中，比如，定义一个dict：
```python
d = dict(name='Zhangsan', age=26, score=75)
```

可以随时修改变量，比如把name改成'LiSi'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。如果没有把修改后的'LiSi'存储到磁盘上，下次重新运行程序，变量又被初始化为'Zhangsan'。

**我们把变量从内存中变成可存储或传输的过程称之为序列化**，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

反过来，**把变量内容从序列化的对象重新读到内存里称之为反序列化**，即unpickling。

### 3.2 JSON
**如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式**，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：

|JSON类型 |	Python类型|
|:-------|:-----|
|{} 	|dict|
|[] 	|list|
|"string"| 	str|
|1234.56 |	int或float|
|true/false |	True/False|
|null |	None|

Python内置的json模块提供了非常完善的Python对象到JSON格式的转换:

### 3.2.1 把Python对象变成一个JSON：
```python
import json
d = dict(name='Zhangsan', age=26, score=75)
# dumps()方法返回一个str，内容就是标准的JSON
json_str= json.dumps(d)
```
### 3.2.2 要把JSON反序列化为Python对象，用loads()方法:

```python
json_str = '{"age": 26, "score": 75, "name": "Zhangsan"}'
json.loads(json_str)
```

## 4. 通过以下方式可以实现API：
- 编写视图:
```python
from .models import Publisher
from django.http import HttpResponse


def publisher_list(request):
    # 查询出所有的出版社
    queryset = Publisher.objects.all()
    # 转换成python中的列表
    data = []
    for i in queryset:
        # 每一个对象都手动转化成一个字典
        p_tmp = {
            'name': i.name,
            'address': i.address
        }
        data.append(p_tmp)

    import json

    return HttpResponse(json.dumps(data), content_type='application/json')
```

![选区_163](https://i.loli.net/2018/08/26/5b8187d3e87d7.png)

- 配置路由:

```python
url(r'^publishers/', views.publisher_list)
```

- 启动项目
```python
python manage.py runserver
```

![选区_164](https://i.loli.net/2018/08/26/5b818857ce7d5.png)

- 手动添加数据

![选区_165](https://i.loli.net/2018/08/26/5b81891865073.png)

- 刷新浏览器

![选区_166](https://i.loli.net/2018/08/26/5b8189867bbc3.png)

![选区_167](https://i.loli.net/2018/08/26/5b8189b76948a.png)

## 5. 对于以上的方案进行第一次改进:

```python
data = []
from django.forms.models import model_to_dict
for i in queryset:
    data.append(model_to_dict(i))
```
注意:这种方式有缺陷,很多字段无法转换成字典,比如图片
![选区_168](https://i.loli.net/2018/08/26/5b818b0c4e203.png)

## 6. 对于以上的方案进行第二次改进(使用Django自带的serializers):

```python
data = []
from django.core import serializers
data = serializers.serialize('json', queryset)

import json
return HttpResponse(data, content_type='application/json')
```
注意:此时data已经是json类型
![选区_169](https://i.loli.net/2018/08/26/5b818c2479231.png)

- 刷新浏览器

![选区_170](https://i.loli.net/2018/08/26/5b818cb3e93e0.png)

# 二、DRF提供的序列化
DRF提供的方案更加先进,更高级别的序列化方案,不仅仅可以实现从数据库里面读取数据,更可以存数据(增删改查)

## 1. 在APP下创建一个序列化一个文件
- 我们自己定义一个序列化
```python

from rest_framework import serializers


# 类名固定为表名称 + Serializer
class PublisherSerializer(serializers.Serializer):
    # read_only必须为True,因为我们模型里面的id是一个自增字段,不可写,自动生成
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=32)
    address = serializers.CharField(max_length=128)
```
![选区_171](https://i.loli.net/2018/08/26/5b818f08cb4a6.png)

## 2. 使用自己定义的序列化
- 非常方便的把我们的对象转化成一个字典
```python
from app01 import models,serializers
p1 = models.Publisher.objects.first()# 先找到一个出版社的对象
s = serializers.PublisherSerializer(p1)
s.data
```

![选区_172](https://i.loli.net/2018/08/26/5b819006d381e.png)

## 3. 给自定义的序列化增加一个'create'和'update'的功能
- 重写父类
```python
def create(self, validated_data):
    # validated_data参数不需要特意去记,就是经过校验的数据
    return models.Publisher.objects.create(**validated_data)

def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.address = validated_data.get('address', instance.address)
    instance.save()
    return instance
```
- 使用　

```python
from app01 import models,serializers
p2 = {'name':'图灵出版社','address':'大兴天宫院'}
s = serializers.PublisherSerializer(data=p2)
s.is_valid()# 如果数据检测没有问题
Out[5]: True
s.validated_data # 可以查看类型,观察到这是一个有序字典
Out[6]: OrderedDict([('name', '图灵出版社'), ('address', '大兴天宫院')])
s.save() # 保存到数据库
Out[7]: <Publisher: 图灵出版社>
```

![选区_173](https://i.loli.net/2018/08/26/5b819299b9882.png)

- 刷新浏览器

![选区_174](https://i.loli.net/2018/08/26/5b8192f0a765e.png)

- 在视图里面使用
```python

    # 第三次改进
    from app01 import serializers
    # 如果是多个对象,一定要写many = True,就是说我们是多个对象,
    # many=True告诉程序要用遍历的方式去给我们做序列化
    s = serializers.PublisherSerializer(queryset, many=True)

    import json
    return HttpResponse(json.dumps(s.data), content_type='application/json')
```

![选区_175](https://i.loli.net/2018/08/26/5b8193b5d540f.png)

## 4.　改进自定义序列化模块
- 因为那些字段,我们已经在模型中创建,没有必要再创建一次,所以我们再进行一次改进
```python
class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher  # 我们要使用的模型
        # 我们要使用的字段
        fields = (
            'id',
            'name',
            'address'
        )
```
![选区_176](https://i.loli.net/2018/08/26/5b81953f50ded.png)

- 刷新浏览器,依旧可以正常运行,也就说是我们可以自己去写每一个字段,当然可以用ModelSerializer,直接使用我们的模型(相当于和我们数据库里面的表字段一一对应)

![选区_177](https://i.loli.net/2018/08/26/5b8195a208241.png)







