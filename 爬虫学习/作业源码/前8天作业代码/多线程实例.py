import requests
import threading
from lxml import etree
import queue

class crawlThread(threading.Thread):
    def __init__(self,threadName,page_queue,data_queue):
        super(crawlThread,self).__init__()
        self.threadName = threadName
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',}

    def run(self):
        # 这里从page_queue获取对应的页码
        while not self.page_queue.empty():
            #get()从队列中取值，先进先出
            page = self.page_queue.get()
            print(page)
            full_url = 'http://blog.jobbole.com/all-posts/page/'+str(page)+'/'
            response = requests.get(full_url,headers=self.headers)
            response.encoding = 'utf-8'
            if response.status_code == 200:
                #将获取到的结果，存放在data_queue队列中
                self.data_queue.put(response.text)
        
# #线程的采集任务
# def crawl_data(page_queue,data_queue):
#     header = {
#         'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
#     }
#     # 这里从page_queue获取对应的页码
#     while not page_queue.empty():
#         #get()从队列中取值，先进先出
#         page = page_queue.get()
#         print(page)
#         full_url = 'http://blog.jobbole.com/all-posts/page/'+str(page)+'/'
#         response = requests.get(full_url,headers=header)
#         response.encoding = 'utf-8'
#         if response.status_code == 200:
#             #将获取到的结果，存放在data_queue队列中
#             data_queue.put(response.text)

# def parse_data(data_queue):
#     #不为空的时候去取值，为空说明没有解析任务了
#     while not data_queue.empty():
#         html = etree.HTML(data_queue.get())
#         articles = html.xpath('//div[@class="post floated-thumb"]')
#         for item in articles:
#             title = item.xpath('.//a[@class="archive-title"]/text()')[0]
#             print(title)

class parseThread(threading.Thread):
    def __init__(self,threadName,data_queue,lock):
        super(parseThread,self).__init__()
        self.threadName = threadName
        self.data_queue = data_queue
        self.lock = lock

    def run(self):
        #不为空的时候去取值，为空说明没有解析任务了
        while not self.data_queue.empty():
            html = etree.HTML(self.data_queue.get())
            articles = html.xpath('//div[@class="post floated-thumb"]')
            for item in articles:
                title = item.xpath('.//a[@class="archive-title"]/text()')[0]
                print(title)
                self.lock.acquire() #加锁
                with open('jobbole.txt','a') as f:
                    f.write(title+'\n')
                self.lock.release() #解锁



def main():
    #创建一个任务队列：里面的参数maxsize表示最大的存储量
    page_queue = queue.Queue(40)
    #http://blog.jobbole.com/all-posts/page/2/  (2表示页码)
    for i in range(1,30):
        page_queue.put(i)

    #将解析后的数据放在这个队列中，供后后面的解析线程去做解析
    data_queue = queue.Queue()

    #创建线程取下载任务
    lock = threading.Lock()
    crawlThreadName = ['crawl1号','crawl2号','crawl3号','crawl4号']
    thread_list = []
    for threadName in crawlThreadName:
        # thread = threading.Thread(target=crawl_data,name=threadName,args=(page_queue,data_queue))
        thread = crawlThread(threadName,page_queue,data_queue)
        # thread.setDaemon(True)
        thread.start()
        thread_list.append(thread)
        # thread.join() 不能直接写在这里

    for thread in thread_list:
        thread.join()

    #创建解析线程：
    parseThreadName = ['parse1号','parse2号','parse3号','parse4号']
    parseThread_list = []
    for threadName in parseThreadName:
        # thread = threading.Thread(target=parse_data,name=threadName,args=(data_queue,))
        # thread.setDaemon(True)
        thread = parseThread(threadName,data_queue,lock)
        thread.start()
        parseThread_list.append(thread)
    
    for thread in parseThread_list:
        thread.join()
    
    #打印当前线程的名称
    print(threading.current_thread().name)
    

if __name__ == '__main__':
    main()
