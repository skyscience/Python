# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class CrawljobboleSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class CrawljobboleDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

# import random
# #自定义ｃｏｏｋｉｅｓ中间件：
# class RandomCookiesMiddleware(object):
#     def __init__(self,cookies):
#         self.cookies = cookies
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         cookies = crawler.settings['COOKIES']
#         return cls(cookies)
#
#     def process_item(self,request,spider):
#         #随机获取一个ｃｏｏｋｉｅ
#         cookie = random.choice(self.cookies)
#         if cookie:
#             request.cookies = cookie
#
#         return None

    # def process_response(self,response,spider):
    #     response.status = 500






#使用ｓｅｌｅｎｉｕｍ加载数据
# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# from scrapy.http import HtmlResponse
#
# class SeleniumMiddleware(object):
#     def __init__(self):
#         self.drive = webdriver.Chrome(executable_path='/home/ljh/桌面/chromedriver')
#         self.drive.set_page_load_timeout(10)
#
#     def process_item(self,request,spider):
#         try:
#             url = request.url
#             self.drive.get(url)
#             if self.drive.page_source:
#                 return HtmlResponse(url=url,body=self.drive.page_source,status=200,encoding='utf-8',request=request)
#         except TimeoutException:
#             print('请求超时')
#             return HtmlResponse(url=url,body=None,status=500)









#自定义ＵｓｅｒＡｇｅｎｔ中间件
# class RandomUserAgent(object):
#     """This middleware allows spiders to override the user_agent"""
#     def __init__(self, useragents):
#         self.useragents = useragents
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         #crawler.settings['USERAGENTS'] 获取ｓｅｔｔｉｎｇｓ.ｐｙ中的ＵＡ池
#         USERAGENTS = crawler.settings['USERAGENTS']
#         return cls(USERAGENTS)
#
#     def process_request(self, request, spider):
#         user_agent = random.choice(self.useragents)
#         print('执行下载中间件'+user_agent)
#         print(user_agent)
#         if user_agent:
#             request.headers.setdefault(b'User-Agent', user_agent)
#             # request.headers['User-Agent'] = user_agent
#         return None
#使用第三方插件来随机获取Ｕｓｅｒ－Ａｇｅｎｔ
# from fake_useragent import UserAgent
# class RandomUserAgentMiddlewareTwo(object):
#
#     def process_request(self, request, spider):
#         user_agent = UserAgent().random
#         print('执行下载中间件'+user_agent)
#         if user_agent:
#             request.headers.setdefault(b'User-Agent', user_agent)
#             # request.headers['User-Agent'] = user_agent

#定义一个ｉｐ代理的中间件
# import base64
# class RandomIPMiddleware(object):
#     def __init__(self,proxies):
#         self.proxies = proxies
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         PROXIES = crawler.settings['PROXIES']
#         return cls(PROXIES)
#
#     def process_request(self, request, spider):
#         proxy = random.choice(self.proxies)
#         if proxy['user_pwd'] is None:
#             request.meta['proxy'] = proxy['IP']
#         else:
#             user_pwd = base64.b64encode(proxy['user_pwd'].encode('utf-8')).decode('utf-8')
#             #设置代理的一个信令
#             request.headers['Proxy-Authorization'] = 'Basic ' + user_pwd
#             request.meta['proxy'] = proxy['IP']
#
#         return None







