import urllib.request as request
import ssl
import base64
# request.urlopen()
# 构建一个代理的处理器，支持代理设置
#{'http':'118.190.95.35:9000','https':'221.228.17.172:8181'}

#如何自己定义一个opener
#构建一个http_handler，来支持http请求
http_handler = request.HTTPHandler(debuglevel=1)
#构建一个https——handler，来支持https请求
context = ssl._create_unverified_context()
#debuglevel默认为0，设置为1的时候表示开启debuglevel
https_handler = request.HTTPSHandler(context=context,debuglevel=1)

#这里构建一个代理的处理器对象ProxyHandler，括号里面的参数是字典{'http':'ip:port','https':"ip:port"}
# proxy_handler = request.ProxyHandler({'http':'118.190.95.35:9000','https':'221.228.17.172:8181'})

#私密代理
#用户名：2295808193密码：6can7hyh
#47.96.133.122  16816
proxy_handler = request.ProxyHandler({'https':'47.96.133.122:16816'})
#用户名和密码(私密代理/独享代理)
username = "2295808193"
password = "6can7hyh"

#使用bs64进行编码
proxy_Authorization = base64.b64encode(('%s:%s' % (username, password)).encode('utf-8')).decode('utf-8')
print(proxy_Authorization)

#创建一个opener对象，实现发起请求
opener = request.build_opener(http_handler,https_handler,proxy_handler)
# headers = {
#     'Proxy-Authorization':'Basic ' + proxy_Authorization
# }
#在平台上添加白名单之后，可以免密使用
req = request.Request('https://www.baidu.com/')

#根据open方法发起请求
response = opener.open(req)
print(response.status)

# 如果我们做了这一步操作，作用是后面你使用urlopen的时候，
# 默认会使用你自己定义的opener
# request.install_opener(opener)
# request.urlopen()

#总结：
1.如何自定义opener？自定义opener作用？
request.urlopen()方法阿德内部实现。
2.创建了http_handler、https_handler、proxy_handler、
HTTPSHandler(context=context,debuglevel=1)
HTTPHandler(debuglevel=1)
ProxyHandler({'https':'47.96.133.122:16816'})
3.创建opener对象，目的是为了使用自定义的handler处理器，来实现我们想要的功能

4.opener.open()发起请求

5.设置代理？
1.why？为了隐藏自己的ip，在爬虫的过程中，往往ip很容易被封，这是时候我们需要伪装ip，就是使用代理
2.根据协议分类？FTP、HTTP/HTTPs、SOCKS、SSL/TSL
3.根据匿名分类：高匿代理、普通代理、透明代理、间谍代理
4.代理基本原理？
5.在哪里寻找代理？
西刺、快代理、360代理、全网代理
收费：
代理精灵、讯代理、快代理。。。。。。
6.其实在真实的爬虫过程中，往往需要去做代理池。
7.独立代理/私密代理的使用
1）需要做用户验证
2）假如要访问https类型的接口，我们要设置白名单才能访问，这时候是免密访问。


cookies:是指某些网站服务器为了辨别用户身份和进行Session跟踪，而储存在用户浏览器上的文本文件数据（通常都是经过加密的），Cookie可以保持登录信息到用户下次与服务器的会话。

