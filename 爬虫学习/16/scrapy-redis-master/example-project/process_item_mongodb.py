import redis
import pymongo
import json

def get_redis_data():
    #创建一个ｒｅｄｉｓ数据库的连接
    redisCli = redis.StrictRedis('192.168.1.111',port=6379,db=0)

    #创建一个ｍｏｎｇｏｄｂ的数据库连接
    mongoCli = pymongo.MongoClient('127.0.0.1',27017)

    #创建数据库
    jobboledb = mongoCli['jobboledb']

    #创建集合
    article = jobboledb.article

    while True:

        source,data = redisCli.blpop('myspider_redis:items')

        print(source,data.decode('utf-8'))
        data = json.loads(data.decode('utf-8'))

        article.insert(data)

        try:
            print("Processing: %(name)s <%(link)s>" % data)
        except KeyError:
            print("Error procesing: %r" % data)


if __name__ == '__main__':
    get_redis_data()

