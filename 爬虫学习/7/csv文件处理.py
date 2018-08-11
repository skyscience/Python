# csv:其实就是一种数据保存的格式，每个字段之间，以逗号分割，
# 有头部
import csv

list = [
    {'name':'fxm','class':201,'age':20,'hight':175},
    {'name':'zy','class':201,'age':22,'hight':180},
    {'name':'zzh','class':201,'age':24,'hight':180},
    {'name':'ltt','class':201,'age':21,'hight':160},
    {'name':'xnsk','class':201,'age':22,'hight':180},
    {'name':'ssc','class':201,'age':22,'hight':180},
    {'name':'asjkx','class':201,'age':22,'hight':180},
    {'name':'sncsl','class':201,'age':22,'hight':180},
]

#将数据写入csv文件
csvfile = open('204.csv','w')
#构建头部的参数
fieldnames = ['name','class','age','hight']
writehandler = csv.DictWriter(csvfile,fieldnames=fieldnames)
#写入一个csv文件的头部
writehandler.writeheader()
# for dict in list:
#     但行写入
#     writehandler.writerow(dict)
#多行写入
writehandler.writerows(list)
#关闭文件
csvfile.close()

#csv文件的读取
csvfile = open('204.csv','r')
reader = csv.reader(csvfile)
for line in reader:
    print(line)

