---
title: 46_Django高级进阶_DRF(六)
tags: 
notebook: Django_Courseware_1803
---
# 一、认证和权限
目前，我们的API对谁可以编辑或删除代码段没有任何限制。我们希望有更高级的行为，以确保：
- 代码片段始终与创建者相关联。
- 只有通过身份验证的用户可以创建片段。
- 只有代码片段的创建者可以更新或删除它。
- 未经身份验证的请求应具有完全只读访问权限。

## 1.　在模型中增加一个字段
- 我们要做一个只有本人才能修改的权限
```python
    # 操作者
    operator = models.ForeignKey('auth.User')
```

![选区_197](https://i.loli.net/2018/08/26/5b82474cb60ee.png)

## 2.  生成迁移文件和执行迁移
- 解决报错
这里报错的原因是，它说之前我们已经创建了很多条数据,现在你又给表增加了字段,原来的数据库里面没有这个字段,你又设置默认值,要么你输入１提供默认值,要输入２退出

![选区_198](https://i.loli.net/2018/08/26/5b8247ab912a1.png)

![选区_199](https://i.loli.net/2018/08/26/5b82489ece45d.png)

## 3.  去序列化里面把字段给添加上
![选区_200](https://i.loli.net/2018/08/26/5b82490ddc9b2.png)


- 刷新浏览器

![选区_001](https://i.loli.net/2018/08/26/5b824c5a70537.png)
-　重写operator　拿出用户名字段
```python
    # 读取用户名
    operator = serializers.ReadOnlyField(source='operator.username')
```
![选区_003](https://i.loli.net/2018/08/26/5b824d024bf4f.png)

![选区_004](https://i.loli.net/2018/08/26/5b824d24693cf.png)

## 4. 只有本人让修改(就是谁录入的谁才有权限修改)
- 导入模块
```python
from rest_framework import permissions
```
- 在视图里面添加一个权限(空权限)　
![选区_005](https://i.loli.net/2018/08/26/5b824e0437503.png)

![选区_008](https://i.loli.net/2018/08/26/5b824e9742730.png)

- 退出登录,刷新浏览器

![选区_006](https://i.loli.net/2018/08/26/5b824e4801f0e.png)

![选区_007](https://i.loli.net/2018/08/26/5b824e6885348.png)

![选区_009](https://i.loli.net/2018/08/26/5b824ef421cfc.png)

## 5. 创建自己的权限
- 创建一个模块

![选区_011](https://i.loli.net/2018/08/26/5b824f790ff44.png)

```python

from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    自定义权限只允许对象的所有者编辑它
    """
    def has_object_permission(self, request, view, obj):
        # 读取权限允许任何请求
        # 所以我们总是允许GET　HEAD POTIONS请求
        if request.method in permissions.SAFE_METHODS:
            return True
        # 只有该出版社的录入者才有权限写
        return obj.operator == request.user
```
- 创建一个新账号

![选区_012](https://i.loli.net/2018/08/26/5b82513d6b7cf.png)

- 切换账号

![选区_014](https://i.loli.net/2018/08/26/5b8251abc3c5e.png)

- 导入自己的写的权限
```python
from app01.permissions import IsOwnerOrReadOnly
```
![选区_015](https://i.loli.net/2018/08/26/5b8252786394f.png)

- 因为不是录入者,不能写
