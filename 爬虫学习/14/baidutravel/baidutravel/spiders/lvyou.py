# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from urllib.parse import urljoin
from baidutravel.items import BaidutravelItem

class LvyouSpider(CrawlSpider):
    name = 'lvyou'
    allowed_domains = ['lvyou.baidu.com']
    start_urls = ['https://lvyou.baidu.com/scene/t-all_s-all_a-all_l-all']
    baseurl = 'https://lvyou.baidu.com/scene'

    rules = (
        Rule(LinkExtractor(allow=r'rn=12&pn=\d+',allow_domains=('lvyou.baidu.com',)),follow=True),
        Rule(LinkExtractor(allow=r'lvyou.baidu.com/.*?/$',restrict_xpaths=('//ul[@class="filter-result"]//h3',)),callback='parse_detail'),
    )

    # def parse_item(self, response):
    #     print(response.status)
    #     print(response.url)
    #     # i = {}
    #     # #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
    #     # #i['name'] = response.xpath('//div[@id="name"]').extract()
    #     # #i['description'] = response.xpath('//div[@id="description"]').extract()
    #     # return i


    def parse_detail(self,response):
        item = BaidutravelItem()
        #没一个地区的详情放在一个集合里面
        with open('detail.html','w') as f:
            f.write(response.body.decode('utf-8'))
        #标题
        item['title'] = response.xpath('//div[@class="dest-name "]//a[@class="clearfix"]/text()').extract_first('')
        #星级
        item['start_new'] = ''.join(response.xpath('//div[@class="main-score"]/text()').extract()).replace('\n','')
        #评论
        item['remarkcount'] = response.xpath('//a[@class="remark-count"]/text()').extract_first('')
        #简介
        item['desc'] = ''.join(response.xpath('//p[@class="main-desc-p"]//text()').extract()).replace('\n','')
        #路线总数
        item['luxiannums'] = ''.join(response.xpath('//a[@id="J_line-more-href"]//text()').extract())
        imageLink = response.xpath('//a[@class="pic-more more-pic-tip clearfix"]/@href').extract_first('')
        #拿到美图页面的完整链接地址
        item['allImagePageUrl'] = urljoin(self.baseurl,imageLink)
        #获取到路线的页面链接
        luxianurl = urljoin(self.baseurl,response.xpath('//a[@id="J_line-more-href"]/@href').extract_first(''))
        #获取当前页面关于景点的评论列表信息，放在一个列表里面
        remarklistTag = response.xpath('//div[@class="remark-list"]//div[@class="remark-item  remark-item-dest clearfix"]')
        print(len(remarklistTag))

        remarklist = []

        for node in remarklistTag:
            name = node.xpath('.//a[@class="ri-uname"]/@title').extract_first("")
            content = ''.join(node.xpath('.//div[@class="ri-body"]/div[@class="ri-remarktxt"]/text()').extract())
            publishtime = node.xpath('.//div[@class="ri-time"]/text()').extract_first("")
            available = node.xpath('.//a[@class="ri-dig ri-dig-available"]//span/text()').extract_first("")
            replynums = node.xpath('.//a[@class="ri-comment"]//span/text()').extract_first("")

            dict = {
                'name':name,
                'content':content,
                'publishtime':publishtime,
                'available':available,
                'replynums':replynums,
            }

            remarklist.append(dict)

        item['remarklist'] = remarklist

        yield scrapy.Request(luxianurl,callback=self.parse_luxian,meta={'item':item})


    #获取每一个目的地的行程路线的第一页数据
    def parse_luxian(self,response):
        print('解析路线')
        item = response.meta['item']
        with open('路线.html','w') as f:
            f.write(response.body.decode('utf-8'))
        pathlistTag = response.xpath('//li[@class="counselor-box"]')
        pathlist = []
        for node in pathlistTag:
            title = node.xpath('.//a[@class="plan-title"]/text()').extract_first("")
            url = urljoin(self.baseurl,node.xpath('.//a[@class="plan-title"]/@href').extract_first(""))
            keyword = node.xpath('.//a[@class="key-word"]/text()').extract()
            if len(keyword) == 0:
                keyword = '未知'
            else:
                keyword = '、'.join(keyword)
            daydest1 = '->'.join(node.xpath('.//div[@class="counselor-plan-detail"]/div[@class="day-dest"][1]//text()').extract()).replace('\n','')
            daydest2 = '->'.join(node.xpath('.//div[@class="counselor-plan-detail"]/div[@class="day-dest"][2]//text()').extract()).replace('\n','')
            dict = {
                'title':title,
                'url': url,
                'keyword': keyword,
                'daydest1': daydest1,
                'daydest2': daydest2,

            }
            pathlist.append(dict)

        item['path_list'] = pathlist

        yield item
