# -*- coding: utf-8 -*-
import scrapy
from zhilianpeoject.items import ZhilianpeojectItem

class ZhilianSpider(scrapy.Spider):
    #name:爬虫的名称，当我们运行爬虫的时候会根据这个名字去找对应的爬虫文件
    name = 'zhilian'
    #allowed_domains:允许爬取的域，可以有多个，你要抓取的ｕｒｌ必须在你设置的域，
    allowed_domains = ['zhaopin.com']
    #start_urls:设置爬虫的起始任务，存放的是目标链接，可以有多个
    start_urls = ['https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E6%8A%80%E6%9C%AF&sm=0&sg=de41ce9d23e64b80bb1305ce3d0fcf57&p=1']

    # parse解析的方法，我们下载器下载好任务（得到的响应response）
    def parse(self, response):
        #返回的是响应的状态码
        print(response.status)
        #返回的是一个字符串
        # print(response.text)
        #使用ｘｐａｔｈ提取数据
        job_list = response.xpath('//div[@class="newlist_list_content"]//table')
        # print(job_list)
        # print(len(job_list))
        for item in job_list:
            #extract作用：将获取到的数据转换ｕｎｉｃｏｄｅ编码，并以列表的形式返回
            url = item.xpath('.//td[@class="zwmc"]/div/a[1]/@href').extract()

            if len(url) > 0:
                url = url[0]
                print(url)
                yield scrapy.Request(url,callback=self.parse_job_detail)


    def parse_job_detail(self,response):
        item = ZhilianpeojectItem()
        print(response.status)
        #获取到了职位详情的ｈｔｍｌ，然后进一步去提取里面的数据
        #职位名称
        item['jobtitle'] = response.xpath('//div[@class="inner-left fl"]/h1/text()').extract()[0]
        #月薪
        item['salary'] = response.xpath('//div[@class="terminalpage clearfix"]//li[1]/strong/text()').extract()[0]
        #发布日期
        item['publishTime'] = response.xpath('//div[@class="terminalpage clearfix"]//li[3]/strong/span/text()').extract()[0]
        #工作地点
        item['workAdress'] = response.xpath('//div[@class="terminalpage clearfix"]//li[2]/strong/a/text()').extract()[0]
        #招聘人数
        item['needpeople'] = response.xpath('//div[@class="terminalpage clearfix"]//li[7]/strong/text()').extract()[0]
        # #职位描述
        # jobDesc = response.xpath('//div[@class="terminalpage-main clearfix"]//div[@class="tab-inner-cont"]/div/text()').extract()[0]
        # #公司名称
        item['companyName'] = response.xpath('//p[@class="company-name-t"]/a/text()').extract()[0]
        # #公司详情的ｕｒｌ
        item['companyUrl'] = ','.join(response.xpath('//p[@class="company-name-t"]/a/@href').extract())
        # print(jobtitle,salary,publishTime,workAdress,needpeople,companyUrl,company)
        # print(item)
        yield item
        # pass

