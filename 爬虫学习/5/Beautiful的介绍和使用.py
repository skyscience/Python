# 基于lxml解析器，使用xpath
# /:
# .:
# //:
# @:
# text():
# [@id=""]:
# [@class=""]
# /li/a[1] :
# /li/a[last()] :
# title[@class="ab"] | title[@id="cd"] :

# BeautifulSoup
# pip3 install beautifulsoup4 安装
import requests
from bs4 import BeautifulSoup

#目标url
url = 'https://book.douban.com/latest?icn=index-latestbook-all'

headers = {
    'User-Agnet':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
}

response = requests.get(url, headers=headers)
print(response.status_code)
response.encoding = 'utf-8'
# with open('page.html','w') as f:
#     f.write(response.text)


soup = BeautifulSoup(response.text,'html5lib')
print(type(soup))
# print(soup.prettify())
#获取title下对应的文本
# print(soup.title.string)
#获取title标签的全部属性
# print(soup.title.attrs)
#获取title标签的class属性
# print(soup.title.attrs['class'])
# print(soup.title.name)

#使用bs4的使用最长用的是find_all：返回的是一个带有标签的列表
# li_list = soup.find_all(name='li') 
# li_list = soup.find_all('.article ul li') 
# print(len(li_list))
# print(li_list)
li_list = soup.select('.article ul li') + soup.select('.aside ul li')
print(len(li_list))
# print(li_list)
for li_tag in li_list:
    # print(li_tag)
    #获取文本信息的两种方式
    # title = li_tag.select('.detail-frame h2 a')[0].get_text()
    title = li_tag.select('.detail-frame h2 a')[0].string
    score = li_tag.select('span.font-small.color-lightgray')[0].string
    desc = li_tag.select('.detail-frame p')[2].string
    tag = li_tag.select('p.color-gray')[0].string
    image_link = li_tag.select('a.cover img')[0].attrs['src']
    print(title,score,desc,tag,image_link)

#总结：
#以下三个都是解析器：
#html5lib
#lxml
#html.parser

#beautifulsoup：也是对html/xml的解析，作用是为了从html/xml解析和提取数据
#首先构造一个soup对象
#soup.标签  
#soup.标签.string 
#soup.标签.name 
#soup.标签.attrs
#标准的格式输出一个文本perttify()
#soup.find_all(标签名、text、属性值)
#soup.find_all(class_="") #class要加下滑线，不然会冲突
#soup.find_all(id="")
#soup.find_all('标签名')
#soup.find_all(attrs=attrs{'属性名称':'属性值'})
#soup.find_all(text="要获取的文本信息")

# css语法
#  . 表示类（class）
#  # 表示id（id）
#  组合使用：
#  p.class #item li

# #获取标签的文本信息
# 标签.get_text()
# 标签.string

# #获取属性
# 标签.attrs

# 标签.attrs['href']
# 标签['href']
# 标签.get('href')









