# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class HrtencentPipeline(object):
    # 可选实现，做参数初始化等
    def __init__(self):
        self.file = open("hrtencent.json", 'w')


    # 这个方法必须实现，每个item pipeline组件都需要调用该方法，
    # 这个方法必须返回一个 Item 对象，被丢弃的item将不会被之后的pipeline组件所处理。
    def process_item(self, item, spider):
        jsontext = json.dumps(dict(item), ensure_ascii=False)+"\n"
        self.file.write(jsontext)
        return item


    # 可选实现，当spider被关闭时，这个方法被调用
    def close_spider(self, spider):
        self.file.close()
