---
title: 42_Django高级进阶_DRF(二)
tags: 
notebook: Django_Courseware_1803
---

# 一、项目准备工作

## 1. 新建一个虚拟环境

```sh
mkvirtualenv h2_dajngo_drf_envs
```

## 2. 安装django和djangorestframework

```sh
pip install django==1.11
pip install djangorestframework 
```

## 3. 新建一个Django项目

![选区_159](https://i.loli.net/2018/08/25/5b817c33b1739.png)

## 4. 将rest_framework注册到INSTALLED_APPS中去

```python
INSTALLED_APPS = (
    ...
    'rest_framework',
)
```

效果如图:

![选区_160](https://i.loli.net/2018/08/26/5b817e805ac4a.png)

## 5. rest_framework相关配置
```python
# 所有跟rest framework有关的配置
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'PAGE_SIZE': 10
}
```

效果如图:

![选区_161](https://i.loli.net/2018/08/26/5b817eb57ebcd.png)
