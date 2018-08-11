# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class ZhilianprojectItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     jobName =
#     pass

class ZhilianJobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #职位名称
    jobName = scrapy.Field()
    #职位薪资
    salary = scrapy.Field()
    #发布时间
    publishTime = scrapy.Field()
    #职位描述
    jobDesc = scrapy.Field()
    #地址
    address = scrapy.Field()
    #公司名称
    company = scrapy.Field()


    def insertdata(self):

        insert_str = """
          INSERT INTO jobs(jobname,salary,publishtime,jobdesc,address,company)
          VALUES(%s,%s,%s,%s,%s,%s)
        """

        parmas = (self['jobName'],self['salary'],self['publishTime'],
                  self['jobDesc'],self['address'],self['company'])

        return insert_str,parmas


class ZhilianCompanyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #职位名称
    companyName = scrapy.Field()
    #职位薪资
    companyType = scrapy.Field()
    #发布时间
    companyModel = scrapy.Field()
    #职位描述
    trade = scrapy.Field()
    #地址
    address = scrapy.Field()

    def insertdata(self):
        insert_str = """
          INSERT INTO company(companyname,companytype,companymodel,trade,address)
          VALUES(%s,%s,%s,%s,%s)
        """

        parmas = (self['companyName'], self['companyType'], self['companyModel'],
                  self['trade'], self['address'])

        return insert_str, parmas



