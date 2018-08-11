# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JobboleSpider(CrawlSpider):
    name = 'jobbole'

    allowed_domains = ['jobbole.com']

    start_urls = ['http://blog.jobbole.com/all-posts/']
    # http://blog.jobbole.com/all-posts/page/1/
    # http://blog.jobbole.com/all-posts/page/2/
    # http://blog.jobbole.com/all-posts/page/3/
    # http://blog.jobbole.com/all-posts/page/4/

    #rules是一个元组，存放连接提取的规则Rule对象
    rules = (
        Rule(LinkExtractor(allow=r'http.*?all-posts/page/\d+',tags=('a','img'),attrs=('href','src'),restrict_css=('div.navigation.margin-20','div.navigation.margin-20'),restrict_xpaths=('//div[@class="navigation margin-20"]','//div[@class="navigation margin-20"]')), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=(),),callback='parse_item',follow=True)
    )

    def parse_item(self, response):

        print(response.status)
        #
        # yield item
