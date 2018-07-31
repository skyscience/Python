import json
import matplotlib.pyplot as pp
from tkinter import *
import webbrowser as web


f = open(r"D:\Program\Python\Python 爬虫\Scrapy\test1\test1.json",
         'r', encoding='UTF-8')
temp = json.loads(f.read())
sl = temp.keys()



top = []
for z in sl:
    top.append(int(z))
for i in range(len(top)-1):    # 这个循环负责设置冒泡排序进行的次数
    for j in range(len(top)-i-1):  # ｊ为列表下标
        if top[j] < top[j+1]:
            top[j], top[j+1] = top[j+1], top[j]
top10 = top[0:10]





# 显示前十名的标题
t10_title = []
for t in top10:
    t = str(t)
    print(str(temp[t]['title']))
    t10_title.append(temp[t]['title'])

def t10d():
    tt = 0
    for xx10 in t10_title:
        tt += 1
        print(tt,'.  ',xx10)


def tj():
    pp.plot(t10_title, top10, linewidth=5)  # 参数linewidth 决定了plot() 绘制的线条的粗细。
    # 设置图表标题，并给坐标轴加上标签（不支持中文）
    pp.title("muke class top", fontsize=24)
    pp.xlabel("class", fontsize=14)  # 函数xlabel() 和ylabel() 让你能够为每条轴设置标题
    pp.ylabel("student", fontsize=12)


    # 函数tick_params() 设置刻度的样式，
    # 其中指定的实参将影响x 轴和y 轴上的刻度 （axes='both' ），
    # 并将 刻度 标记的字号设置为14（labelsize=14 ）。
    pp.tick_params(axis='both', labelsize=14)   # 设置刻度标记的大小
    pp.show()



# 打开浏览器
def browse(url):
	web.open(url)


# ========================= 往下是垃圾场======================
# emm 代码没写好...
def printhello0():
    print('点击')
    cd = top10[0]
    fsurl = temp[str(cd)]['url']
    browse(fsurl)

def printhello1():
    print('点击')
    cd = top10[1]
    fsurl = temp[str(cd)]['url']
    browse(fsurl)

def printhello2():
    print('点击')
    cd = top10[2]
    fsurl = temp[str(cd)]['url']
    browse(fsurl)

def printhello3():
    print('点击')
    cd = top10[3]
    fsurl = temp[str(cd)]['url']
    browse(fsurl)

def printhello4():
    print('点击')
    cd = top10[4]
    fsurl = temp[str(cd)]['url']
    browse(fsurl)

def printhello5():
    print('点击')
    cd = top10[5]
    fsurl = temp[str(cd)]['url']
    browse(fsurl)

def printhello6():
    print('点击')
    cd = top10[6]
    fsurl = temp[str(cd)]['url']
    browse(fsurl)

def printhello7():
    print('点击')
    cd = top10[7]
    fsurl = temp[str(cd)]['url']
    browse(fsurl)

def printhello8():
    print('点击')
    cd = top10[8]
    fsurl = temp[str(cd)]['url']
    browse(fsurl)

def printhello9():
    print('点击')
    cd = top10[9]
    fsurl = temp[str(cd)]['url']
    browse(fsurl)

def topU():
    root = Tk()  # 初始化Tk()
    root.title("text-test")    # 设置窗口标题
    root.geometry("300x340")    # 设置窗口大小 注意：是x 不是*
    # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
    root.resizable(width=True, height=True)
    t = Text(root)
    Button(root, text=t10_title[0], command=printhello0).pack()
    Button(root, text=t10_title[1], command=printhello1).pack()
    Button(root, text=t10_title[2], command=printhello2).pack()
    Button(root, text=t10_title[3], command=printhello3).pack()
    Button(root, text=t10_title[4], command=printhello4).pack()
    Button(root, text=t10_title[5], command=printhello5).pack()
    Button(root, text=t10_title[6], command=printhello6).pack()
    Button(root, text=t10_title[7], command=printhello7).pack()
    Button(root, text=t10_title[8], command=printhello8).pack()
    Button(root, text=t10_title[9], command=printhello9).pack()
    t.pack()   # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
    root.mainloop()  # 进入消息循环

    



while True:
    print('\n'*4)
    print('慕课网爬虫辅助系统')
    print('0.课程总数')
    print('1.===')
    print('2.查看前10名课程')
    print('3.查看前10名课程详情')
    print('4.进入排行榜')
    print('6.退出系统')
    ia = input('请选择功能，输入对应的序号 按enter键即可。')
    ia = int(ia)
    if ia == 0:
        print('\n'*2)
        print('课程数：', len(sl))
    if ia == 1:
        print('\n'*2)
        print('>>>',top,'<<<')
    if ia == 2:
        print('\n'*2)
        t10d()
    if ia == 3:
        print('\n'*2)
        tj()
    if ia ==4:
        print('\n'*2)
        topU()
    if ia == 6:
        break