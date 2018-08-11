# -*- coding:UTF-8 -*-
import pymysql
from urllib.request import Request,urlopen
import re

# 目标url的地址规律：
# http://www.xicidaili.com/nn/1
# http://www.xicidaili.com/nn/2
# http://www.xicidaili.com/nn/3

class Spider_IP:
    def __init__(self):
        self.client = pymysql.Connect('localhost','root','ljh123456','ipproxy',3306)
        self.cursor = self.client.cursor()

    def get_ip_data(self,endpage):
        for i in range(1,endpage+1):
            print('正在获取第'+str(i)+'页')
            url = 'http://www.xicidaili.com/nn/'+ str(i)
            headers = {
                'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
            }
            #构建一个request请求对象(url、data、headers)
            req = Request(url,headers=headers)
            #发起请求(可以)
            response = urlopen(req)
            #获取html源码
            html = response.read().decode('UTF-8')
            # print(html)
            #编辑匹配的规则
            re_compile1 = re.compile(r'<tr.*?class="odd".*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?country.*?<td>(.*?)</td>.*?',re.S)
            result1 = re.findall(re_compile1,html)
            re_compile2 = re.compile('<tr.*?class="".*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?country.*?<td>(.*?)</td>.*?',re.S)
            result2 = re.findall(re_compile2,html)
            # print(result1)
            # print(result2)
            ip_result = result1+result2
            #返回所有的IP结果
            # return ip_result
            for ip_item in ip_result:
                self.save_ip_todb(ip_item)

    def save_ip_todb(self,ipitem):
        print(ipitem)
        print('正在保存代理'+ipitem[0])
        #构建数据库插入语句
        insert_sql = """
        INSERT INTO proxy(ip,port,type) VALUES(%s,%s,%s)
        """
        self.cursor.execute(insert_sql,ipitem)
        self.client.commit()
        # self.cursor.close()

if __name__ == '__main__':
    spider = Spider_IP()
    endpage = input('请输入截止页码：') 
    spider.get_ip_data(int(endpage)) 
    
    





