# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs


qk = codecs.open('test1.json', 'w', encoding='utf-8')
qk.write('')

class Test1Pipeline(object):
    def __init__(self):
        


        # 创建文件
        self.file = codecs.open('test1.json', 'a+', encoding='utf-8')
        self.file.write('{')
    

    
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        print('item====',item['student'])
        self.file.write('"'+item['student']+'":'+line+',')
        # print('"d":'+line+',')
        return item


    def spider_closed(self, spider):
        self.file.close()
  
        
end = codecs.open('test1.json', 'a+', encoding='utf-8')
end.write('"0":{"null":"null"}'+'}')
