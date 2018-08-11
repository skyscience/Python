import pymysql
import redis
import json

def get_redis_data():
    #创建数据库连接
    redisCli = redis.StrictRedis('192.168.1.111',6379,db=0)
    mysqlCli = pymysql.Connection('127.0.0.1','root','ljh1314','jobbole',3306,charset='utf8')
    cursor = mysqlCli.cursor()
    while True:
        source,data = redisCli.blpop('myspider_redis:items')
        print(source.decode('utf-8'),data.decode('utf-8'))
        data = json.loads(data.decode('utf-8'))
        insert_sql, parmas = insert_data(data)
        cursor.execute(insert_sql,parmas)
        mysqlCli.commit()
        # cursor.close()


def insert_data(data):
    insert_sql = """
    INSERT INTO article(%s) values(%s)
    """ % (','.join([key for key,value in data.items()]),
           ','.join(['%s' for key,value in data.items()]))

    print(insert_sql)

    parmas = [value for key,value in data.items()]

    return insert_sql,parmas


if __name__ == '__main__':
    get_redis_data()
