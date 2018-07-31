# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field

class Test1Item(scrapy.Item):
    #标题
    title = Field()
    # 
    url = Field()
    # img = Field()
    info = Field()
    student = Field()

