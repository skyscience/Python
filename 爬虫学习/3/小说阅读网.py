# https://www.readnovel.com/rank/hotsales?pageNum=2
# https://www.readnovel.com/rank/hotsales?pageNum=1

import urllib.request as request
import urllib.parse as parse
import urllib.error as error
import ssl, os, re

ISFINISHED = False

def get_data_from_url(url):
    print(url)
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
    }
    req = request.Request(url,headers=headers)
    try:
        response = request.urlopen(req,context=ssl._create_unverified_context())
    except error.HTTPError as err:
        print(err)
    except error.URLError as err:
        print(err)
    else:
        if response.status == 200:
            print('请求完成')
            pattern = re.compile('<li.*?data-rid.*?<img.*?src="(.*?)">.*?book-mid-info.*?<a\shref="(.*?)".*?>(.*?)</a>.*?name.*?default.*?>(.*?)</a>'
            +'.*?<a.*?>(.*?)</a>.*?<span>(.*?)</span>.*?intro.*?>(.*?)</p>.*?update.*?<a.*?>(.*?)</a>.*?<span>(.*?)</span>',re.S)
            html = response.read().decode('utf-8')
            
            novel_list = re.findall(pattern,html)
            # print(len(novel_list))

            if len(novel_list) == 0:
                print('全部下载完成')
                global ISFINISHED
                ISFINISHED = True
            
            for novel in novel_list:
                # print(novel)
                #''.join():把列表拼接成字符串
                # content = '\n'.join(novel).replace(' ','').replace('\r','')
                # if not os.path.exists('小说阅读/'+novel[1]):
                #     print('正在创建文件夹：' + novel[2])
                #     os.mkdir('小说阅读/'+novel[2])
                # write_txt_to_file(content,novel[2])
                # get_image_from_url('https:'+novel[0],novel[2])

                # https://www.readnovel.com/book/9553264004296703#Catalog

                novel_deatil_url = parse.urljoin('https://www.readnovel.com/book/9553264004296703#Catalog',novel[1])+'#Catalog'
                print(novel_deatil_url)
                get_novel_datail_from_url(novel_deatil_url)

def get_novel_datail_from_url(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
    }
    req = request.Request(url,headers=headers)
    try:
        response = request.urlopen(req,context=ssl._create_unverified_context())
    except error.HTTPError as err:
        print(err)
    except error.URLError as err:
        print(err)
    else:
        if response.status == 200:
           print(response.status)
           html = response.read().decode('utf-8')
           #通过分析页面，我们发现每一个详情中的免费的章节列表，在第一div的ul下
           pattern = re.compile('<div\sclass="volume".*?<ul\sclass="cf">(.*?)</ul>',re.S)
           result = re.search(pattern,html)
           #这个时候我们取到了所有的免费章节的li标签
           html = result.group(1)
           #为了匹配章节详情的连接和标题
           pattern = re.compile('<a\shref="(.*?)".*?>(.*?)</a>',re.S)
           chapter_list = re.findall(pattern,html)
           for chapter in chapter_list:
               print(chapter) 


       



def write_txt_to_file(content,filename):
    print('正在写入图片：'+filename)
    with open('小说阅读/'+filename+'/'+filename+'.txt','w') as f:
        f.write(content)

def get_image_from_url(url,filename):
    print('正在下载图片：'+filename+'jpg')
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
    }
    req = request.Request(url,headers=headers)
    try:
        response = request.urlopen(req,context=ssl._create_unverified_context())
    except error.HTTPError as err:
        print(err)
    except error.URLError as err:
        print(err)
    else:
        if response.status == 200:
            print(filename+'.jpg'+'下载完成')
            write_image_to_file(response.read(),filename)


def write_image_to_file(data,filename):
    with open('小说阅读/'+filename+'/'+filename+'.jpg','wb') as f:
        f.write(data)


def main():
    for i in range(1,2):
        if ISFINISHED == False:
            full_url = 'https://www.readnovel.com/rank/hotsales?pageNum='+str(i)
            get_data_from_url(full_url)
        else:
            print('跳出循环，下载完毕')
            break

if __name__ == '__main__':
    main()