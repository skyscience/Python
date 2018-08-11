# -*- coding: utf-8 -*-
import scrapy
from jobboleproject.items import JobboleprojectItem
import re

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url,callback=self.custom_parse)


    def custom_parse(self,response):
        print(response.status)
        print('自定义解析方法')

        articles = response.xpath('//div[@class="post floated-thumb"]')
        for subitem in articles:
            #如果想完全用正则提取
            # result = response.xpath('.').re('')

            item = JobboleprojectItem()
            print(item)
            # 标题
            item['title'] = subitem.xpath('.//a[@class="archive-title"]/text()').extract_first('')
            # 时间
            item['publishTime'] = subitem.xpath('.//div[@class="post-meta"]/p[1]/text()').re('\d+/\d+/\d+')[0]
            # tag
            item['tags'] = subitem.xpath('.//div[@class="post-meta"]/p[1]/a[2]/text()').extract_first('')
            # 简介
            item['desc'] = ','.join(subitem.xpath('.//span[@class="excerpt"]//p/text()').extract())
            # 评论数
            # item['commentNum'] = subitem.xpath('.//div[@class="post-meta"]/p[1]/a[3]/text()').extract()
            # if len(item['commentNum']) > 0:
            #     pattern = re.compile('\d+')
            #     result = re.findall(pattern,item['commentNum'][0])
            #     item['commentNum'] = result[0]
            # else:
            #     item['commentNum'] = 0
            comment_tag = subitem.xpath('.//div[@class="post-meta"]/p[1]/a[3]')
            if len(comment_tag) > 0:
                item['commentNum'] = int(subitem.xpath('.//div[@class="post-meta"]/p[1]/a[3]/text()').re('\d+')[0])
            else:
                item['commentNum'] = 0

            # 图片连接
            item['image_url'] = subitem.xpath('.//div[@class="post-thumb"]/a/img/@src').extract_first('')
            # 本地图片路径
            # image_path = scrapy.Field()
            print(item)
            yield item







        next_url = response.xpath('//a[@class="next page-numbers"]/@href').extract_first('')
        print(next_url)

        yield scrapy.Request(url=next_url,callback=self.parse)

    # def parse(self, response):
    #     print(response.status)
    #
    #
    #
    #     #提取下一页的ｕｒｌ
    #     next_url = response.xpath('//a[@class="next page-numbers"]/@href').extract_first('')
    #     print(next_url)
    #
    #     yield scrapy.Request(url=next_url,callback=self.parse)
