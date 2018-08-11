# -*- coding:utf-8 -*- 
# 1.爬虫基本流程
# 1）确定目标url
# 2）发起请求，接收响应
# 3）跟你你需要的字段，提取数据
# 4）将获取目标数据做持久化存储（写入文件、写入数据库（mysql、redis、mongodb））
# 服务器返回的响应有：响应的状态码、响应头、响应体

# urllib：这是python自带的一个模块（包），他能够帮助我们实现，发起请求，获取响应。
# urllib.request : 这个模块其实实现构造请求，发起请求，获取响应。
# urllib.parse : 这个模块是帮助我们处理url的，使用这个模块可以解析、拼接url，以及做序列化。
# urllib.error : 这个模块是帮助我们处理请求、或者链接的错误，其实就是容错的一个处理

#今天：我们要实现的是构造请求（post、get请求）

#目标url
#https://www.baidu.com/baidu?tn=monline_3_dg&ie=utf-8&wd=%E6%95%B0%E6%8D%AE%E5%A0%82

import urllib.request
#关于https中的证书处理
import ssl
# urlopen(url,  表示你要获取数据的目标url
# data=None, #如果是get请求，那么data参数默认为None，如果是post请求，你就需要去设置data参数
# timeout=socket._GLOBAL_DEFAULT_TIMEOUT, 设置响应超时的时间单位是秒
# cafile=None, #设置证书文件的地方，
# capath=None,  #设置证书路径的地方

# context=None) #context 其实在这里假如设置了参数，那么就会忽略ssl证书，
# 假如你的目标url是一个http的请求，是不需要设置这个参数的，假如是https的
# 请求那么我们需要设置这个参数

#cadefault：这个参数表示是否使用默认的证书，默认为false，不使用

#urlopen()方法内部其实就是帮助我们实现了发送请求、返回响应结果
#urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:833)如果报这个错误，说明我们的证书不对
#这个表示不去认证ssl(不去做证书认证)
context = ssl._create_unverified_context()
url = 'http://www.baidu.com/baidu?tn=monline_3_dg&ie=utf-8&wd=%E6%95%B0%E6%8D%AE%E5%A0%82'
response = urllib.request.urlopen(url,context=context)
#直接使用response.read()返回的数据类型b'的字节类型
#print(response.read())
#这里对b'的字节类型进行了转码，是将utf-8编码格式，转换成unicode。
#print(response.read().decode('utf-8'))
# decode：转码，将其他类型的编码，转换成unicode编码
# encode：编码，是将unicode类型的编码，转为其他类型的编码

#获取响应状态(如果返回200表示请求成功，400:请求错误，
# 401:未认证，403：拒绝访问，权限不够，404:找不到页面，500:服务器错误)
print(response.status)

#获取响应头头部信息表示获取所有的响应头信息
# print(response.getheaders())

#获取某一个响应头信息
print(response.getheader('Content-Type'))