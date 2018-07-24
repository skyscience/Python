# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from crawljobbole.items import CrawljobboleItem


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
        Rule(LinkExtractor(allow=r'http.*?all-posts/page/\d+',), callback='parse_item',follow=True),
    )

    def parse_item(self, response):

        articles = response.xpath('//div[@class="post floated-thumb"]')
        for subitem in articles:
            # 如果想完全用正则提取
            # result = response.xpath('.').re('')
            item = CrawljobboleItem()
            # 标题
            item['title'] = subitem.xpath('.//a[@class="archive-title"]/text()').extract_first('')
            # 时间
            item['publishTime'] = subitem.xpath('.//div[@class="post-meta"]/p[1]/text()').re('\d+/\d+/\d+')[0]
            # tag
            item['tags'] = subitem.xpath('.//div[@class="post-meta"]/p[1]/a[2]/text()').extract_first('')
            # 简介
            item['desctext'] = ','.join(subitem.xpath('.//span[@class="excerpt"]//p/text()').extract())
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
                if len(subitem.xpath('.//div[@class="post-meta"]/p[1]/a[3]/text()').re('\d+')) > 0:
                    item['commentNum'] = subitem.xpath('.//div[@class="post-meta"]/p[1]/a[3]/text()').re('\d+')[0]
                else:
                    item['commentNum'] = '0'
            else:
                item['commentNum'] = '0'

            # 图片连接
            item['image_url'] = subitem.xpath('.//div[@class="post-thumb"]/a/img/@src').extract_first('')
            # 本地图片路径
            # image_path = scrapy.Field()
            yield item
