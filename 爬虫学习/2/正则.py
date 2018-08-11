import re
# 在python的正则模块下
# 有哪些常见或者常试用的方法
# 1.re.compile():根据你的正则规则构建一个正则对象
# 2.re.findall():在全部文本中匹配出所有符合正则规则的结果
# 3.re.sub():替换
# 4.re.match:从起始位置开始匹配，如果不符合正则规则就返回None，
# 如果符合就立即返回结果，一次匹配。
# 5.re.search:search是在全文中做匹配，一旦出现符合规则的就返回结果，
# 没有符合规则的就返回None，一次匹配
# 6.re.split:分割函数

string = 'href="http://www.baidu.com/link?url=vNL6sVhjtLj4y1irSb64FF5DXuhqjESSqtaQxfpNgdr90woO4srMkh7WNrC0dVrI6GYaDbFWB-soEV-3kVBciSba0r_yR-pc1zeEX-T4IKCtarget=_blank"><em>中国</em>(世界四大文明古国之一)_百度百科</a>'
# print(string)
#构建一个正则对象
# pattren = re.compile('href.*link')
# reslut = re.match(pattren,string)
# print(type(reslut))
# #取出了匹配结果
# print(reslut.group(0))

# pattren = re.compile('href="(.*?)target.*?">')
# reslut = re.findall(pattren,string)
# print(type(reslut))
# print(reslut[0])

# pattren = re.compile('href=')
# target=_blank
pattren = re.compile('target.+?')
# pattren = re.compile('target.*')
reslut = re.sub(pattren,'">',string)
print(reslut)

# pattren = re.compile('http.*>')
# reslut = re.search(pattren,string)
# print(type(reslut))
# print(reslut.group(0))

#分割
pattren = re.compile('>')
result = re.split(pattren,string)
print(type(result))
print(len(result))








