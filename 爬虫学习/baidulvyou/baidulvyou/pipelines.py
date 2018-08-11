# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.conf import settings
from scrapy.exceptions import DropItem
import os,scrapy
import pymongo,pymysql,json

class BaidulvyouImagePipeline(ImagesPipeline):

    image_store = settings['IMAGES_STORE']

    def get_media_requests(self, item, info):
        image_url = item['image_url']
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        paths = [dict['path'] for status,dict in results if status]
        if not paths:
            raise DropItem('图片下载出错')
        else:
            print('图片下载成功')
            os.rename(self.image_store+'/'+paths[0],self.image_store+'/'+item['note_title']+'.jpg')
            item['image_path'] = self.image_store+'/'+item['note_title']+'.jpg'

            return item

class BaidulvyouPipeline(object):

    def __init__(self,MONGOHOST,MONGOPORT,MONGODB_DB):
        self.client = pymongo.MongoClient(MONGOHOST,MONGOPORT)
        self.db = self.client[MONGODB_DB]

    @classmethod
    def from_crawler(cls,crawler):
        MONGOHOST = crawler.settings['MONGODBHOST']
        MONGOPORT = crawler.settings['MONGODBPORT']
        MONGODB_DB = crawler.settings['MONGODB_DB']
        print(MONGOHOST,MONGOPORT,MONGODB_DB)

        return cls(MONGOHOST,MONGOPORT,MONGODB_DB)

    def process_item(self, item, spider):
        print(json.dumps(dict(item),ensure_ascii=False))
        # col = self.db['youji']
        # col.insert(json.dumps(dict(item),ensure_ascii=False))

        return item

    def close_open(self,spider):
        self.client.close()


# class BaidulvyouPipeline(object):
#
#     def __init__(self,MYSQLHOST,MYSQLUSER,MYSQLPWD,MYSQLDB,MYSQLPORT):
#         self.client = pymysql.Connect(MYSQLHOST,MYSQLUSER,MYSQLPWD,MYSQLDB,MYSQLPORT,chrtset='utf8')
#         self.cousor = self.client.cursor()
#
#     @classmethod
#     def from_settings(cls,settings):
#         MYSQLHOST = settings['MYSQLHOST']
#         MYSQLPORT = settings['MYSQLPORT']
#         MYSQLDB = settings['MYSQLDB']
#         MYSQLUSER = settings['MYSQLUSER']
#         MYSQLPWD = settings['MYSQLPWD']
#
#         return cls(MYSQLHOST,MYSQLUSER,MYSQLPWD,MYSQLDB,MYSQLPORT)
#
#     def process_item(self, item, spider):
#         insert_sql,parmas = item.insert_sql()
#         self.cousor.execute(insert_sql,parmas)
#         self.client.commit()
#
#         return item
#
#     def close_open(self,spider):
#         self.cousor.close()
#         self.client.close()
