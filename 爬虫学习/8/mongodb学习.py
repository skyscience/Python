1.关系型数据库：mysql 、sqlit
2.非关系型数据库：redis、mongodb

#mongodb：
# sudo service mongodb start
# sudo service mongodb stop
# sudo service mongodb restrat

# mongo 启动客户端服务
# show dbs 查看所有的数据库
# db 查看当前的数据库
# use 数据库名称  （没有集合或数据时不显示）
# db.createCollection('集合名称')  创建集合
# db.集合名称.insert({'':''}) 
# db.集合名称.insert([{'':''},{'':''}])
# db.集合名称.find(条件) #返回所有符合条件的结果
# db.集合名称.remove(条件) #删除所有符合条件的结果
# db.集合名称.find(条件).skip(2) 从查询结果的第二条开始返回
# db.集合名称.find(条件).limit(2) 返回查询结果返回2条数据
# db.集合名称.find(条件).limit(2).skip(2) 跳过前两条，返回后两条（limit、skip谁前谁后都可以）
# db.集合名称.drop()  表示删除集合
# db.dropDatabase() 表示删除当前数据库
# db.集合名称.update({条件},{'$set':{替换的条件}})
# db.集合名称.find().count() 表示获取集合中文本的数量
# db.books.save({}）#有更新和保存的功能(如果插入的文档（_id）与集合文档中的数据（_id）如果一致，会更新文档)，如果不一致，会重新插入一条数据
# db.books.find({},{'_id':0,'name':0}),表示查询结果，可以不返回_id和name字段（0:表示隐藏，1:表示显示）

