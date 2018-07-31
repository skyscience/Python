# -*- coding: utf-8 -*-
import scrapy
from test1.items import Test1Item
from urllib import parse
import re
from scrapy import FormRequest,Request

class TsSpider(scrapy.Spider):
    #爬虫的识别名称，必须是唯一的，在不同的爬虫必须定义不同的名字。
    name = 'ts1' 
    #搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页，不存在的URL会被忽略。
    allowed_domains = ["example.webscraping.com"]
    start_urls = ['http://example.webscraping.com/user/profile']
    login_url = 'http://example.webscraping.com/places/default/user/login'

    
    def parse(self, response):
        print('web_info',response.text)

    
    def start_requests(self):
        yield scrapy.Request(self.login_url,callback=self.login)

    
    def login(self,response):
        formdata = {
        'email':'2639358455@qq.com','password':'18201423398h'}
        yield FormRequest.from_response(response,formdata=formdata,
        callback=self.parse_login)
    
    
    def parse_login(self,response):
        print('[info ]: '+response.text)
        if 'Welcome' in response.text:
            yield from super().start_requests()