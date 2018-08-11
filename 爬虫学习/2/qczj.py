import urllib.request as request
import ssl,re
#获取汽车之家全部分账列表的第一页内容
url = 'https://www.autohome.com.cn/all/1/#liststart'

headers = {
    'User-Agnet':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
}

req = request.Request(url,headers=headers)
response = request.urlopen(req,context=ssl._create_unverified_context())

print(response.status)
html = response.read().decode('gbk')
# print(response.read().decode('gbk'))

# <div class="article-pic">
# <img src="//www2.autoimg.cn/newsdfs/g27/M01/B0/D2/120x90_0_autohomecar__ChcCQFs9yKeAVHqUAAFjKc2HYQs021.jpg">
# </div>
# <h3>...</h3>

#根据想要提取的数据找到规律来写正则
pattern = re.compile('div.*?class="article-pic".*?<img.*?src="(.*?)".*?<h3>(.*?)</h3>',re.S)

result = re.findall(pattern,html) 
# print(result)
for i in result:
    print(i)
    full_image_url = 'https:'+i[0]
    file_name = i[1]
    headers = {
        'User-Agnet':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
    }
    req = request.Request(full_image_url,headers=headers)
    response = request.urlopen(req,context=ssl._create_unverified_context())
    print(response.status)
    image_data = response.read()
    with open('qichezhijia/'+ file_name+'.jpg' ,'wb') as f:
        f.write(image_data)








