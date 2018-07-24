# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import pymysql

class CrawljobbolePipeline(object):
    def __init__(self,dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls,settings):
        #数据库的连接参数
        parmas = {
            'host':settings['MYSQL_HOST'],
            'user':settings['MYSQL_USER'],
            'passwd':settings['MYSQL_PWD'],
            'db':settings['MYSQL_DB'],
            'port':settings['MYSQL_PORT'],
            'charset':'utf8',
        }
        print(parmas)
        # 一个*表示元组，**表示字典
        #这里创建了一个连接池
        dbpool = adbapi.ConnectionPool('pymysql',**parmas)
        return cls(dbpool)

    def process_item(self, item, spider):
        #让连接池执行数据插入任务，并传递参数
        query = self.dbpool.runInteraction(self.insert_data_to_db,item,spider)
        # #添加一个数据插入失败的回调
        query.addErrback(self.handle_err,item)
        return item

    def insert_data_to_db(self,cursor,item,spider):
        #使用游标执行数据插入
        insert_sql,parmas = item.insert_data(dict(item))
        print(insert_sql,parmas)
        #INSERT INTO article(publishTime,desc,commentNum,tags,title,image_url) VALUES (%s,%s,%s,%s,%s,%s) ['2018/06/17', 'Vim 插件管理器就可以派上用场。插件管理器将安装插件的文件保存在单独的目录中，因此管理所有插件变得非常容易。 ', 0, 'IT技术', 'Vim-plug：极简 Vim 插件管理器', 'http://jbcdn2.b0.upaiyun.com/2018/06/e10fe1fd7da125e34ea34b9f5dad9c30.png']
        cursor.execute(insert_sql,parmas)
        print('插入成功')

    def handle_err(self,failure,item):
        #数据插入失败的回调函数
        print(failure)
        print('数据库插入失败')

    def close_spider(self,spider):
        self.dbpool.close()






