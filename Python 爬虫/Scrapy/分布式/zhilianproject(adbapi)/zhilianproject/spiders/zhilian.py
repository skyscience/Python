# -*- coding: utf-8 -*-
import scrapy
#LinkExtractor，根据你定义的正则规则，来匹配链接
from scrapy.linkextractors import LinkExtractor

from scrapy.spiders import CrawlSpider, Rule

from zhilianproject.items import ZhilianJobItem,ZhilianCompanyItem

import scrapy

class ZhilianSpider(CrawlSpider):
    #爬虫的名称，启动爬虫时，会根据爬虫的名称
    name = 'zhilian'
    #允许爬取的域
    # allowed_domains = ['sou.zhaopin.com','jobs.zhaopin.com','company.zhaopin.com']
    allowed_domains = ['zhaopin.com']
    #设置起始url
    start_urls = ['https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E6%8A%80%E6%9C%AF&sm=0&p=1']

    scrapy.Request

    #每一页的链接

    # < a
    # href = "http://sou.zhaopin.com/jobs/searchresult.ashx?" \
    #        "jl=%e5%8c%97%e4%ba%ac&amp;kw=%e6%8a%80%e6%9c%af&amp;" \
    #        "sm=0&amp;sg=01655a036139411dbce2a559588d62da&amp;p=4" >
    # 4 < / a >
    #

    #匹配详情的链接
    # < a
    # style = "font-weight: bold"
    # par = "ssidkey=y&amp;ss=201&amp;ff=03&amp;sg=01655a036139411dbce2a559588d62da&amp;so=51"
    # href = "http://jobs.zhaopin.com/554770135250104.htm"
    # target = "_blank" > 通信 < b > 技术 < / b > 硬件工程师 < / a >

    #匹配公司想详情的链接进行请求
    #http: // company.zhaopin.com / CC433408989.htm

    rules = (
        Rule(LinkExtractor(allow=('http.*?jobs/searchresult',),
                           restrict_xpaths='//div[@class="pagesDown"]/ul'),
                           callback='parse_item',
                           ),

        Rule(LinkExtractor(allow=('http.*?jobs.zhaopin.com/.*?htm',),
                           restrict_xpaths='//div[@id="newlist_list_content_table"]'),
             callback='parse_job_detail'),

        Rule(LinkExtractor(allow=('http.*?company.zhaopin.com/.*?htm',)),
             callback='parse_company_detail'),
    )

    def parse_item(self, response):
        print(response.status)
        print(response.url)

    def parse_job_detail(self,response):
        # with open('job.html','w') as f:
        #     f.write(response.body.decode('utf-8'))
        print(response.status)
        print(response.url)

        #创建一个item对象
        item = ZhilianJobItem()

        # 职位名称
        item['jobName'] = response.xpath('//div[@class="inner-left fl"]//h1/text()').extract_first('')
        # 职位薪资
        item['salary'] = response.xpath('//div[@class="terminalpage clearfix"]//ul[@class="terminal-ul clearfix"]/li[1]/strong/text()').extract_first('')
        # 发布时间
        item['publishTime'] = response.xpath('//span[@id="span4freshdate"]/text()').extract_first('')
        # 职位描述
        item['jobDesc'] = ''.join(response.xpath('//div[@class="terminalpage-main clearfix"]//div[@class="tab-inner-cont"]//text()').extract())
        # 地址
        item['address'] = response.xpath('//div[@class="terminalpage-main clearfix"]//h2/text()').extract_first('')
        # 公司名称
        item['company'] = response.xpath('//div[@class="inner-left fl"]//h2/a/text()').extract_first('')

        # yield item


    def parse_company_detail(self,response):
        print(response.status)
        print(response.url)
        item = ZhilianCompanyItem()

        # 公司名称
        item['companyName'] = response.xpath('//div[@class="mainLeft"]//h1/text()').extract_first('')
        # 公司类型
        item['companyType'] = response.xpath('//table[@class="comTinyDes"]/tr[1]/td[2]/span/text()').extract_first('')
        # 公司规模
        item['companyModel'] = response.xpath('//table[@class="comTinyDes"]/tr[2]/td[2]/span/text()').extract_first('')
        # 行业
        item['trade'] = response.xpath('//table[@class="comTinyDes"]/tr[3]/td[2]/span/text()').extract_first('')
        # 公司地址
        item['address'] = response.xpath('//table[@class="comTinyDes"]/tr[4]/td[2]/span/text()').extract_first('')

        yield item

