#get  请求
#post 请求

# post请求是把铭感的参数放在表单里面from_data,
# 误区，post请求后面不一定没有参数。

#倒入模块包，起个别名
import urllib.request as request
import urllib.parse as parse
import ssl

url = 'https://httpbin.org/post'

#发起post请求要构造表单数据
from_data = {
    'name':'某某某',
    'class':'204',
    'age':18,
    'sex':1,
}

#post请求在给服务器传参数的时候，
# 1.首先要使用urlencode编码
# 2.最后传的参数一定是一个字节类型的
#1.首先要使用urlencode编码
# from_data = parse.urlencode(from_data)
# print(from_data) # kye1=value1&kye2=value2&kye3=value3
# from_data = from_data.encode('utf-8')
# # #2.最后传的参数一定是一个字节类型的
# print(from_data)
# print(type(from_data))

#在最外层加bytes是为了强制转换
print(parse.urlencode(from_data,encoding='utf-8').encode('utf-8'))
# from_data = bytes(parse.urlencode(from_data).encode('utf-8'))
# {"args":{},
# "data":"",
# "files":{},
# "form":
# {
# "age":"18",
# "class":"204",
# "name":"\u67d0\u67d0\u67d0",
# "sex":"1"
# },
# "headers":
# {"Accept-Encoding":"identity",
# "Connection":"close",
# "Content-Length":"55",
# "Content-Type":"application/x-www-form-urlencoded",
# "Host":"httpbin.org",
# "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0"},
# "User-Agent":"Python-urllib/3.6" :如果你不设置uesr-agent，那默认的UA：Python-urllib/3.6，一般会被认为是爬虫
# "json":null,
# "origin":"61.148.243.200",
# "url":"https://httpbin.org/post"}
# print(from_data)

# headers = {
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
# }
#构造一个post请求
context = ssl._create_unverified_context()
req = request.Request(url,data=from_data,method="POST")
response = request.urlopen(req,context = context) 
# print(response.read().decode('utf-8'))





