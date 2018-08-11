# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from zhonghuawang.items import ZhonghuawangItem
# from scrapy_redis.spiders import RedisCrawlSpider

class ZhwSpider(CrawlSpider):
# class ZhwSpider(RedisCrawlSpider):
    name = 'zhw'
    allowed_domains = ['china.com']
    start_urls = ['https://travel.china.com/hotspot/index_1.html']
    # redis_key = 'zhwSpider:start_urls'

    rules = (
        #https://travel.china.com/hotspot/index_1.html
        Rule(LinkExtractor(allow='.*?index_\d+.*?html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        #拿到列表数据
        # response.encoding = 'gbk'
        # response.body.decode(response.encoding)
        article_list = response.xpath('//div[@class="listnewsarea"]/div')

        for note in article_list:
            item = ZhonghuawangItem()
            item['title'] = note.xpath('.//div[@class="m_R"]/h2/a/text()').extract_first().encode('utf-8').decode('utf-8')
            item['content'] = note.xpath('.//div[@class="tt"]/text()').extract_first()
            item['publishTime'] = note.xpath('.//span[@class="time"]/text()').extract_first()
            print(item)
            yield item



