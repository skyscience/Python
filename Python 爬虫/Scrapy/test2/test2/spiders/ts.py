# -*- coding: utf-8 -*-
import scrapy


class TsSpider(scrapy.Spider):
    name = 'ts'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        filename = 'jobbole.html'
        open(filename,'wb').write(response.body)
