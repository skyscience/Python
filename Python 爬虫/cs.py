# -*- coding: utf-8 -*-
import scrapy


class CsSpider(scrapy.Spider):
    name = 'cs'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/']

    def parse(self, response):
        pass
