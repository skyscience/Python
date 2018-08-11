# -*- coding:utf-8 -*-

import threading
import json
import requests
from lxml import etree
import queue

class ThreadCrawl(threading.Thread):
    def __init__(self,threadName,pageQueue,dataQueue):
        super(ThreadCrawl,self).__init__()
        self.threadName = threadName
        self.pageQueue = pageQueue
        self.dataQueue = dataQueue
        self.headers = {
            "User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
            }
    
    def run(self):
        print(threading.current_thread().name)
        while not CREWL_EXIT:
            try:
                page = self.pageQueue.get(False)
                url = "http://www.qiushibaike.com/8hr/page/" + str(page) +"/"
                response = requests.get(url,headers = self.headers)
                content_data = response.text
                self.dataQueue.put(content_data)
            except:
                pass
CREWL_EXIT = False

    
class ThreadParse(threading.Thread):
    def __init__(self,threadName,dataQueue):
        super(ThreadParse,self).__init__()
        self.threadName = threadName
        self.dataQueue = dataQueue

    def run(self):
        print(threading.current_thread().name)
        while not PARSE_EXIT:
            try:
                content = self.dataQueue.get(False)
                self.parse(content)
            except:
                pass
    
    def parse(self,content):
        print('在这里解析')
         # 解析为HTML DOM
        html = etree.HTML(content)

        node_list = html.xpath('//div[contains(@id, "qiushi_tag")]')

        for node in node_list:
            # xpath返回的列表，这个列表就这一个参数，用索引方式取出来，用户名
            username = node.xpath('./div/a/@title')[0]
            # 图片连接
            image = node.xpath('.//div[@class="thumb"]//@src')#[0]
            # 取出标签下的内容,段子内容
            content = node.xpath('.//div[@class="content"]/span')[0].text
            # 取出标签里包含的内容，点赞
            zan = node.xpath('.//i')[0].text
            # 评论
            comments = node.xpath('.//i')[1].text

            items = {
                "username" : username,
                "image" : image,
                "content" : content,
                "zan" : zan,
                "comments" : comments
            }
            # print(items)

            with open('duanzi.json','a') as f:
                f.write(json.dumps(items,ensure_ascii=False)+'\n')

PARSE_EXIT = False

def main():
    #创建三个爬取任务线程
    pageQueue = queue.Queue()
    #存放数据结果队列
    dataQueue = queue.Queue()
    #获取前20页的内容，将任务添加到队列
    for i in range(1,20):
        pageQueue.put(i)

    crawlNames = ['craw1','craw2','craw3']
    threadCrawls = []

    for threadName in crawlNames:
        crawlthread = ThreadCrawl(threadName,pageQueue,dataQueue)
        crawlthread.start()
        threadCrawls.append(crawlthread)

    parseNames = ['parse1','parse2','parse3']
    threadParses = []
    for threadName in parseNames:
        parseThread = ThreadParse(threadName,dataQueue)
        parseThread.start()
        threadParses.append(parseThread)


    while not pageQueue.empty():
        # print('pageQueue不为空')
        pass
    
    global CREWL_EXIT
    CREWL_EXIT = True

    print('pageQueue为空')

    for thread in threadCrawls:
        thread.join()

    while not dataQueue.empty():
        # print('dataQueue不为空')
        pass
    
    global PARSE_EXIT
    PARSE_EXIT = True

    print('dataQueue为空')

    for thread in threadParses:
        thread.join()

if __name__ == '__main__':
    main()