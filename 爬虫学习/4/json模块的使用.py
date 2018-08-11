# 什么时候会用到json模块？
# 一般情况下如果网页采用ajax动态加载数据的时候，
# 会返回json数据类型，这时候我们需要将json字符串，转换为python对象
import json
import requests
#一下是模块的使用方法
# json.load:是将本地文件中的json字符串，转换为python
# json.dump:可以将python对象转为json字符串，并存储
# json.loads:可以将json字符串转为python对象
# json.dumps:可以将python对象转为json字符串
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0'
}
url = "http://news.baidu.com/widget?id=LocalNews&ajax=json&t=1531104430743"
response = requests.get(url,headers=headers)
response.encoding = 'utf-8'
data = json.loads(response.text)
print(data)
print(type(data))

# print(response.text)
#在requests中返回的respinse响应有一个json方法，跟json.loads()方法功能一致
# response.json(),在内部直接将json字符串，转换成了python数据类型的对象

# json.dump:可以将python对象转为json字符串，并存储(写入本地文件)
# 如果要保存的数据中有中文ensure_ascii=False，表示不采用ascii，使用的是utf-8编码格式
# json.dump(data,open('json_data.json','w'),ensure_ascii=False)

# json.load:是将本地文件中的json字符串，转换为python
data = json.load(open('json_data.json','r'))
# print(data)
print(type(data))
#遍历字典中的键和值
# for name,value in data.items():
#     print(name)
#     print(value)

#取值
subdata = data['data']['LocalNews']['data']['rows']
pic_news = subdata['pic']
print(pic_news)
pic_news_title = pic_news['title']
pic_news_url = pic_news['url']
pic_news_url = pic_news['time']

first_news = subdata['first']
second_news = subdata['second']
for sub_news in first_news+second_news:
    #判断数据的类型
    # type()
    # isinstance(data,tupe)
    # print(sub_news)
    print(sub_news['title'],sub_news['url'],sub_news['time'])

#json.dumps:可以将python对象转为json字符串
# json_str = json.dumps(subdata,ensure_ascii=False)
# print(type(json_str))
# print(json_str)

###注意事项：
#1.json的嵌套数据必须是object（dict）和数组（list）
#2.json数据中的数据引用必须使用双引号

