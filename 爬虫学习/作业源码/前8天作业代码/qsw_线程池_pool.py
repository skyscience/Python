#使用python3.2之后为我们封装的线程池
from concurrent.futures import ThreadPoolExecutor
import time
import threading
import requests
import os
from lxml import etree
import re



#这个代码在获取小说列表、获取小说章节列表以及下载章节详情时候共同使用了线程池

def get_data(url):
    print('开始下载'+url)
    print(threading.current_thread().name)
    header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0'
    }
    response = requests.get(url,headers=header) 
    if response.status_code == 200:
        response.encoding = 'gbk'
        return response.text

def naveldone(future):
    #线程池执行设定任务结束后的结果参数
    print('下载完了'+ str(time.time()))
    text = future.result()
    print(text)
    #http://www.quanshuwang.com/book/161/161996
    #可以在这提取每一本书籍的连接
    html = etree.HTML(text)
    novallist = html.xpath('//ul[@class="seeWell cf"]/li')
    charpterlisturls = []
    for novel in novallist:
        title = novel.xpath('.//a[@class="clearfix stitle"]/@title')[0]
        url = novel.xpath('.//a[@class="clearfix stitle"]/@href')[0]
        pattern = re.compile(r'.*?(\d+?).html',re.S)
        id = re.findall(pattern,url)[0]
        chapterurl = 'http://www.quanshuwang.com/book/%s/%s' % (id[:3],id)
        # http://www.quanshuwang.com/book/161/161996
        # http://www.quanshuwang.com/book_161996.html
        file_path = 'novel1/'+title
        #判断当前文件夹是否存在
        if not os.path.exists(file_path):
            #如果不存在，则创建文件夹
            os.mkdir(file_path)
        #将小说章节页面连接放在一个数组中
        charpterlisturls.append(chapterurl)
    add_chapterpool(charpterlisturls)
    #获取到书籍之后，这时候要去寻找章节列表,根据书籍的id拼接一个章节列表的接口

#将任务添加进chapterpool线程池，让线程池去执行章节列表的下载任务
def add_chapterpool(charpterlist):
    #通过遍历将任务添加进chapterpool线程池
    chapterpool = ThreadPoolExecutor(10) # 获取每一本书的章节列表
    for url in charpterlist:
        #添加任务
       a = chapterpool.submit(get_chapter,url)
       #设置回调
       a.add_done_callback(get_chapter_done)
    chapterpool.shutdown(True)

#获取小说的章节列表
def get_chapter(url):
    header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0'
    }
    response = requests.get(url,headers=header) 
    if response.status_code == 200:
        response.encoding = 'gbk'
        return response.text

#获取章节列表之后的回调
def get_chapter_done(future):
    text = future.result()
    #获取数据章节列表
    html = etree.HTML(text)
    chapter_detal_urls = html.xpath('//div[@class="clearfix dirconone"]/li/a/@href')
    #这里可以判断一下如果
    add_chapterDetalPool(chapter_detal_urls)


#将每一个章节的下载任务添加进章节下载的线程池，执行下载任务
def add_chapterDetalPool(chapter_detal_urls):
    #通过遍历将任务添加进章节下载的线程池
    chapterDetalPool = ThreadPoolExecutor(10) # 获取每一章节详情
    for url in chapter_detal_urls:
        #让线程池去执行下载章节详情的下载任务
        a = chapterDetalPool.submit(get_chapterDetal_data,url)
        #下载章节详情之后的回调函数
        a.add_done_callback(get_chapterDetal_data_done)
    chapterDetalPool.shutdown(True)


#下载章节详情的方法
def get_chapterDetal_data(url):
    header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0'
    }
    response = requests.get(url,headers=header) 
    if response.status_code == 200:
        response.encoding = 'gbk'
        return response.text


#章节下载完之后的回调
def get_chapterDetal_data_done(future):
    text = future.result()
    html = etree.HTML(text)
    shuming = html.xpath('//div[@id="direct"]/a[@class="article_title"]/text()')[0]
    zhangjieming =  html.xpath('//strong[@class="l jieqi_title"]/text()')[0]
    content = "".join(html.xpath('//div[@id="content"]/text()')).replace('<br />','').replace('\r','').replace('&nbsp;','')
    filename = 'novel1/'+shuming+'/'+zhangjieming+'.txt'
    print(filename)
    with open(filename,'a') as f:
        f.write(content)

def main():
    #如何定义一个线程池(池子里面有三个创建好的线程，可以同时使用)
    #max_workers：这个参数是说，同时能够执行的最大的线程数
    srarttime = time.time()
    navalpool = ThreadPoolExecutor(10) # 获取每一页

    #如何提交任务给线程池呢？
    for i in range(1,3):
        #submit: 表示将我们需要执行的任务给这个线程池，
        url = 'http://www.quanshuwang.com/list/1_'+str(i)+'.html'
        a = navalpool.submit(get_data,url)
        #给线程池设置任务之后，可以设置一个回调函数，
        #作用是：当我们某个任务执行完毕之后，就会回调你设置的回调函数
        a.add_done_callback(naveldone)

    navalpool.shutdown(True)
    endtime = time.time()
    #如何设置才能让主线程等待子线程任务结束再结束
    print(threading.current_thread().name)
    print(endtime-srarttime)

if __name__ == '__main__':
    main()




