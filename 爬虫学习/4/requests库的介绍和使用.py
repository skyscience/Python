# 1.requests:虽然Python的标准库中 urllib 模块已经包含了平常
# 我们使用的大多数功能，但是它的 API 使用起来让人感觉不太好，
# 而 Requests 自称 “HTTP for Humans”，说明使用更简洁方便。

#如何使用？
import requests

#首先发起一个get请求
#https://movie.douban.com/subject_search?search_text=成龙&cat=1002
params = {
    'search_text':'成龙',
    'cat':1002,
}
#如果使用requests需要先使用 urlencode() 将参数转换为url的编码格式
# 1.如果我们要设置一个headers
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0'
}

#  :param method: method for the new :class:`Request` object.
#     :param url: URL for the new :class:`Request` object.
#     :param params: (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`.
#     :param data: (optional) Dictionary or list of tuples ``[(key, value)]`` (will be form-encoded), bytes, or file-like object to send in the body of the :class:`Request`.
#     :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
#     :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
#     :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
#     :param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
#         ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
#         or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content-type'`` is a string
#         defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
#         to add for the file.
#     :param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth. #使用auth = (user,passsword)
#     :param timeout: (optional) How many seconds to wait for the server to send data
#         before giving up, as a float, or a :ref:`(connect timeout, read
#         timeout) <timeouts>` tuple.设置响应超时 timeout = 3,
#     :type timeout: float or tuple (2,5)
#     :param allow_redirects: (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to ``True``.
#     :type allow_redirects: bool : # allow_redirects是否允许重定向Defaults to ``True``.
#     :param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
#     :param verify: (optional) Either a boolean, in which case it controls whether we verify
#             the server's TLS certificate, or a string, in which case it must be a path
#             to a CA bundle to use. Defaults to ``True``.
#     :param stream: (optional) if ``False``, the response content will be immediately downloaded.
#     :param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
#     :return: :class:`Response <Response>` object
#     :rtype: requests.Response

#加入出现ssl错误，说明我们请求的网站使用的是自己创建的证书，也就是使用的未授权的证书。verify=False 就可以忽略未授权的ssl证书
#params：get请求时传递参数（查询参数）
#headers：设置请求头
#verify=False：忽略未授权的ssl（也就是未认证的CA证书）
response = requests.get('https://movie.douban.com/subject_search',params=params,headers=headers,verify=False)
print(response.status_code)
print(response.url)

#如何构造一个post请求
from_data = {
    'data1':'value1',
    'data2':'value2',
    'data3':'value3',
}
#data:参数用来提交表单数据，不用再经过转化了
# response = requests.post('https://httpbin.org/post',data=from_data)
# print(response.status_code)
# #urllib.read()方法返回的是二进制数据，
# print(response.text) #返回是解码后的字符串
# print(response.content) #返回的是二进制数据
# print(response.headers) #获取响应头
# print(response.headers['Connection']) #获取响应头的某一个参数


#如何使用代理？
# proxies = {
#     'http':'1270.0.0.1:8080',
#     'https':'1270.0.0.1:8080',
# }
# #proxies :这个参数是设置代理，proxies是一个字典类型的数据
# response = requests.get('https://movie.douban.com/subject_search',params=params,headers=headers,verify=False,proxies=proxies)
# print(response.status_code)
# print(response.url)


#使用cookies
# response = requests.get('https://movie.douban.com/subject_search',params=params,headers=headers,verify=False)
# print(response.status_code)
# print(response.url)
# print(response.cookies) #返回的是一个RequestsCookieJar对象，里面有cookie参数
# #如何将RequestsCookieJar对象转换为一个字典
# cookie_dict = requests.utils.dict_from_cookiejar(response.cookies)
# print(type(cookie_dict),cookie_dict)

#如何设置一个cookies(已知)
# cookies = {
#     'bid':'yTyQEkmXdBE',
# }
# response = requests.get('https://movie.douban.com/subject_search',cookies=cookies,params=params,headers=headers,verify=False)
# print(response.status_code)
# print(response.url)
# print(response.cookies) #返回的是一个RequestsCookieJar对象，里面有cookie参数
#如何将RequestsCookieJar对象转换为一个字典

#如何维持一个会话（）
#构造一个session对象，来维持会话，他会保存cookies，然后下次发起请求的时候会携带cookie
# session = requests.session()
# from_data = {
#     'email':'18518753265',
#     'password':'ljh1990123'
# }
# #发起一个post 请求，登陆成功后将cookie保存在session中
# response = session.post('http://www.renren.com/PLogin.do',data=from_data,headers=headers)
# #登陆成功之后,再使用session发起请求，这时候会挟带登陆成功后返回的cookies
# response = session.get('http://www.renren.com/965722397/profile')
# #打印请求状态
# print(response.status_code)

#可以使用post进行文件的上传,
# files = [{
#     'file':open('postdata.txt','rb'),
# },
# {
#     'file':open('postdata.txt','rb'),
# },
# {
#     'file':open('postdata.txt','rb'),
# },
# ]
# response = requests.post('https://httpbin.org/post',files=files)
# #有时候我们使用response.text也会出现乱码的情况，(utf-8\GBK)
# response.encoding = 'utf-8' 
# print(response.status_code)
# print(response.text)

#下载图片
# response = requests.get(
#     'https://img3.doubanio.com/view/celebrity/s_ratio_celebrity/public/p694.jpg',
#     headers=headers,
#     )
# print(response.status_code)
# with open('foo.jpg','wb') as f:
#     f.write(response.content)
#上传图片
# url = 'https://httpbin.org/post'
# multiple_files = [
#         ('images', ('foo.jpg', open('foo.jpg', 'rb'), 'image/jpg')),
#         ]
# r = requests.post(url, files=multiple_files)
# print(r.text)

# requests.delete
# requests.put
# 最后都是调用的requests.request()

#获取百度新闻本地新闻类标（是一个ajax请求，返回的是json数据）
#http://news.baidu.com/widget?id=LocalNews&ajax=json&t=1531104430743
url = "http://news.baidu.com/widget?id=LocalNews&ajax=json&t=1531104430743"
response = requests.get(url,headers=headers)
response.encoding = 'utf-8'
# print(response.text)
print(response.json())
# response.json(),在内部直接将json字符串，转换成了python数据类型的对象
print(type(response.json()))










 






