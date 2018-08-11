# xml:注重的是数据的存储，它的标签你可以自己定义，取值的时候根据标签去取值
# <a>2</a>
# <b>1</b>
# html:注重的是数据的展示，每个标签都有自己的含义，不能自己定义标签
#要使用xpath，首先要倒入lxml库：lxml是一个解析器，能够解析xml/html文档
#要使用它，首先要pip3 install lxml

#案例：
#利用xpath语法提取小说阅读网的数据
#不同的页码，这是pageNum发生了变化
import requests
from lxml import etree
import json

url = 'https://www.readnovel.com/finish?pageSize=10&gender=2&catId=-1&isFinish=1&isVip=-1&size=-1&updT=-1&orderBy=0&pageNum=2'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
}
response = requests.get(url,headers=headers)
print(response.status_code)
# print(response.text)

#1.首先使用etree将获取到的html文本转换成htmldom（文档模型对象）
html = etree.HTML(response.text)
print(type(html))

novel_list = html.xpath('//div[@class="right-book-list"]/ul/li')
print(type(novel_list))
print(len(novel_list))
print(novel_list)
for li in novel_list:
    #图片链接
    image_url = li.xpath('./div[@class="book-img"]//img/@src')[0]
    #小说的标题
    title = li.xpath('./div[@class="book-info"]/h3/a/text()')[0]
    #作者名称
    author = li.xpath('./div[@class="book-info"]/h4/a/text()')[0]
    #标签
    tags = ','.join(li.xpath('.//p[@class="tag"]/span/text()'))
    #描述
    desc = li.xpath('.//p[@class="intro"]/text()')[0]
    # print(image_url,title,author,tags,desc)
    dict = {
        'image_url':image_url,
        'title':title,
        'author':author,
        'tags':tags,
        'desc':desc
    }
    # print(dict)
    with open('xiaoshuo.json','a') as f:
        f.write(json.dumps(dict,ensure_ascii=False) + '\n')


# nodename： 获取所有符合节点名称的节点（标签）
# / ：从根节点开始获取
# // ：无论节点在任何位置，使用//都能将其匹配出来。
# . ：从当前节点获取
# @ ：用来获取属性值
# text():表示获取标签文本



