# -*- coding: utf-8 -*-
import scrapy


class Ts1Spider(scrapy.Spider):
    name = 'ts1'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/']

    def parse(self, response):
        pass
