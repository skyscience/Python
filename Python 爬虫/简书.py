import re
import urllib.request
import ssl


class Spider:
    def __init__(self):
        self.switch = True  


    def loadPage(self): 
        print("正在下载数据...")
        url = "https://www.jianshu.com/c/7b2be866f564" 
        # str(self.page) + ".html"
        headers = {"User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
        context = ssl._create_unverified_context()


        #向网页发起请求，获取网页返回的Response对象
        urlrequest = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(urlrequest, context=context)
        html = response.read()
        html = html.decode('gbk')
        print("数据获取成功")


        # 创建正则表达式规则创建对象，匹配每一页里面的段子内容，re.S
        # 表示匹配全部字符串内容
        pattern = re.compile('<a\sclass="title">(.*?)</a>', re.S)
        print("数据:"+pattern)
        # 将正则匹配对西那个应用到html源码字符里面，返回这个页面里的所有段子列表
        content_list = pattern.findall(html)
        self.dealPage(content_list)
    

    def dealPage(self, content_list):
        # 处理每页的段子
        print("正在处理数据...")
        for item in content_list:
            # # 将集合里面的额每一个做循环处理
            # item = item.replace("<p>", "").replace(
            # "</p>", "").replace("<br>", "").replace("<br />", "")
            # print(item)
            #调用写入方法写入文件
            self.writePage(item)


    def writePage(self, item):
        print("正在写入数据...")
        with open("duanzi.txt", "a") as f:
            f.write(item)
        #把每个条链接写入文件里面


    def startWork(self):
        while self.switch:
            self.loadPage()
            command = input("如果继续爬取请按回车(退出输入N)")

            if command == "N":
                self.switch = False
                print("谢谢使用")
            #每次循环，页面码数加一
            self.page += 1




if __name__ == "__main__":
    #先初始化一个类对象
    start = Spider()
    #采用类的对象来调用类的方法
    start.startWork()