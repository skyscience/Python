# 1.分析目标网站
# 头条
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=-1

# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=20298065&count=15&category=-1

#直播
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=6

# #沪深
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=105

# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=178343&count=15&category=105

#房产
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=111

#港股
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=102

#基金
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=104

#美股
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=101

# 私募
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=113

#保险
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=110
#多进程来实现
from concurrent.futures import ProcessPoolExecutor
import requests
import json,os

pool = ProcessPoolExecutor(8)

def get_data_from_parmas(parmas):
    # parmas:参数,get请求后面拼接的参数，是一个字典类型
    # requests.get(url,parmas)
    print('开启下载进程'+str(os.getpid))
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
        'Referer':'https://xueqiu.com/',
        'Cookie':'device_id=4296c195e93c0b7e4e5ec89ac01a55ac; Hm_lvt_1db88642e346389874251b5a1eded6e3=1531458617,1531458631,1531462196,1531462250; _ga=GA1.2.1992218818.1528361692; _gid=GA1.2.1754465791.1531405223; aliyungf_tc=AQAAACSqQmM3SAUAWRBAfFcxAhChRqtr; xq_a_token=7443762eee8f6a162df9eef231aa080d60705b21; xq_a_token.sig=3dXmfOS3uyMy7b17jgoYQ4gPMMI; xq_r_token=9ca9ab04037f292f4d5b0683b20266c0133bd863; xq_r_token.sig=6hcU3ekqyYuzz6nNFrMGDWyt4aU; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1531462808; u=431531442513356',
    }
    response = requests.get('https://xueqiu.com/v4/statuses/public_timeline_by_category.json',params=parmas,headers=headers)
    # print('1')
    print(response.status_code) #打印结果状态
    # response.json() = > json.loads(response.text)
    # print(response.json())
    # print(next_max_id)
    parmas['count'] = 15
    parmas['max_id'] = response.json()['next_max_id']
    #将要获取的下一页的链接的参数，和响应结果返回
    print('结束下载进程'+str(os.getpid))
    return parmas,response.json(),response.url

def download_done(future):
    
    # print(future.result())
    print(future.result()[0])
    print(future.result()[2])
    #解析操作，
    jsonData = print(future.result()[1])

    #发起请求，
    handler = pool.submit(get_data_from_parmas,future.result()[0])
    handler.add_done_callback(download_done)
    

if __name__ == '__main__':
    #进程池
    print('开启主进程'+str(os.getpid))
    # since_id=-1&max_id=-1&count=10&category=113
    list = [
        {'since_id':-1,'max_id':-1,'count':10,'category':-1},
        {'since_id':-1,'max_id':-1,'count':10,'category':6},
        {'since_id':-1,'max_id':-1,'count':10,'category':105},
        {'since_id':-1,'max_id':-1,'count':10,'category':111},
        {'since_id':-1,'max_id':-1,'count':10,'category':102},
        {'since_id':-1,'max_id':-1,'count':10,'category':104},
        {'since_id':-1,'max_id':-1,'count':10,'category':101},
        {'since_id':-1,'max_id':-1,'count':10,'category':113},
        {'since_id':-1,'max_id':-1,'count':10,'category':110},
    ]

    for parmas in list:
        handler =  pool.submit(get_data_from_parmas,parmas)
        handler.add_done_callback(download_done)

    # pool.close()
    # pool.join()
    # pool.shutdown(wait=True)

    print('主进程结束'+str(os.getpid))



