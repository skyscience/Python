# selenium:是一个自动化的测试工具，
# 应用场景适合在网站使用动态加载的技术，（javascrapy，ajax）

# pip3 install selenium
from selenium import webdriver
import time

#设置Chrome的无界面浏览器
# opt = webdriver.ChromeOptions()
# opt.set_headless()
# 创建一个浏览器的驱动
dirver = webdriver.Chrome(options=opt,executable_path='/Users/ljh/Desktop/chromedriver')
# PhantomJS
# dirver = webdriver.PhantomJS(executable_path='/Users/ljh/Desktop/phantomjs')
#发起一个请求
dirver.get('https://movie.douban.com/subject_search?search_text=%E6%88%90%E9%BE%99&cat=1002')
#打印网页的文本信息

time.sleep(5)

with open('page.html','w') as f:
    f.write(dirver.page_source)
# print(dirver.page_source)
#保存截图的
dirver.save_screenshot('baidu.png')
#根据id找到对应的标签，send_keys往标签离 main输入内容
# dirver.find_element_by_id('kw').send_keys('赵圆')
# #根据id找到对应的标签，然后模拟点击
# dirver.find_element_by_id('su').click()
# dirver.save_screenshot('baidu.png')
# print(dirver.page_source)

#点击结果页面的新闻栏
# dirver.find_element_by_css_selector('.s_tab > a').click()

# dirver.find_element_by_xpath('//div[@class="s_tab"]//a[1]').click()

# time.sleep(2)

# # dirver.back()

# # dirver.find_element_by_xpath('//p[@id="page"]/a[1]').click()
# dirver.implicitly_wait(10)
# # 隐士等待：作用会在你设定的时间里做等待，等待10秒终
# dirver.find_element_by_css_selector('#page > a').click()

# time.sleep(2)

# #后退
# dirver.back()

# time.sleep(5)

# #前进
# dirver.forward()

# # 刷新当前界面
# dirver.refresh()

# #退出浏览器
# dirver.close()

# 获取cookies值，一般我们会使用selenium用来模拟登陆
# dirver.get_cookies()




