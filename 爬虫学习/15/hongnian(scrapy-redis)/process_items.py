import redis
import pymongo
import json

def main():
    mongoclient = pymongo.MongoClient('127.0.0.1',27017)
    # mongoclient = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    rediscli = redis.StrictRedis('127.0.0.1',6379,0)

    #拿到mongodb里面的数据库
    db = mongoclient['hongniang']
    #拿数据库中的集合
    hn = db['hn']

    while True:
        source,data = rediscli.blpop(['HongNiang:items'])
        data = data.decode('utf8')
        data = json.loads(data)
        print(source, data)
        hn.insert(data)


if __name__ == '__main__':
    main()


