from multiprocessing import Process,Queue
from multiprocessing import Manager
import requests
from lxml import etree
import csv,os

def getdata(pageQueue,dataQueue):
    header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0'
    }
    while not pageQueue.empty():
        print('进程开启'+str(os.getpid()))
        page = pageQueue.get()
        #http://www.quanshuwang.com/list/1_page.html
        full_url = 'http://www.quanshuwang.com/list/1_'+str(page)+'.html'
        # print(full_url)
        dataQueue.put(full_url)
        response = requests.get(full_url,headers=header)
        response.encoding = 'gbk'
        if response.status_code == 200:
            print(full_url+'请求成功')
            dataQueue.put(response.text)
            print(dataQueue.empty())

#解析进程
def parsedata(dataQueue):
    print('解析进程'+str(os.getpid()))
    print(dataQueue.empty())
    while not dataQueue.empty():
        html = etree.HTML(dataQueue.get())
        novel_list = html.xpath('//ul[@class="seeWell cf"]/li')
        print(len(novel_list))
    

if __name__ == '__main__':
    print('主线程开始')
    #构建了一个任务队列
    # pageQueue = Manager().Queue(200)
    pageQueue = Queue(200)
    for i in range(1,20):
        pageQueue.put(i)
    #构建一个结果队列，存储获取的响应结果
    # dataQueue = Manager().Queue()
    dataQueue = Queue()
    #打印，查看队列是否为空
    print(pageQueue.empty(),dataQueue.empty())

    p1 = Process(target=getdata,args=(pageQueue,dataQueue))
    # p2 = Process(target=getdata,args=(pageQueue,dataQueue))
    # p3 = Process(target=getdata,args=(pageQueue,dataQueue))

    # p2.start()
    # p3.start()

    
    # p2.join()
    # p3.join()
    
    parse1 = Process(target=parsedata,args=(dataQueue,))
    parse2 = Process(target=parsedata,args=(dataQueue,))
    # parse3 = Process(target=parsedata,args=(dataQueue,))
   
    p1.start()
    parse1.start()
    # parse2.start()
    # parse3.start()
    
    p1.join()
    parse1.join()
    # parse2.join()
    # parse3.join()

    print('主线程结束')





    