from multiprocessing import Process,Queue
#Manager支持的类型有List,Dict,Queue
from multiprocessing import Manager
import requests
from lxml import etree
import csv,os

def getdata(pageQueue,dataQueue):
    header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0'
    }
    while not pageQueue.empty():
        print('下载进程开启'+str(os.getpid()))
        page = pageQueue.get()
        #http://www.quanshuwang.com/list/1_page.html
        full_url = 'http://www.quanshuwang.com/list/1_'+str(page)+'.html'
        response = requests.get(full_url,headers=header)
        response.encoding = 'gbk'
        if response.status_code == 200:
            print(full_url+'请求成功')
            print('下载进程结束'+str(os.getpid()))
            dataQueue.put(response.text)

#解析进程
def parsedata(dataQueue):
    print('解析进程开启'+str(os.getpid()))
    print(dataQueue.empty())
    while not dataQueue.empty():
        data = dataQueue.get()
        if not data is 0:
            print('解析进程结束'+str(os.getpid()))
            html = etree.HTML(data)
            novel_list = html.xpath('//ul[@class="seeWell cf"]/li')
            print(len(novel_list))
        else:
            print('退出')
            break
    
    
if __name__ == '__main__':
    print('主进程开始')
    #构建了一个任务队列
    # pageQueue = Queue(300)
    pageQueue = Manager().Queue(300)
    for i in range(1,50):
        pageQueue.put(i)
    #构建一个结果队列，存储获取的响应结果
    # dataQueue = Queue()
    dataQueue = Manager().Queue()
    #打印，查看队列是否为空
    print(pageQueue.empty(),dataQueue.empty())

    downloadProcess = []
    for i in range(0,3):
        p1 = Process(target=getdata,args=(pageQueue,dataQueue))
        p1.start()
        downloadProcess.append(p1)

    for process in downloadProcess:
        process.join()

    print('总数',dataQueue.empty(),dataQueue.qsize())

    parseProcess = []
    for i in range(0,3):
        parse1 = Process(target=parsedata,args=(dataQueue,))
        parse1.start()
        parseProcess.append(p1)
    
    for process in parseProcess:
        parse1.join()

    print(dataQueue.empty())
    print('主进程结束')



    