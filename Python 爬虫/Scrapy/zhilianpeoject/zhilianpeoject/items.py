# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#目标文件，我们一般在这里定义目标数据结构
class ZhilianpeojectItem(scrapy.Item):
    # define the fields for your item here like:
    # 职位名称
    jobtitle = scrapy.Field()
    # 月薪
    salary = scrapy.Field()
    # 发布日期
    publishTime = scrapy.Field()
    # 工作地点
    workAdress = scrapy.Field()
    # 招聘人数
    needpeople = scrapy.Field()
    # 职位描述
    jobDesc = scrapy.Field()
    # 公司名称
    companyName = scrapy.Field()
    # 公司详情的ｕｒｌ
    companyUrl = scrapy.Field()
    pass
