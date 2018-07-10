import urllib.request as request
import ssl,re
from mypy import *
import random



def getData():
    url = 'http://www.xicidaili.com/nn/'+ page
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
    req = request.Request(url,headers=headers)
    response = request.urlopen(req)
    content = response.read().decode('utf-8')
    #获取正则匹配全部数据
    pattern = re.compile('<tr.*?>.*?<td\sclass="country"><img.*?></td>.*?<td>(.*?)</td>.*?<td>(\d+)</td>.*?<a\shref=".*?">(.*?)</a>.*?<td\sclass="country">.*?</td>.*?<td>(.*?)</td>.*?<td>(\d.*?[\u4e00-\u9fa5])</td>.*?<td>(\d.*?\d)</td>.*?</tr>',re.S)
    get_data = re.findall(pattern,content)
    # print(get_data)
   
    return database_data(get_data)

def database_data(get_data):
   
    mysqlHelper =  MysqlHelper('127.0.0.1','root','1227bing','xicidaili')
    for data in get_data:
        mysqlHelper.connect()
        ip = data[0]
        # print(ip)
        port = data[1]
        # print(port)
        address = data[2]
        # print(address)
        type = data[3]
        # print(type)
        time = data[4]
        # print(time)
        datetime = data[5]
        # print(datetime)` `

        http_handler = request.HTTPHandler()
        context = ssl._create_unverified_context()
        https_handler = request.HTTPSHandler(context=context)
        proxy_handler = request.ProxyHandler({type:ip+':'+port})
        opener = request.build_opener(http_handler,https_handler,proxy_handler)
        url = 'http://www.baidu.com'
    
        req = request.Request(url)
        response = opener.open(req)
        # print(response.status)
        if response.status == 200:
            sql = "insert into dldata values(0,%s,%s,%s,%s,%s,%s)"
            params = [ip,port,address,type,time,datetime]
            finish = mysqlHelper.insert(sql,params)

    if finish:
        print('添加成功！')
    else:
        print('添加失败!')
    return getPageData()
#获取随机一组数据的ip和端口
def get_random_data():
    mysqlHelper =  MysqlHelper('127.0.0.1','root','1227bing','xicidaili')
    mysqlHelper.connect()
    sql = 'select * from dldata'
    #从数据库中获取全部数据
    fetchall = mysqlHelper.fetchall(sql)
    # print(fetchall)
    #随机抽出一组数据
    random_data = random.choice(fetchall)
    #获取随机一组数据的ip和端口
    random_data = ('IP: '+random_data[1]+'\tPort: '+random_data[2])
    print(random_data)


def getPageData():
    mysqlHelper =  MysqlHelper('127.0.0.1','root','1227bing','xicidaili')
    mysqlHelper.connect()
    sql = 'select * from dldata limit %s,10'
    sy = (int(page)-1)*10
    # sy = str(sy)
    params = [sy]
    #从数据库中获取全部数据
    fetchall = mysqlHelper.fetchall(sql,params)
    for data in fetchall:
        print('IP: ' + data[1]+'\tPort: ' + data[2])
    random_one = int(input('是否随机选择一个IP？ 1.是 2.否'))
    if random_one == 1:
        get_random_data()
    else:
        pass
   
page = input('请输入你要访问的页数: ')
getData()






