import urllib.request as request
import re,base64
#目标url
url = 'http://et.airchina.com.cn/dynamicAd/GetAdvert//LowFareSearchPageSpecialsAdvert_zh_CN_new.acejson?origin=PEK&callback=jsonp1530867153531'

#构建一个http_handler处理器对象
http_handler = request.HTTPHandler()

proxy_handler = request.ProxyHandler({'http':'47.96.133.122:16816'})
#用户名和密码(私密代理/独享代理)
username = "2295808193"
password = "6can7hyh"

#构建一个opener
opener =  request.build_opener(http_handler)

#使用bs64进行编码
# proxy_Authorization = base64.b64encode(('%s:%s' % (username, password)).encode('utf-8')).decode('utf-8')
# print(proxy_Authorization)

# #构建一个请求
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
    # 'Proxy-Authorization':'Basic ' + proxy_Authorization,
} 

req = request.Request(url,headers=headers)

response = opener.open(req) 

#出发城市、到达城市、价格、日期
pattern = re.compile('<tr.*?evenTr.*?tableTdSearch.*?>(.*?)</td>.*?tableTdSearch.*?>(.*?)</td>.*?<b.*?>(.*?)</b>.*?tableTdSearch.*?>(.*?)</td>',re.S)
html = response.read().decode('utf-8')
print(html)

with open('deatil.html','w') as f:
    f.write(html)

result = re.findall(pattern,html)
print(response.status)
print(result)