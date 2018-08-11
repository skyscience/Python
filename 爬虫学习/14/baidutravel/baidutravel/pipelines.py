# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# from scrapy.utils.project import get_project_settings
import pymongo
class BaidutravelPipeline(object):

    def __init__(self,client,sheet):

        self.client = client
        self.sheet = sheet

    @classmethod
    def from_settings(cls,settings):
        MONGODB_HOST = settings['MONGODB_HOST']
        MONGODB_PORT = settings['MONGODB_PORT']
        MONGODB_DB = settings['MONGODB_DB']
        MONGODB_COLLECTION = settings['MONGODB_COLLECTION']
        client = pymongo.MongoClient(MONGODB_HOST,MONGODB_PORT)
        sheet = client[MONGODB_DB][MONGODB_COLLECTION]
        return cls(client,sheet)

    def process_item(self, item, spider):
        self.sheet.insert(dict(item))
        return item
