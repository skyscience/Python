import urllib.request as request
import urllib.parse as parse
import ssl,re
import os


for i in range(1,33):
    i=str(i)
    url = 'https://www.readnovel.com/rank/hotsales?pageNum='+i
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5478.400 QQBrowser/10.1.1550.400'
    }
    req = request.Request(url,headers=headers)
    response = request.urlopen(req,context=ssl._create_unverified_context())
    html = response.read().decode('utf-8')
 
 
 
    pattern = re.compile('div.*?class="book-img-box".*?<a.*?<img.*?src="(.*?)">.*?<div.*?class="book-mid-info">.*?h4>.*?<a.*?">(.*?)</a>.*?<p.*?class="author">.*?<a.*?>(.*?)</a>.*?<em>.*?<a.*?>(.*?)</a>.*?<em>.*?<span>(.*?)</span>.*?<p.*?class="intro">(.*?)</p>.*?<p.*?class="update">.*?<a.*?>(.*?)</a>.*?<em>.*?<em>.*?<span>.*?</span>.*?</p>.*?</div>',re.S)
    result = re.findall(pattern,html)
    for i in result:
        title = i[1]
        os.mkdir('第二天/'+'book/'+title)
        image_url = 'https:'+i[0]
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5478.400 QQBrowser/10.1.1550.400'
        }
        req = request.Request(image_url,headers=headers)
        response = request.urlopen(req,context=ssl._create_unverified_context())
        image_data=image_data = response.read().decode('utf-8')
        with open('第二天/'+'book/'+title+'/'+title +'.jpg' ,'wb',encoding='utf-8') as f:
            f.write(image_data)
        with open('第二天/'+'book/'+title+'/'+title +'.txt','w') as o:
            o.write('书名:'+i[1]+'\n'+'作者:'+i[2]+'\n'+'分类:'+i[3]+'\n'+'状态:'+i[4]+'\n'+'预览:'+i[5])