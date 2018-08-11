# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaidutravelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #标题
    title = scrapy.Field()
    #星级
    start_new = scrapy.Field()
    #评论
    remarkcount = scrapy.Field()
    #描述
    desc = scrapy.Field()
    #所有图片的页面接口
    allImagePageUrl = scrapy.Field()
    #总的路线
    luxiannums = scrapy.Field()
    #路线列表
    path_list = scrapy.Field()
    #评论列表
    remarklist = scrapy.Field()

