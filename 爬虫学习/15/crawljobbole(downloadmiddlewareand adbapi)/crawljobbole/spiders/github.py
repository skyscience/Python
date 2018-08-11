# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
import time,json,os

class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/people/3kyhghuoghuo/activities',]

    def start_requests(self):

        if os.path.exists('cookie.txt'):
            f = open('cookie.txt','r')
            cookie_str = f.read()
            if cookie_str:
                cookie_dict = json.loads(cookie_str)
                for url in self.start_urls:
                    yield scrapy.Request(url, callback=self.parse, cookies=cookie_dict)
        else:
            driver = webdriver.Chrome(executable_path='/home/ljh/桌面/chromedriver')
            driver.get('https://www.zhihu.com/')
            driver.find_element_by_xpath('//div[@class="HomeSidebar-signBannerActions"]/button[1]').click()
            time.sleep(1)
            driver.find_element_by_name('username').send_keys('13366634531')
            driver.find_element_by_name('password').send_keys('a362320')

            #driver.find_element_by_class_name('Button SignFlow-submitButton Button--primary Button--blue').click()
            driver.find_element_by_css_selector('Button.SignFlow-submitButton.Button--primary.Button--blue').click()
            cookies = driver.get_cookies()
            cookie_dict = {}
            for cookie in cookies:
                print(cookie['name'],cookie['value'])
                cookie_dict[cookie['name']] = cookie['value']

            with open('cookie.txt','w') as f:
                f.write(json.dumps(cookie_dict,ensure_ascii=False))

            print(cookie_dict)
            print(cookies)

            for url in self.start_urls:
                yield scrapy.Request(url,callback=self.parse,cookies=cookie_dict)
        print('打印ｃｏｏｋｉｅｓ')

    def parse(self, response):
        print(response.status)
        pass
