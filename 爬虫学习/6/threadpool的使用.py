from concurrent.futures import ThreadPoolExecutor
import threading
from lxml import etree
import requests

def run(page):
    #get()从队列中取值，先进先出
    print(page)
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',}
    #打印当前线程的名称
    print(threading.current_thread().name)
    full_url = 'http://blog.jobbole.com/all-posts/page/'+str(page[0])+'/'
    response = requests.get(full_url,headers=headers)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        #将获取到的结果，存放在data_queue队列中
        return response.text
       
def download_done(future):
    # print(future.result())
    print('下载成功')
    html = etree.HTML(future.result())
    articles = html.xpath('//div[@class="post floated-thumb"]')
    for item in articles:
        title = item.xpath('.//a[@class="archive-title"]/text()')[0]
        print(title)

#ThreadPoolExecutor;可以帮我们创建一个线程池（池子里面芳的是线程）
#如何构造一个线程池(里面有10个子线程)
pool = ThreadPoolExecutor(10)
for i in range(1,50):
    #执行完毕任务之后，有一个返回的结果
    handle = pool.submit(run,(i,))
    handle.add_done_callback(download_done)






