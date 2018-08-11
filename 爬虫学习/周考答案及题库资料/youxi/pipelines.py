# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class YouxiPipeline(object):

    def __init__(self,MONGODB_HOST,MONGODB_PORT,MONGODB_DB):
        self.mongoCli = pymongo.MongoClient(MONGODB_HOST, MONGODB_PORT)
        self.db = self.mongoCli[MONGODB_DB]


    @classmethod
    def from_settings(cls,settings):
        MONGODB_HOST = settings['MONGODB_HOST']
        MONGODB_PORT = settings['MONGODB_PORT']
        MONGODB_DB = settings['MONGODB_DB']

        return cls(MONGODB_HOST,MONGODB_PORT,MONGODB_DB)

    def process_item(self, item, spider):

        self.db[item.get_collection_name()].insert(dict(item))

        return item

    def close_spider(self,spider):
        self.mongoCli.close()
