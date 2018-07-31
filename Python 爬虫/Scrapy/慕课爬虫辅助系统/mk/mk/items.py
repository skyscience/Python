# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field


class MkItem(scrapy.Item):
    #标题
    title = Field()
    # 链接
    url = Field()
    # 图片
    # img = Field()
    # 课程介绍
    info = Field()
    # 学员数量
    student = Field()