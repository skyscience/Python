# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

#twisted是一个异步的网络框架，这里可以帮助我们实现异步将数据插入数据库
#adbapi里面的子线程会去执行数据库的阻塞操作，当一个线程执行完毕之后，同时，原始线程能继续进行正常的工作，服务其他请求。

from twisted.enterprise import adbapi


#异步插入数据库
class ZhilianprojectPipeline(object):

    def __init__(self,dbpool):
        self.dbpool = dbpool

    #使用这个函数来应用settings配置文件。
    @classmethod
    def from_settings(cls,settings):
        parmas = {
            'host':settings['MYSQL_HOST'],
            'user':settings['MYSQL_USER'],
            'passwd':settings['MYSQL_PASSWD'],
            'db':settings['MYSQL_DB'],
            'port':3306,
            'charset':'utf8',
        }

        # **表示字典，*tuple元组,
        # 使用ConnectionPool，起始最后返回的是一个ThreadPool
        dbpool = adbapi.ConnectionPool('pymysql',**parmas)

        return cls(dbpool)

    def process_item(self, item, spider):
        #这里去调用任务分配的方法
        query = self.dbpool.runInteraction(self.insert_data_todb,item,spider)
        #数据插入失败的回调
        query.addErrback(self.handle_error,item)


    #执行数据插入的函数
    def insert_data_todb(self,cursor,item,spider):
        insert_str,parmas = item.insertdata()
        cursor.execute(insert_str,parmas)
        print('插入成功')

    def handle_error(self,failure,item):
        print(failure)
        print('插入错误')
        #在这里执行你想要的操作

    def close_spider(self, spider):
        self.dbpool.close()



# class ZhilianprojectPipeline(object):
#
#     #这里是同步的方式将数据插入数据库
#     def __init__(self):
#         self.client = pymysql.Connect('localhost','root','ljh123456','zhilian',3306,charset='utf8')
#         self.cursor = self.client.cursor()
#
#     def process_item(self, item, spider):
#         print(item)
#         #这里我们将数据库语句，写入在item里面
#         insert_str,parmas = item.insertdata()
#         self.cursor.execute(insert_str,parmas)
#         self.client.commit()
#
#         return item
#
#     def close_spider(self,spider):
#         self.cursor.close()
#         self.client.close()

