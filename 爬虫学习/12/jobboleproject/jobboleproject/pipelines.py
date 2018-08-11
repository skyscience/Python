# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.contrib.pipeline.images import ImagesPipeline
import scrapy
from scrapy.exceptions import DropItem
import os
from scrapy.utils.project import get_project_settings

image_store = get_project_settings().get('IMAGES_STORE')
class JobboleImagePipeline(ImagesPipeline):



    def get_media_requests(self, item, info):
        image_url = item['image_url']
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        print('下载图片')
        # print(results)
        # [(True,
        #  {'checksum': '2b00042f7481c7b056c4b410d28f33cf',
        #   'path': 'full/7d97e9 8f8af710c7e7fe703abc8f639e0ee507c4.jpg',
        #   'url':'图片连接'})]
        path =[dict['path'] for status,dict in results if status]
        if not path:
            raise DropItem('图片路径不存在')
        else:
            os.rename(image_store+'/'+path[0],image_store+'/'+item['title']+'.jpg')
            item['image_path'] = image_store+'/'+item['title']+'jpg'

        return item


class JobboleprojectPipeline(object):
    def process_item(self, item, spider):
        return item
