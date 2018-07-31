# -*- coding: utf-8 -*-
import scrapy
from hrtencent.items import HrtencentItem
      
# 最基本的类，所有编写的爬虫必须继承这个类。
class HtSpider(scrapy.Spider):
    # 爬虫的识别名称，必须是唯一的，在不同的爬虫必须定义不同的名字。
    name = 'tencentJob'   
    # 是搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页，不存在的URL会被忽略。
    allowed_domains = ['hr.tencent.com']    
    url = "http://hr.tencent.com/position.php?&start=0"
    offset = 0
    # 爬取的URL元祖/列表。爬虫从这里开始抓取数据
    # 所以，第一次下载的数据将会从这些urls开始。其他子URL将会从这些起始URL中继承性生成。
    start_urls = [url + str(offset)]
    print(start_urls)   


    #  解析response，并返回Item或Requests（需指定回调函数）。Item传给Item pipline持久化 ，
    #  而Requests交由Scrapy下载，并由指定的回调函数处理（默认parse())，一直进行循环，直到处理完所有的数据为止。
    def parse(self, response):
        # 主要作用如下：  
        # 1. 负责解析返回的网页数据(response.body)，提取结构化数据(生成item)
	    # 2. 生成需要下一页的URL请求。


        # 获取当前列表页面的所有的节点  
        position_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")

        # 获取到节点再来筛
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


        # 将获取的数据交给pipelines
        yield item

        nexturls = response.xpath("//div[@class='pagenav']/a[@id='next']/@href").extract()
        url = "http://hr.tencent.com/" + nexturls[0]
        print(url)
        if nexturls[0]:
            yield scrapy.Request(url, callback=self.parse)
        else:
            print("爬虫任务结束")
