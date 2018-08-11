#https://www.douban.com/search?q=美剧

#self._output(request.encode('ascii'))这个错误残生的原因是
#因为我们的请求里面带有中文
# https://www.douban.com/search?q=%E7%BE%8E%E5%89%A7
import urllib.request
import urllib.parse
import ssl

dict = {
    'q':'美剧',
}
#是将这个中文参数，转化为url的编码格式
#query必须是一个字典类型的数据
context = ssl._create_unverified_context()
q = urllib.parse.urlencode(query=dict,encoding='utf-8')
print(q)
url = 'https://www.douban.com/search?'+ q
print(url)
#urllb.request.Request:构造一个请求对象
#要实现一个携带header的请求，urlopen方法就不能满足了
#这事我们需要构造一个请求对象
#Request可以携带的参数如下：
#  url, 这是是目标url
#  data=None, post请求设置参数的位置
#  headers={},请求头
#  origin_req_host=None, 请求的远端的host
#  unverifiable=False,#：
#  method=None 请求的方法
#这里是构造一个带有氢气头的请求的对象
#构建一个请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0'
}
req = urllib.request.Request(url,headers=headers)
#根据构造的请求对象发起请求，获取响应
response = urllib.request.urlopen(req,context = context)

#这是直接根据url发起的请求，获取响应
response = urllib.request.urlopen(url,context = context)
print(response.status)

#将获取的网站源码保存在本地，做持久化
with open('douban.html','w') as f:
    f.write(response.read().decode('utf-8'))

