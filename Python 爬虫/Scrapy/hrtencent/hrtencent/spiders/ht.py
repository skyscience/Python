# -*- coding: utf-8 -*-
import scrapy
from hrtencent.items import HrtencentItem

class HtSpider(scrapy.Spider):
    name = 'tencentJob'
    allowed_domains = ['hr.tencent.com']
    url = "http://hr.tencent.com/position.php?&start=0"
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        # print(response.body)
        # with open("tencentJob.html","wb") as file:
        # file.write(response.body)
        #
        # pass
        position_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        for each in position_list:
        # 获取职位名称
            name = each.xpath("./td[1]/a/text()").extract_first("")
            # 获取详情链接
            link = each.xpath("./td[1]/a/@href").extract_first("")
            # 获取职位类别
            positionType = each.xpath("./td[2]/text()").extract_first("")
            # 获取招聘人数
            peopleNum = each.xpath("./td[3]/text()").extract_first("")
            # 获取工作地点
            workLoaction = each.xpath("./td[4]/text()").extract_first("")
            # 获取发布时间
            publishTime = each.xpath("./td[5]/text()").extract_first("")

            print(name)
            print(link)
            print(positionType)
            print(peopleNum)
            print(workLoaction)
            print(publishTime)

        # 初始化模型对像
        item = HrtencentItem()
        item['name'] = name
        item['link'] = link
        item['positionType'] = positionType
        item['peopleNum'] = peopleNum
        item['workLoaction'] = workLoaction
        item['publishTime'] = publishTime

        yield item

        nexturls = response.xpath("//div[@class='pagenav']/a[@id='next']/@href").extract()
        url = "http://hr.tencent.com/" + nexturls[0]
        print(url)
        if nexturls[0]:
            yield scrapy.Request(url, callback=self.parse)
        else:
            print("爬虫任务结束")
