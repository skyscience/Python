# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawljobboleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 时间
    publishTime = scrapy.Field()
    # tag
    tags = scrapy.Field()
    # 简介
    desctext = scrapy.Field()
    # 评论数
    commentNum = scrapy.Field()
    # 图片连接
    image_url = scrapy.Field()
    # # 本地图片路径
    # image_url = scrapy.Field()

    def insert_data(self,dict):

        insert_sql = 'INSERT INTO article(%s) VALUES (%s)' % (','.join([key for key,value in dict.items()]),','.join(['%s' for key,value in dict.items()]))
        #INSERT INTO article(publishTime,desc,commentNum,tags,title,image_url) VALUES (%s,%s,%s,%s,%s,%s)
        # insert_sql = 'INSERT INTO article(publishTime,desc,commentNum,tags,title,image_url) VALUES ("%s","%s","%s","%s","%s","%s")'
        parmas = [value for key,value in dict.items()]
        # parmas = [self['publishTime'],self['desc'],self['commentNum'],self['tags'],self['title'],self['image_url']]
        print(insert_sql)
        print(parmas)

        return insert_sql,parmas


