# -*- coding: utf-8 -*-
import scrapy
import json
import re
import time
from baidulvyou.items import BaidulvyouItem
import re

from scrapy.linkextractors import LinkExtractor

class YoujiSpider(scrapy.Spider):
    name = 'youji'
    allowed_domains = ['baidu.com']
    #https://lvyou.baidu.com/main/ajax/rank/prod?type=1&t=1532002795134
    #https://lvyou.baidu.com/search/ajax/searchnotes?format=ajax&type=0&pn=35&rn=10&t=1532002910430
    #https://lvyou.baidu.com/search/ajax/searchnotes?format=ajax&type=0&pn=35&rn=10&t=1532003077405
    #https://lvyou.baidu.com/search/ajax/searchnotes?format=ajax&type=0&pn=45&rn=10&t=1532003120773
    #https://lvyou.baidu.com/search/ajax/searchnotes?format=ajax&type=0&pn=55&rn=10&t=1532003150104
    start_urls = ['https://lvyou.baidu.com/search/ajax/searchnotes?format=ajax&type=0&pn=15&rn=10&t=1532002910430']

    def parse(self, response):
        print(response.status)

        node_list = json.loads(response.text)['data']['notes_list']
        if node_list == 0:
            print('没有数据了')
        else:
            for node in node_list:
                item = BaidulvyouItem()
                #//gss0.baidu.com/9vo3dSag_xI4khGko9WTAnF6hhy/lvpics/w%3D300/sign=4aadce97bd4543a9f51bfccc2e168a7b/63d9f2d3572c11df5058af40692762d0f603c2cc.jpg
                #//gss0.baidu.com/9vo3dSag_xI4khGko9WTAnF6hhy/lvpics/w%3D300/sign=4aadce97bd4543a9f51bfccc2e168a7b/63d9f2d3572c11df5058af40692762d0f603c2cc.jpg
                #//gss0.baidu.com/-Po3dSag_xI4khGko9WTAnF6hhy/lvpics/w%3D300/sign=7ec506858bcb39dbc1c06156e01609a7/1f178a82b9014a90550224d2a3773912b31beea5.jpg
                item['image_url'] = 'https:' + node['full_url']
                # # 游记标题
                item['note_title'] = node['title']
                # # 用户名称
                item['user_name'] = node['user_nickname']
                # # 点赞数量
                item['zan_num'] = int(node['mark'])
                # 内容
                item['content'] = node['content'].replace('&nbsp','').replace("'",'')

                # 观看数量
                item['visit_num'] = int(node['view_count'])
                # # 评论数量
                item['comment_num'] = int(node['recommend_count'])
                # # 回复内容
                item['replay_content'] = re.findall(re.compile('.*?<p>(.*?)</p>.*?'),node['last_post']['content'])

                if len(item['replay_content']) > 0:
                    item['replay_content'] = item['replay_content'][0]
                else:
                    item['replay_content'] = '未知'

                yield item

            # pattern = re.compile('.*?pn=(\d+).*?')
            # current_num = re.findall(pattern,response.url)[0]
            # nextpage_num = int(current_num)+10
            # t = int(time.time()*1000)
            # print(t,nextpage_num)
            #
            # next_url = 'https://lvyou.baidu.com/search/ajax/searchnotes?format=ajax&type=0&pn=%d&rn=10&t=%d' % (nextpage_num,t)
            #
            # yield scrapy.Request(next_url,callback=self.parse)

