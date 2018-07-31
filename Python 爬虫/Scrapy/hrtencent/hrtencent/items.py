# -*- coding: utf-8 -*-
import scrapy

#  通过创建一个 scrapy.Item 类， 并且定义类型为 scrapy.Field的类属性来定义一个Item
# 可以理解成类似于ORM的映射关系
class HrtencentItem(scrapy.Item):
    # 构建item模型
    name = scrapy.Field()
    link = scrapy.Field()
    positionType = scrapy.Field()
    peopleNum = scrapy.Field()
    workLoaction = scrapy.Field()
    publishTime = scrapy.Field()