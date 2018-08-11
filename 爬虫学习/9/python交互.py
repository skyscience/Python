import pymongo

#创建客户端链接
mogoClient = pymongo.MongoClient('127.0.0.1',27017)
# ｍogoClient = pymongo.MongoClient('localhost',27017)
# ｍogoClient = pymongo.MongoClient('mongodb://127.0.0.1:27017')

#取数据库
db = mogoClient.student
# db = mogoClient['student']

#获取数据库中的集合
info = db.info
#info = db['info']

#设置字段
document = {
    'name':'zhangsan',
    'gender':1,
    'age':20,
}

#设置字段
document1 = {
    'name':'zhangsan1',
    'gender':1,
    'age':20,
}

#设置字段
document2 = {
    'name':'zhangsan2',
    'gender':0,
    'age':20,
}

#　单条插入和多条插入
# reslut = info.insert(document)
# reslut = info.insert([document,document1,document2])
# print(reslut)
# result = info.insert_many([])

#返回一条数据，这时返回的是一个文本
# result = info.find_one()
# print(result)

#查找集合中的数据，返回的是一个cursor对象
# result = info.find() #<pymongo.cursor.Cursor object at 0x7f8fdb566748>
# # #通过遍历获取<pymongo.cursor.Cursor object at 0x7f8fdb566748>里面的数据
# for item in result:
#     print(item)
# print(result)

#修改第一条符合条件的数据
# reslut = info.update({'name':'zhangsan'},{'$set':{'age':10,'gender':0}})
# print(reslut)

#修改所有符合条件的数据
# reslut = info.update_many({'name':'zhangsan'},{'$set':{'age':0,'gender':1}})
# print(reslut)

#　条件查询，返回的是一个cursor对象，
# reslut = info.find({'name':'zhangsan'})
# print(reslut)
# 遍历查询结果
# for item in reslut:
#     print(item)


# reslut = info.save({'_id':'5b4c60ed11575e7bb6534320','name':'lisi'})
#ObjectId('5b4c60ed11575e7bb6534320')
objId = str(ObjectId('5b4c60ed11575e7bb6534320'))
reslut = info.save({'_id':objId,'name':'lisi'})


# # 分页查询
# reslut = info.find().limit(1).skip(2)

# # 根据ａｇｅ字段降序排列
# result = info.find().sort('age',-1)
# # 根据ａｇｅ字段升序排列
# result = info.find().sort('age',1)

