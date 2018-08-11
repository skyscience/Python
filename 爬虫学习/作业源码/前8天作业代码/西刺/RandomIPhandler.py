# -*- coding:utf-8 -*-
import pymysql
import random

class RandomIPhandler:
    #初始化构造函数
    def __init__(self):
        self.client = pymysql.Connect('localhost','root','ljh123456','ipproxy',3306)
        self.cursor = self.client.cursor()
    
    def get_random_ip(self):
        #随机获取一条数据
        select_SQL='select * from proxy'
        self.cursor.execute(select_SQL)
        results=self.cursor.fetchall()
        result=random.choice(results)
        # 优化在这里我们可以做一个优化处理判断当前选取的ip是否可以使用
        # 自定义一个ProxyHandler对象设置需要使用的IP
        # 构建一个opener对象
        # 使用urllib_opener将自定义opener自定义为全局的（注意这样写之后调用urlopen就相当于调用自定义的opener对象）
        # 使用opener.open方法打开连接判断是否有html，其实这里更适合做error的容错判断确定代理是否可用，如果不可用那么我们递归再次获取
        # 优化点：如果判断当前的代理不可用，那么我们是否可以将数据库里面的这条数据删除掉？（自己实现）
        return result

    # def ipCheck(self, proxy_ip):
    #     """代理检测"""
    #     proxy_host = +ip[0]+":"+ip[1] 
    #     proxy = urllib2.ProxyHandler(proxy_ip)
    #     opener = urllib2.build_opener(proxy)
    #     urllib2.install_opener(opener)
    #     try:
    #         html = urllib2.urlopen('http://1212.ip138.com/ic.asp')
    #         # print html.read()
    #         if html:
    #             self.is_active_proxy_ip.append(proxy_ip)
    #             return True
    #         else:
    #             return False
    #     except Exception as e:
    #         return False


def main():
    handler = RandomIPhandler()
    ip = handler.get_random_ip()
    print(ip)

#入口函数
if __name__ == '__main__':
    main()




