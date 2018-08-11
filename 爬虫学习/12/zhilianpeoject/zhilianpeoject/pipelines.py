# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymysql
from zhilianpeoject.items import ZhilianCompanyItem,ZhilianpeojectItem
import pymongo

# #管道文件，一般在这里做数据的清洗、筛选、持久化
# class ZhilianpeojectPipeline(object):
#     def __init__(self,MONGODBHOST,MONGODBPORT,MONGODB_DB):
#         # self.client = pymysql.Connect('localhost','root','ljh1314','zhilian',3306,charset='utf8')
#         self.client = pymongo.MongoClient(MONGODBHOST,MONGODBPORT)
#         self.db = self.client[MONGODB_DB]
#
#     @classmethod
#     def from_settings(cls,settings):
#         MONGODBHOST = settings['MONGODBHOST']
#         MONGODBPORT = settings['MONGODBPORT']
#         MONGODB_DB = settings['MONGODB_DB']
#
#         return cls(MONGODBHOST,MONGODBPORT,MONGODB_DB)
#
#
#     def open_spider(self,spider):
#         print('爬虫启动的时候会走一次')
#         ##这里执行你想要执行的代码
#
#     def process_item(self, item, spider):
#         print('管道文件我来了')
#         if isinstance(item,ZhilianpeojectItem):
#             print('职位数据插入')
#             #jobDesc
#             col = self.db['jobDesc']
#             col.insert(json.dumps(dict(item),ensure_ascii=False))
#
#
#         elif isinstance(item,ZhilianCompanyItem):
#             print('公司数据插入')
#             col = self.db['company']
#             col.insert(json.dumps(dict(item), ensure_ascii=False))
#
#         return item
#
#     def close_spider(self,spider):
#         print('爬虫结束的时候会执行')
#         ##这里执行你想要执行的代码
#         #爬虫结束后关闭游标和数据库连接
#         self.client.close()




#管道文件，一般在这里做数据的清洗、筛选、持久化
#mysql数据插入
class ZhilianpeojectPipeline(object):
    def __init__(self,MYSQLHOST,MYSQLPORT,MYSQLUSER,MYSQLPWD,MYSQLDB):
        # self.client = pymysql.Connect('localhost','root','ljh1314','zhilian',3306,charset='utf8')
        self.client = pymysql.Connect(MYSQLHOST,MYSQLUSER,MYSQLPWD,MYSQLDB,MYSQLPORT,charset='utf8')
        self.cursor = self.client.cursor()

    @classmethod
    def from_settings(cls,settings):
        MYSQLHOST = settings['MYSQLHOST']
        MYSQLPORT = settings['MYSQLPORT']
        MYSQLUSER = settings['MYSQLUSER']
        MYSQLPWD = settings['MYSQLPWD']
        MYSQLDB = settings['MYSQLDB']

        return cls(MYSQLHOST,MYSQLPORT,MYSQLUSER,MYSQLPWD,MYSQLDB)


    def open_spider(self,spider):
        print('爬虫启动的时候会走一次')
        ##这里执行你想要执行的代码

    def process_item(self, item, spider):
        print('管道文件我来了')
        #方式一：比较麻烦
        # if isinstance(item,ZhilianpeojectItem):
        #     print('职位数据插入')
        #     # insert_sql = 'INSERT INTO zhilianjob(jobtitle,salary,publishTime,workAdress,needpeople,jobDesc,companyName,companyUrl) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
        #     # self.cursor.execute(insert_sql,
        #     #                     (item['jobtitle'],item['salary'],
        #     #                      item['publishTime'], item['workAdress'],
        #     #                      item['needpeople'], item['jobDesc'],
        #     #                      item['companyName'], item['companyUrl'],)
        #     #                     )
        #     # self.client.commit()
        #
        # elif isinstance(item,ZhilianCompanyItem):
        #     print('公司数据插入')
        #     # insert_sql = 'INSERT INTO zhiliancompany(comapyName,comapnyClassfiy,companyMode,companyIndustry,companyAdress,companyDesc) VALUES(%s,%s,%s,%s,%s,%s)'
        #     # self.cursor.execute(insert_sql,
        #     #                     (item['comapyName'], item['comapnyClassfiy'],
        #     #                      item['companyMode'], item['companyIndustry'],
        #     #                      item['companyAdress'], item['companyDesc'],
        #     #                      ))
        #     # self.client.commit()

        #方式二：
        #原理，在对应的类里面写好数据库语句，然后返回数据库语句和目标数据
        #拿到后直接执行
        insert_sql,parmas = item.insert_sql()
        self.cursor.execute(insert_sql,parmas)
        return item

    def close_spider(self,spider):
        print('爬虫结束的时候会执行')
        ##这里执行你想要执行的代码
        #爬虫结束后关闭游标和数据库连接
        self.cursor.close()
        self.client.close()


# #管道文件，一般在这里做数据的清洗、筛选、持久化
# class ZhilianpeojectPipeline(object):
#     def process_item(self, item, spider):
#         print('管道文件我来了')
#         with open('zhilian.json','a') as f:
#             f.write(json.dumps(dict(item),ensure_ascii=False)+'\n')
#
#         # print(item)
#         return item

# ZhilianpeojectPipelinecustom

# class ZhilianpeojectPipelinecustom(object):
#     def process_item(self, item, spider):
#         print('管道文件我来了')
#         with open('zhilian.json','a') as f:
#             f.write(json.dumps(dict(item),ensure_ascii=False)+'\n')
#
#         # print(item)
#         return item



from scrapy.conf import settings
from scrapy.utils.project import get_project_settings

# class ZhilianpeojectPipeline(object):
#     def __init__(self):
#         # host = get_project_settings().get('MONGOHOST')
#         host = settings['MONGOHOST']
#         port = settings['MONGOPORT']
#         db = settings['MONGODB']
#         self.client = pymongo.MongoClient(host,port)
#         self.db = self.client[db]
#
#
#     def process_item(self, item, spider):
#         print('管道文件我来了')
#         if isinstance(item,ZhilianpeojectItem):
#             col = self.db.jobdesc
#             col.insert(json.dumps(dict(item),ensure_ascii=False))
#         elif isinstance(item,ZhilianCompanyItem):
#             col = self.db.company
#             col.insert(json.dumps(dict(item),ensure_ascii=False))
#
#         return item
#
#     def close_spider(self,spider):
#         self.db.close()
#
