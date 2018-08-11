# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HongnianItem(scrapy.Item):
    # define the fields for your item here like:
    # 姓名
    name = scrapy.Field()
    #年龄
    age = scrapy.Field()
    #身高
    hight = scrapy.Field()
    #工作地点
    workLocal = scrapy.Field()
