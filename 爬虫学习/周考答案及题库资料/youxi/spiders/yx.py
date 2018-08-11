# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from youxi.items import YouxiItem,YouxiMobileItem
import re,json

class YxSpider(CrawlSpider):
    name = 'yx'
    allowed_domains = ['17173.com']
    start_urls = ['http://top.17173.com/list-2-0-0-0-0-0-0-0-0-0-1.html','http://newgame.17173.com/shouyou/ceshi']

    rules = (
        Rule(LinkExtractor(allow=r'top.17173.com/list-2-0-0-0-0-0-0-0-0-0-\d+.*?html'), callback='parse_item', follow=True),
    )

    def parse_start_url(self, response):
        if response.url.find('top.17173.com') > 0:
            print('热门游戏榜获取成功startUrls')
            print(response.url)
            self.parse_item(response)
        else:
            print('手游公测榜')
            #解析y第一页的内容，然后加载后面的Ａｊａｘ页面数据
            newList = response.xpath('ul[@id="nowlist"]/li')
            bgList = response.xpath('ul[@id="bgitem"]/li')
            endList = response.xpath('ul[@id="enditem"]/li')

            for node in newList:
                item = YouxiMobileItem()
                item['name'] = node.xpath('.//h6[@class="tit"]/a/text()').extract_first()
                item['testTime'] = node.xpath('.//div[@class="c2"]/p/text()').extract_first()
                item['testName'] = node.xpath('.//p[@class="c3"]/text()').extract_first()
                item['testStatus'] = node.xpath('.//i[@class="c8"]/text()').extract_first()
                item['voteNum'] = 0
                url = node.xpath('.//h6[@class="tit"]/a/@href').extract_first()

                yield scrapy.Request(url,callback=self.parse_detail,meta={'item':item,'type':'test'})

            for node in bgList+endList:
                item = YouxiMobileItem()
                item['name'] = node.xpath('.//h6[@class="c1"]/a/text()').extract_first()
                item['testTime'] = node.xpath('.//p[@class="c2"]/text()').extract_first()
                item['testName'] = node.xpath('.//p[@class="c3"]/text()').extract_first()
                item['testStatus'] = node.xpath('.//i[@class="c6"]/text()').extract_first()
                item['voteNum'] = 0
                url = node.xpath('.//h6[@class="tit"]/a/@href').extract_first()

                yield scrapy.Request(url, callback=self.parse_detail, meta={'item': item, 'type': 'test'})


            yield scrapy.Request('http://newgame.17173.com/shouyou/ceshi/GetTestListApi?pageSize=30&page=2',callback=self.parse_youxi_test)
            #"cnt": 17判断u又没哟数据
            #http://newgame.17173.com/shouyou/ceshi/GetTestListApi?pageSize=30&page=13

    def parse_youxi_test(self,response):
        data = json.loads(response.text)
        cnt = int(data['data']['cnt'])
        if cnt > 0:
            for node in data['data']['dataSet']:
                item = YouxiMobileItem()
                item['name'] = node['info_chname']
                item['testTime'] = node['test_stime']
                item['testName'] = node['test_status_name']
                item['testStatus'] = node['test_status']
                item['voteNum'] = 0
                url = node['game_url']

                yield scrapy.Request(url, callback=self.parse_detail, meta={'item': item, 'type': 'test'})

            nextPage = int(re.findall('.*?page=(\d+)',response.url)[0]) + 1
            fullUrl = 'http://newgame.17173.com/shouyou/ceshi/GetTestListApi?pageSize=30&page=%d' % nextPage

            yield scrapy.Request(fullUrl,callback=self.parse_youxi_test)



    def parse_item(self, response):
        print('热门游戏榜获取成功')
        rank_list = response.xpath('//div[@class="mod-bd"]//div[@class="item-in"]')
        print(len(rank_list))
        for node in rank_list:
            item = YouxiItem()
            item['name'] = node.xpath('.//div[@class="con"]/a/text()').extract_first('').strip()
            item['testStatus'] = node.xpath('.//div[@class="c5"]/text()').extract_first('').strip()
            item['rankNum'] = int(node.xpath('.//div[@class="c1"]/em/text()').extract_first('').strip())
            item['voteNum'] = int(node.xpath('.//div[@class="c3"]/text()').extract_first('').strip())
            url = node.xpath('.//div[@class="con"]/a/@href').extract_first('')

            yield scrapy.Request(url=url,callback=self.parse_detail,meta={'item':item,'type':'new'})

    def parse_detail(self, response):
        item = response.meta['item']
        type = response.meta['type']

        item['coverImage'] = response.xpath('//div[@class="pn-c1"]//span[@class="avatar-t"]//img/@src').extract_first('')

        item['star'] = response.xpath('//div[@class="box-star-l"]/div/@style').re('\d+')
        if len(item['star']) > 0:
            item['star'] = item['star'][0]
        else:
            item['star'] = 0
        item['cate'] = ','.join(response.xpath('//div[@class="box-mater-cate"]//a/text()').extract())
        item['type'] = response.xpath('//ul[@class="list-mater-info"]/li[1]/a/text()').extract_first('')
        item['free'] = response.xpath('//ul[@class="list-mater-info"]/li[3]/span/text()').extract_first('')
        item['language'] = response.xpath('//ul[@class="list-mater-info"]/li[2]/span/a/text()').extract_first('')
        item['company'] = response.xpath('//ul[@class="list-mater-info"]/li[5]/a/text()').extract_first('')
        item['operator'] = response.xpath('//ul[@class="list-mater-info"]/li[@class="item-operator"]/span[2]/a/text()').extract_first('')
        item['desc'] = response.xpath('//div[@class="mod-mater-intro"]/p/text()').extract_first('')
        item['download'] = response.xpath('a[@class="channel-dl"]/@href').extract_first('')
        item['regest'] = response.xpath('//ul[@class="list-mater-info"]/li[6]/a/@href').extract_first('')
        item['officialUrl'] = response.xpath('//a[@class="to-website-normal"]/@href').extract_first()

        pattern = re.compile('http.*?game-info-(\d+).html')
        result = re.findall(pattern, response.url)[0]
        if type == 'test':
            #http://top.17173.com/api/gamerankinfo?gameCode=4054552.js
            yield scrapy.Request('http://top.17173.com/api/gamerankinfo?gameCode='+result,callback=self.parse_rank_num,meta={'item':item,'id':result})

        else:
            # http://hao.17173.com/api/getGameScheCount?game_codes=20011
            yield scrapy.Request('http://hao.17173.com/api/getGameScheCount?game_codes='+result,callback=self.parse_notiy_num,meta={'item':item,'id':result})



    #获取排名（只有手游测评的时候调用）
    def parse_rank_num(self, response):
        item = response.meta['item']
        id = response.meta['id']

        rankNum = response.xpath('.').re('.*?"rank_num":(\d+).*?')
        if len(rankNum) > 0:
            item['rankNum'] = int(rankNum[0])
        else:
            item['rankNum'] = 0

        yield scrapy.Request('http://hao.17173.com/api/getGameScheCount?game_codes='+id,callback=self.parse_notiy_num,meta={'item':item,'id':id})


    #这里获取的是福利通知的数量
    def parse_notiy_num(self,response):
        # print(response.status,response.text)
        data = response.xpath('.').re('.*?\((.*?)\)')[0]
        json_data = json.loads(data)
        item = response.meta['item']
        id = response.meta['id']
        item['followMe'] = json_data['data'][id]

        yield item

