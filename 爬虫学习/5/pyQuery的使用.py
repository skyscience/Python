#pyquery的使用
# import pyquery.PyQuery as pq
from pyquery import PyQuery as pq
import requests

#目标url
url = 'https://www.zhihu.com/'
# html = pq(url)
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
    # 'Cookie':'d_c0="AECkByAjvQ2PTmlOAlzqwO-0CyLnCWYog08=|1528811082"; q_c1=ab62e2d9152a42478ffdff1dbe2fb5bd|1528811082000|1528811082000; _zap=8f6d1299-47ba-4dac-8730-561430540886; tgw_l7_route=170010e948f1b2a2d4c7f3737c85e98c; _xsrf=b14aa88a-a5b0-4601-a46c-08557e77adb2',
}
response = requests.get(url,headers=headers)
print(response.status_code) 
response.encoding = 'UTF-8'
pq = pq(response.text)
# print(pq.html())
# print(pq('p'))
# print(pq.find('p'))
# print(pq.items('p'))
# for item in pq.items('p'):
#     print(item)
# list = pq.filter('.Card.HomeMainItem')
# Card HomeMainItem
#将获取到的网页，放在本地文件中
# with open('zhihu.html','w') as f:
#     f.write(response.text)
list = pq('div.Card.HomeMainItem')
print(len(list))
#如果使用pyquery取出来的标签，我们如果直接遍历的话，是<class 'lxml.html.HtmlElement'>对象
# HtmlElement不能直接使用css语法，这个时候我们必须在返回的结果后面加一个items(),来便利这个时候
# 是一个pyquery.pyquery.PyQuery，这时候我们就可以使用css语法。
for div in list.items():
    print(type(div))
    from_title = div('.Popover div').eq(0).text() 
    rich_text = div('.RichText.ztext.AuthorInfo-badgeText').text()
    title = div('.ContentItem-title div a').text()
    desc = div('span.RichText.ztext.CopyrightRichText-richText').text()
    agree_num = div('button.Button.VoteButton.VoteButton--up').text()
    comment_num = div('button.Button.ContentItem-action.Button--plain.Button--withIcon.Button--withLabel').eq(0).text()
    print(from_title,rich_text,title,desc,agree_num,comment_num)

