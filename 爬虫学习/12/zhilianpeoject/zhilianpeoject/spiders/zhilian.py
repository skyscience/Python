# -*- coding: utf-8 -*-
import scrapy
from zhilianpeoject.items import ZhilianpeojectItem,ZhilianCompanyItem

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

        next_page_url = response.xpath('//li[@class="pagesDown-pos"]/a/@href').extract_first('')
        # print(next_page_url)
        # if not next_page_url is '':
        #     yield scrapy.Request(next_page_url,callback=self.parse)
        # else:
        #     print('没有下一页了')


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
        item['companyUrl'] = response.xpath('//p[@class="company-name-t"]/a/@href').extract()[0]
        # print(jobtitle,salary,publishTime,workAdress,needpeople,companyUrl,company)
        # print(item)
        yield scrapy.Request(item['companyUrl'],callback=self.parse_company_detail,meta={'company':item['companyName']})
        yield item

    def parse_company_detail(self,response):
        print(response.status) #打印请求状态
        #css提取
        # 提取公司名称
        item = ZhilianCompanyItem()

        #取值
        item['companyName'] = response.meta['company']

        item['comapyName'] = response.css('div.mainLeft > div h1::text').extract_first('')
        # 公司性质
        if len(response.css('table.comTinyDes tr')) > 0:
            comapnyClassfiy = response.css('table.comTinyDes tr')[0].css('td span::text').extract()
            # 公司规模
            if len(comapnyClassfiy) > 1:
                item['comapnyClassfiy'] = comapnyClassfiy[1]

            companyMode = response.css('table.comTinyDes tr')[1].css('td span::text').extract()
            if len(companyMode) > 1:
                item['companyMode'] = companyMode[1]
            # # 公司行业
            companyIndustry = response.css('table.comTinyDes tr')[2].css('td span::text').extract()
            if len(companyIndustry) > 1:
                item['companyIndustry'] = companyIndustry[1]
            # # 公司地址
            companyAdress = response.css('table.comTinyDes tr')[3].css('td span::text').extract()
            if len(companyAdress) > 1:
                item['companyAdress'] = companyAdress[1]
        # # 公司介绍s
        item['companyDesc'] = '\n'.join(response.css('.company-content ::text').extract())
#         vip_image_url = response.css('div.mainLeft > div h1 img::attr(src)').extract_first('')
# # 　　　　　.extract_first('')　＝> .extract()[0]
#         jobname_url = response.css('.positionListContent1 .jobName a::attr(href)').extract_first('')
        yield item