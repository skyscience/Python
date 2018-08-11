# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


#一周热榜
class YouxiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #公测状态
    testStatus = scrapy.Field()
    #名称
    name = scrapy.Field()
    #星级
    star = scrapy.Field()
    #封面
    coverImage = scrapy.Field()
    #ｔａｇｓ
    cate = scrapy.Field()
    #投票数量
    voteNum = scrapy.Field()
    #排名
    rankNum = scrapy.Field()
    #游戏类型
    type = scrapy.Field()
    #是否收费
    free = scrapy.Field()
    #公司名称
    company = scrapy.Field()
    #运营商
    operator = scrapy.Field()
    #描述
    desc = scrapy.Field()
    #语言
    language = scrapy.Field()
    #福利通知
    followMe = scrapy.Field()
    #注册
    regest = scrapy.Field()
    #下载地址
    download = scrapy.Field()
    #官方地址
    officialUrl = scrapy.Field()

    # 定义一个方法用来获取集合名称
    def get_collection_name(self):
        return 'hotgames'


#手游测评
class YouxiMobileItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #公测状态
    testStatus = scrapy.Field()
    #开测时间
    testTime = scrapy.Field()
    #测试名称
    testName = scrapy.Field()
    #名称
    name = scrapy.Field()
    #星级
    star = scrapy.Field()
    #封面
    coverImage = scrapy.Field()
    #ｔａｇｓ
    cate = scrapy.Field()
    #投票数量
    voteNum = scrapy.Field()
    #排名
    rankNum = scrapy.Field()
    #游戏类型
    type = scrapy.Field()
    #是否收费
    free = scrapy.Field()
    #公司名称
    company = scrapy.Field()
    #运营商
    operator = scrapy.Field()
    #描述
    desc = scrapy.Field()
    #语言
    language = scrapy.Field()
    #福利通知
    followMe = scrapy.Field()
    #注册
    regest = scrapy.Field()
    #下载地址
    download = scrapy.Field()
    #官方地址
    officialUrl = scrapy.Field()

    # 定义一个方法用来获取集合名称
    def get_collection_name(self):
        return 'testgames'



