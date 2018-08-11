#cookies作用：http是一个无状态的请求，如果要位置回话
#就需要cookie和session，cookies是服务为了辨别用户身份信息的
#一般是放在浏览器中，里面的数据一般都是经过加密的。
#在爬虫中我们一般使用cookie来模拟用户登陆

#1.最不动脑的方法，我们直接在浏览器中登陆，然后在浏览器中找到cookie
#直接放在我们的请求头中

#2.寻找登陆的接口，然后分析登陆时需要在接口中传递的参数，模拟表单数据，发请请求，等待响应了

#1，如何获取cookies？

import http.cookiejar as cookiejar
import urllib.request as request
import urllib.parse as parse

# #构建一个cookiesjar对象，用来保存cookie
# cookieJar = cookiejar.CookieJar()
# #构建一个cookie_handler处理器(HTTPCookieProcessor)
# cookie_hanlder = request.HTTPCookieProcessor(cookieJar)
# http_handler = request.HTTPHandler(debuglevel=1)
# #自定义一个opener
# opener = request.build_opener(cookie_hanlder,http_handler)
# url = 'http://www.baidu.com/'
# req = request.Request(url)
# response = opener.open(req)
# print(type(cookieJar))
# for cookie in cookieJar:
#     print(cookie.name,cookie.value)

#发起一个请求之后，cookieJar对象中已经缓存了cookie，下次再使用opener发起请求的时候
#会携带cookies

#cookiejar.MozillaCookieJar
# 另一种方式：使用MozillaCookieJar,可以直接设置一个文件名称，
# 获取到cookies之后，直接将cookie保存在本地文件中

# filename = 'cookie.txt'
# cookieJar = cookiejar.MozillaCookieJar(filename)
# #构建一个cookie_handler处理器(HTTPCookieProcessor)
# cookie_hanlder = request.HTTPCookieProcessor(cookieJar)
# http_handler = request.HTTPHandler(debuglevel=1)
# #自定义一个opener
# opener = request.build_opener(cookie_hanlder,http_handler)
# url = 'http://www.baidu.com/'
# req = request.Request(url)
# response = opener.open(req)
# print(type(cookieJar))
# for cookie in cookieJar:
#     print(cookie.name,cookie.value)

# #必须要调用这个save方法才能将cookie保存在本地文件中
# cookieJar.save()


#如何读取使用MozillaCookieJar读取本地cookie.txt文件
# cookieJar = cookiejar.MozillaCookieJar()
# cookieJar.load('cookie.txt')

# for cookie in cookieJar:
#     print(cookie.name,cookie.value)


#如何在模拟登陆中使用？

#目标url：http://www.renren.com/PLogin.do
# 表单里面的数据：
# {'password':'','email':''}
#1.创建一个cookiejar对象用来保存cookie
cookieJar = cookiejar.CookieJar()
#2.cookie的处理器对象
cookie_handler = request.HTTPCookieProcessor(cookieJar)
http_handler = request.HTTPHandler()
#自定义opener
opener = request.build_opener(cookie_handler,http_handler)
#目标url，一个post请求
url = 'http://www.renren.com/PLogin.do'
form_data = {
    'email':'18518753265',
    'password':'ljh1990123',
} 
#首先要使用urlencode转换为url格式的编码，然后再转成b'(bytes)
form_data = parse.urlencode(form_data).encode('utf-8') 
print(form_data)

#构造请求
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
} 
#构建一个请求对象
req = request.Request(url,data=form_data,method="POST",headers=headers)

#发起请求
response = opener.open(req)
print(response.status)

# for cookie in cookieJar:
#     print(cookie.name,cookie.value)

url = 'http://www.renren.com/965722397/profile'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
} 
#构建一个请求对象
req = request.Request(url,headers=headers)
response = opener.open(req)
print(response.status)
html = response.read().decode('utf-8')
with open('pserson.html', 'w') as f:
    f.write(html)

















#