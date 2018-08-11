# -*— coding：UTF-8 -*-
import urllib.request
import RandomIPhandler
import ssl
import logging
import requests
handler = RandomIPhandler.RandomIPhandler()
ip = handler.get_random_ip()
print(ip)
proxy = ip[3]+'://'+ip[1]+":"+ip[2]
print(proxy)
proxy_handler = urllib.request.ProxyHandler({ip[3]:proxy}) 
context = ssl._create_unverified_context()
opener = urllib.request.build_opener(proxy_handler,urllib.request.HTTPSHandler(context=context,debuglevel=1))
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
}
req = urllib.request.Request('https://www.jianshu.com/p/a5cb4070e733',headers=headers)
response = opener.open(req)
# print(response.code)
# print(response.msg)
with open('baidu.html','w') as f:
    f.write(response.read().decode('utf-8'))

# response = requests.get(url,proxies={ip[3]:proxy})



