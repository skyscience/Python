# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaidulvyouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #图片连接
    image_url = scrapy.Field()
    #本地图片路径
    image_path = scrapy.Field()
    #游记标题
    note_title = scrapy.Field()
    #用户名称
    user_name = scrapy.Field()
    #点赞数量
    zan_num = scrapy.Field()
    #内容
    content = scrapy.Field()
    #观看数量
    visit_num = scrapy.Field()
    #评论数量
    comment_num = scrapy.Field()
    #回复内容
    replay_content = scrapy.Field()

    def insert_sql(self):
        insert_sql = """
        INSERT INTO youji(image_url,image_path,note_title,user_name,zan_num,content,visit_num,comment_num,replay_content)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        parmas = (self['image_url'],self['image_path'],
                  self['note_title'],self['user_name'],
                  self['zan_num'],self['content'],
                  self['visit_num'],self['comment_num'],
                  self['replay_content'])
        return insert_sql,parmas

    #如果不想写那摩多的字段，可以用列表推导式和字典推导式来实现
    def insert_sql(self,itemDict):
        insert_sql = """
        INSERT INTO youji(%s)
        VALUES (%s)
        """ % (
        ','.join([key for key, value in itemDict.items()]),
        ','.join(['%s' for key, value in itemDict.items()])
        )

        parmas = [value for key, value in itemDict.items()]
        return insert_sql,parmas
