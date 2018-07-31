# -*- coding: utf-8 -*-
import scrapy
# import sys
import time
import re


from mk.items import MkItem
from urllib import parse
from scrapy import FormRequest, Request
from scrapy.selector import Selector


pageIndex = 0
# sys.stdout = open('output.txt', 'w')


class TsSpider(scrapy.Spider):
    # 爬虫的识别名称，必须是唯一的，在不同的爬虫必须定义不同的名字。
    name = 'mks'
    # 允许访问的域
    allowed_domains = ['imooc.com']
    # 爬取的地址
    start_urls = ["http://www.imooc.com/course/list"]
    # 爬取方法

    def parse(self, response):
        # 实例一个容器保存爬取的信息
        item = MkItem()
        # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
        # 先获取每个课程的div
        sel = Selector(response)
        
        title = sel.xpath('/html/head/title/text()').extract()  # 标题
        print('[标题]: ',title[0])
        # sels = sel.xpath('//div[@class="course-card-content"]')
        sels = sel.xpath('//a[@class="course-card"]')
        # pictures = sel.xpath('//div[@class="course-card-bk"]')  #IMG
        index = 0
        global pageIndex
        pageIndex += 1


        print('[现在时间]: ',u'%s' % (time.strftime('%Y-%m-%d %H-%M-%S')))
        print('第' + str(pageIndex) + '页 ')
        print('========================================================')

        for box in sels:
            print(' ')
            # 获取div中的课程标题
            item['title'] = box.xpath(
                './/h3[@class="course-card-name"]/text()').extract()[0].strip()
            # print('标题：' + item['title'])

            # 获取div中的课程简介
            item['info'] = box.xpath(
                './/p/text()').extract()[0].strip()
            # print('简介：' + item['info'])

            # 获取每个div中的课程路径
            item['url'] = 'http://www.imooc.com' + \
                box.xpath('.//@href').extract()[0]
            # print('路径：' + item['url'])

            # 获取div中的学生人数
            item['student'] = box.xpath('.//div[@class="course-card-info"]/span[2]/text()').extract()[0].strip()
            # print(item['student'])

            # 获取div中的标题图片地址
            # item['img'] = pictures[index].xpath('.//img/@src').extract()[0]
            # print('图片地址：' + item['img'])
            
            index += 1
            yield item


        time.sleep(0.01)
        next = u'下一页'
        url = response.xpath("//a[contains(text(),'" + next + "')]/@href").extract()
        if url:
            # 将信息组合成下一页的url
            page = 'http://www.imooc.com' + url[0]
            # 返回url
            yield scrapy.Request(page, callback=self.parse)
        print('===END===')