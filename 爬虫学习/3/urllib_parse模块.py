#urllib.parse:对url进行解析、合并、拆分、编码
import urllib.parse as parse

url = 'https://www.readnovel.com/book/9500446903583303#Catalog'
#duiurl进行解析
result = parse.urlparse(url)
print(result)
# scheme:协议
# netloc：域名
# path：资源路径
# params：参数
# query：查询条件
# fragment：锚点，相当于一个定位，假如有锚点，那么你在访问url的时候，会跳到指定位置
# ParseResult(scheme='https', netloc='www.readnovel.com', path='/book/9500446903583303', params='', query='', fragment='Catalog')

#url的拼接
#components:是一个list
# components = ('https','www.readnovel.com','/book/9500446903583303','','','Catalog')
# result = parse.urlunparse(components)
# print(result)

#urlencode
form_data = {
    'name':'scbcbwdc',
    'age':18,
    'sex':1,
}
#如果是get请求，到这一步就可以了
#form_data = parse.urlencode(form_data,encoding='utf-8')
#如果是post请求
form_data = parse.urlencode(form_data).encode('utf-8')
print(form_data)

# parse.parse_qs()将b'name=scbcbwdc&age=18&sex=1'转回为字典类型,
# 不过字典中的数据是字节类型（bytes）类型
result = parse.parse_qs(form_data)
print(result)
for name,value in result.items():
    print(name.decode('utf-8'))
    print(value[0].decode('utf-8'))




#parse.urljoin(部分拼接)
# base_url = 'https://www.readnovel.com/book/9500446903583303#Catalog'
# sub_url = '//www.readnovel.com/novel/12345.html'
# result = parse.urljoin(base_url,sub_url)
# print(result)


