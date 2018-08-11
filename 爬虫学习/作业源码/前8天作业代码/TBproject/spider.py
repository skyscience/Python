from selenium import webdriver
import time
from lxml import etree
import MySQLdb
import pymongo


# chrome_options = webdriver.ChromeOptions()
# chrome_options.set_headless()

# 一定要注意driver驱动的版本和谷歌浏览器的版本

browser = webdriver.Chrome(executable_path="/Users/ljh/Desktop/chromedriver")
# browser = webdriver.Chrome(executable_path="/Users/ljh/Desktop/chromedriver",options=chrome_options)
# browser = webdriver.PhantomJS(executable_path='/Users/ljh/Desktop/phantomjs')
# browser = webdriver.Firefox(executable_path='/Users/ljh/Desktop/geckodriver')
# 创建mysql数据库链接
mysqlcli = MySQLdb.connect('127.0.0.1','root','ljh123456','taobao',charset='utf8',use_unicode=True)

#mongoDB的数据库链接(设置IP和端口号)
mongocli = pymongo.MongoClient(host='127.0.0.1',port=27017)
# 创建mongodb数据库名称（没有会自动创建）
dbname = mongocli['taobao']
# 创建mongodb数据库的表名称（没有会自动创建）
sheetname = dbname['product']

def search():
    browser.get("https://www.taobao.com")
    browser.implicitly_wait(3)
    browser.find_element_by_class_name("search-combobox-input").send_keys("美食")
    time.sleep(2)
    print('点击了搜索按钮')
    browser.find_element_by_class_name("btn-search").click()
    if browser.page_source:
        getprodect_items(browser.page_source)


def getprodect_items(html):
    # with open("page.html","w") as file:
    #     file.write(html)
    response = etree.HTML(html)
    items = response.xpath("//div[@class='item J_MouserOnverReq  ']")
    for each in items:
        print('正在插入')
        image_url = "https:" + each.xpath("//div[@class='pic']/a/img/@src")[0]
        title = each.xpath(".//div[@class='pic']/a/img/@alt")[0]
        buynum = each.xpath(".//div[@class='deal-cnt']/text()")[0]
        price = each.xpath(".//div[@class='price g_price g_price-highlight']/strong/text()")[0]
        store = each.xpath(".//div[@class='shop']/a/span[2]/text()")[0]
        location = each.xpath(".//div[@class='location']/text()")[0]
        print("------华丽的商品分割线-----")
        # print("商品图片地址："+"https:"+image_url)
        # print("商品名称:"+title)
        # print("商品价格:"+price)
        # print("购买数量:"+buynum)
        # print("商店地址:"+location)
        # print("店铺名称:"+store)
        # 这里需要将数据写如数据库
        # 分别以mysql
        # cursor = mysqlcli.cursor()
        # insert_sql = """
        #       INSERT INTO tbproduct(title,price,image_url,buynum,location,store)
        #       VALUES (%s,%s,%s,%s,%s,%s)
        # """
        # cursor.execute(insert_sql,[title,float(price),image_url,buynum,location,store])
        # mysqlcli.commit()
        # cursor.close()
        print([title,float(price),image_url,buynum,location,store])

        # mongoDB为例
        # product = {
        #     "title":title,
        #     "image_url":image_url,
        #     "price":price,
        #     "buynum":buynum,
        #     "location":location,
        #     "store":store
        # }
        # sheetname.insert(product)


    # 获取下一页的数据
    time.sleep(3)
    
    browser.find_element_by_css_selector("li.item.next a.J_Ajax.num.icon-tag").click()
    # 如果数据存在就进行提取数据
    if browser.page_source:
        time.sleep(1)
        # 递归方法获取数据
        getprodect_items(browser.page_source)
        


def main():
    search()
    time.sleep(5)
    browser.quit()

if __name__ == '__main__':
    main()