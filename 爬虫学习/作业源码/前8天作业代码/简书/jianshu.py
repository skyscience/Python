# 简书摄影分类数据
#https://www.jianshu.com/c/7b2be866f564?order_by=added_at&page=1

import requests
from lxml import etree
import urllib.parse as parse
import os
from concurrent.futures import ThreadPoolExecutor
import re

def get_article_url(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
    }
    # url = 'https://www.jianshu.com/c/7b2be866f564?order_by=added_at&page=1'
    # url = 'https://www.jianshu.com/c/7b2be866f564?order_by=added_at&page=2'
    response = requests.get(url, headers=headers)
    # with open('jianshu.html','w') as f:
    #     f.write(response.text)
    print(response.status_code)

    html = etree.HTML(response.text)
    article_list = html.xpath('//ul[@class="note-list"]/li')
    article_urls = []
    for article in article_list:
        href = article.xpath('.//a[@class="title"]/@href')[0]
        href = parse.urljoin(url,href)
        print(href)
        # get_detail_info(href)
        article_urls.append(href)
    
    if len(article_urls) > 0:
        return article_urls
    else:
        return []

    
def get_detail_info(future):
    urls = future.result()
    print(urls)
    if len(urls) > 0:
        for url in urls:
            # https://www.jianshu.com/p/83b1a5428162
            headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
            }
            response = requests.get(url, headers=headers)
            print(response.status_code)
            with open('deatil.html','w') as f:
                f.write(response.text)
            response.encoding = 'utf-8'
            html = etree.HTML(response.text)
            title = html.xpath('//h1[@class="title"]/text()')[0] + '\n'
            aythor = html.xpath('//div[@class="author"]//span[@class="name"]/a/@href')[0] + '\n'
            publish_time = html.xpath('//span[@class="publish-time"]/text()')[0] + '\n'
            content = html.xpath('//div[@class="show-content-free"]/p/text()')
            if len(content) == 0:
                content = ['暂无文本']
            content = '\n'.join(content)
            print(content)
            dirpath = 'jianshu/'+title
            detal_content = "标题："+ title + "作者:" +aythor + "发布时间:" +publish_time + "内容:" +content
            if not os.path.exists(dirpath):
                os.mkdir(dirpath)
            
            filename = dirpath+"/"+title
            with open(filename,"w") as f:
                f.write(detal_content)

            image_list = html.xpath('//div[@class="image-view"]/img/@data-original-src')
            add_downloadimage_to_pool(dirpath,image_list)

#因为下载图片是一个非常耗时的操作，所以我们采用线程池去下载任务
def add_downloadimage_to_pool(dirpath,image_list):
    #这里根据要下载的图片的数量，来创建线程池中线程的数量
    pool = ThreadPoolExecutor(len(image_list))
    #使用for循环，将任务添加进线程池
    for img_url in image_list:
        img_url = parse.urljoin('https:',img_url)
        p = pool.submit(downloadImage,(img_url,dirpath))
        p.add_done_callback(downloadImageDone)
    pool.shutdown(True)

#下载图片的任务
def downloadImage(data):
    print("开始下载图片"+data[0])
    headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
    }
    url = data[0]
    response = requests.get(url, headers=headers)
    #获取图片名称https://upload-images.jianshu.io/upload_images/7800712-c5a5551674956f1f.jpg
    parrent =  re.compile('.*?/upload_images/(.*?jpg)')
    imagename = re.findall(parrent,url)[0]
    # print(imagename)
    if response.status_code == 200:
        print(data[1],imagename)
        return response.content,data[1],imagename
    
def downloadImageDone(future):
    image_data = future.result()[0]
    dirpath = future.result()[1]
    imagename = future.result()[2]
    filename = dirpath+"/"+imagename
    with open(filename,"wb+") as f:
        f.write(image_data)


def main():
    downloadArticlePool = ThreadPoolExecutor(10)
    for i in range(1,2):
        url = 'https://www.jianshu.com/c/7b2be866f564?order_by=added_at&page=%s' % str(i)
        print(url)
        p = downloadArticlePool.submit(get_article_url,url)
        p.add_done_callback(get_detail_info)
    downloadArticlePool.shutdown(True)
    

if __name__ == '__main__':
    main()