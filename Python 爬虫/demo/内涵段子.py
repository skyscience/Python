import re
import urllib.request


class Spider:
    def __init__(self):
        self.page = 1   # 初始化起始页面位置
        self.switch = True  # 爬取开关，如果为True继续爬取


    def loadPage(self): # 下载页面
        print("正在下载数据...")
        url = "http://www.neihan8.com/article/list_5_" + \
        str(self.page) + ".html"
        headers = {"User_Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:58.0) Gecko/20100101 Firefox/58.0"}
        
        #向网页发起请求，获取网页返回的Response对象
        urlrequest = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(urlrequest)
        html = response.read()
        html = html.decode('gbk')
        print("数据获取成功")
        # 创建正则表达式规则创建对象，匹配每一页里面的段子内容，re.S
        # 表示匹配全部字符串内容
        pattern = re.compile('<div\sclass="f18 mb20">(.*?)</div>', re.S)
        # 将正则匹配对西那个应用到html源码字符里面，返回这个页面里的所有段子列表
        content_list = pattern.findall(html)
        self.dealPage(content_list)
    

    def dealPage(self, content_list):
        # 处理每页的段子
        print("正在处理数据...")
        for item in content_list:
            # 将集合里面的额每一个段子循环处理
            item = item.replace("<p>", "").replace(
            "</p>", "").replace("<br>", "").replace("<br />", "")
            # print(item)
            #调用写入方法写入文件
            self.writePage(item)


    def writePage(self, item):
        print("正在写入数据...")
        with open("duanzi.txt", "a") as f:
            f.write(item)
        #把每个段子写入文件里面


    def startWork(self):
        # 控制爬虫的运行
        #循环执行，直到self.switch == Flase
        while self.switch:
            self.loadPage()
            #python3 语法
            command = input("如果继续爬取请按回车(退出输入Q)")

            if command == "Q":
                self.switch = False
                print("谢谢使用")
            #每次循环，页面码数加一
            self.page += 1



if __name__ == "__main__":
    #先初始化一个类对象
    duanziSpider = Spider()
    #采用类的对象来调用类的方法
    duanziSpider.startWork()