from concurrent.futures import ProcessPoolExecutor
import requests
from lxml import etree
import csv,os
def download_data(url):
    print('下载进程：'+str(os.getpid()))
    header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0'
    }
    response = requests.get(full_url,headers=header)
    response.encoding = 'gbk'
    if response.status_code == 200:
        print(full_url+'请求成功')
        print('下载进程结束：'+str(os.getpid()))
        return response.text

def done(future):
    # print(future.result())
    html = etree.HTML(future.result())
    novel_list = html.xpath('//ul[@class="seeWell cf"]/li')
    print(len(novel_list))
    for item in novel_list:
        print(item)
        title = item.xpath('.//a[@class="clearfix stitle"]/text()')[0]
        novel_link = item.xpath('.//a[@class="clearfix stitle"]/@href')[0]
        author = item.xpath('.//span[@class="l"]/a[2]/text()')[0]
        desc = item.xpath('.//em[@class="c999 clearfix"]/text()')[0]
        dict = {'title':title,'novel_link':novel_link,
        'author':author,'desc':desc,
        }

        with open('xiaoshuo.csv','a') as f:
            fieldnames = ['title','novel_link','author','desc']
            writer = csv.DictWriter(f,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(dict)



    
        

pool = ProcessPoolExecutor(10)
# full_url = 'http://www.quanshuwang.com/list/1_'+str(page)+'.html'
for i in range(1,200):
    full_url = 'http://www.quanshuwang.com/list/1_'+str(i)+'.html'
    handler = pool.submit(download_data,(full_url,))
    handler.add_done_callback(done)
pool.shutdown(wait=True)

