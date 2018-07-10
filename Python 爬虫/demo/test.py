import requests
import os

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

text = input('输入您要查询什么')

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5478.400 QQBrowser/10.1.1550.400',
}
for i in range(0,4):
    url = 'https://www.baidu.com/s?wd={0}&pn={1}'.format(text,str(i*10))
    print(url)
    response = requests.get(url,headers=headers)
    a = open(text+str(i)+'.txt','w')
    a.write(response.text).decode('utf-8')