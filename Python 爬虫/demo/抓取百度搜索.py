#__author__ = 'Administrat
#coding=utf-8

import urllib.request as request
import urllib.parse as parse
import ssl
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


def get_search_data(params,headers):
    #https://www.baidu.com/s?wd=%E5%95%A4%E9%85%92%E8%8A%82&pn=10
    full_url = 'https://www.baidu.com/s?'+params
    print('正在获取请求:'+ full_url)
    context = ssl._create_unverified_context()

    req = request.Request(full_url,headers=headers)
    response = request.urlopen(req,context = context)
    print(response.status)
    html = response.read().decode('utf-8') #=
    write_data(html,parse.unquote(params))  

def write_data(html,url):
    print('正在写入:'+ url)
    file = 'GET/'+url+'.html'
    with open(file,'w',encoding='utf-8') as f:
        f.write(html)


def main():
    kw = input('请输入搜索关键字:')
    print(kw)
    startpage = int(input('请输入获取的起始页码'))
    endpage = int(input('请输入截止的页码'))
    print(kw,startpage,endpage)
    
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
    }


    for i in range(startpage,endpage+1):
        wd = {
            'wd':kw,
            'pn':(i-1)*10,
        }
        wd = parse.urlencode(wd,encoding='utf-8')
        get_search_data(wd,headers)


if __name__ == '__main__':
    main()