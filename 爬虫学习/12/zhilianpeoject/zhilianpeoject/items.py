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

    def insert_sql(self):
        insert_sql = 'INSERT INTO zhilianjob(jobtitle,salary,publishTime,workAdress,needpeople,jobDesc,companyName,companyUrl) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
        parmas = (self['jobtitle'],self['salary'],
                 self['publishTime'], self['workAdress'],
                 self['needpeople'], self['jobDesc'],
                 self['companyName'], self['companyUrl'],
                 )

        return insert_sql,parmas



class ZhilianCompanyItem(scrapy.Item):
    # 提取公司名称
    comapyName = scrapy.Field()
    # 公司性质
    comapnyClassfiy = scrapy.Field()
    # 公司规模
    companyMode = scrapy.Field()
    # 公司行业
    companyIndustry = scrapy.Field()
    # 公司地址
    companyAdress = scrapy.Field()
    # 公司介绍
    companyDesc = scrapy.Field()

    def insert_sql(self):
        # insert_sql =
        #     # self.cursor.execute(insert_sql,
        #     #                     (item['comapyName'], item['comapnyClassfiy'],
        #     #                      item['companyMode'], item['companyIndustry'],
        #     #                      item['companyAdress'], item['companyDesc'],
        #     #                      ))
        insert_sql = 'INSERT INTO zhiliancompany(comapyName,comapnyClassfiy,companyMode,companyIndustry,companyAdress,companyDesc) VALUES(%s,%s,%s,%s,%s,%s)'
        parmas = (self['comapyName'],self['comapnyClassfiy'],
                  self['companyMode'], self['companyIndustry'],
                  self['companyAdress'], self['companyDesc'],
                  )

        return insert_sql,parmas

