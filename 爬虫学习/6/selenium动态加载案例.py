# douban 
from selenium import webdriver 
import time
from lxml import etree
#构造了一个浏览器的驱动
driver = webdriver.Chrome(executable_path='/Users/ljh/Desktop/chromedriver')

#发起一个请求
#https://movie.douban.com/
driver.get('https://movie.douban.com/')

time.sleep(10)

driver.find_element_by_id('inp-query').send_keys('成龙')
# driver.find_element_by_name('search_text').send_keys('电影')
# with open('page.html','w') as f:
#     f.write(driver.page_source)
driver.find_element_by_css_selector('.inp-btn input').click()
if driver.page_source:
   html = etree.HTML(driver.page_source)
   movie_list = html.xpath('//div[@class="item-root"]')
   print(len(movie_list))
#    for item in movie_list:
#     #    print(item)
#        #获取电影的名称
#        name = item.xpath('.//a[@class="title-text"]/text()')[0]
#        #获取电影的评分
#        score = item.xpath('.//span[@class="rating_nums"]/text()')
#     #    if judge_None(score) == False:
#     #        score = 0
#        if len(score) == 0:
#            score = 0
#        else:
#            score = score[0]

#        #获取评论量
#        comment_num = item.xpath('.//span[@class="pl"]/text()')[0]
#        #电影的演员介绍
#        meta = item.xpath('.//div[@class="meta abstract"]/text()')[0]
#        #电影的主演员介绍
#        meta2 = item.xpath('.//div[@class="meta abstract_2"]/text()')[0]
#        #电影封面图片的链接
#        image_link = item.xpath('./a/img/@src')[0]
#        #电影详情的链接
#        movie_link = item.xpath('.//a[@class="title-text"]/@href')[0]
#        print(name,score,comment_num,meta,meta2,image_link,movie_link)
       
       #保存数据库
         #自己完善

       #继续找下一页
        # 自己完善
    
def judge_None(list):
    if len(list) == 0:
        return False
    else:
        return True

    # with open('page.html','w') as f:
    #     f.write(driver.page_source)

# driver.close()
# driver.quit()

