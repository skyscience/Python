# -*- coding: utf-8 -*-
import scrapy
from test2.items import Test2Item
from urllib import parse
import re


class TsSpider(scrapy.Spider):
    name = 'ts'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']
    


    def parse(self, response):
        # filename = 'jobbole.html'    
        # open(filename,'wb').write(response.body)

        post_nodes = response.css("#archive .floated-thumb .post-thumb a")
        for post_node in post_nodes:
            # 这里是异步的下载
            image_url = post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")
            yield scrapy.Request(url=parse.urljoin(response.url, post_url), meta={"front_image_url": image_url},callback=self.parse_detail)

    def parse_detail(self,response):
        # print(response)
        # 使用xpath语法或者css语法提取网页的相关信息
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]
        create_date = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip().replace("·","").strip()
        url = response.url
        # http://blog.jobbole.com/113949/ 获取文章的id
        object_id = re.match(".*?(\d+).*", url).group(1)
        praise_nums = response.xpath("//span[contains(@class,'vote-post-up')]/h10/text()").extract()[0]

        bookmark_nums = response.xpath("//span[contains(@class,'bookmark-btn')]/text()").extract()[0]
        match_bookmark_nums = re.match(".*?(\d+).*",bookmark_nums)
        if match_bookmark_nums:
            bookmark_nums = int(match_bookmark_nums.group(1))
        else:
            bookmark_nums = 0
            comment_nums = response.xpath("//a[@href='#article-comment']/span/text()").extract()[0]
        match_comment_nums = re.match(".*?(\d+).*",comment_nums)
        if match_comment_nums:
            comment_nums = int(match_comment_nums.group(1))
        else:
            comment_nums = 0
            content = response.xpath("//div[@class='entry']").extract()[0]

        tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']//a/text()").extract()
        # 过滤评论标签
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ",".join(tag_list)

        item = Test2Item()
        item['title'] = title
        # 创建时间
        item['create_date'] = create_date
        # 文章地址
        item['url'] = url
        # id
        item['url_object_id'] = object_id
        # 文章图片
        item['front_image_url'] = response.meta.get("front_image_url","")
        # 点赞数
        item['praise_nums'] = praise_nums
        # 收藏数
        item['bookmark_nums'] = bookmark_nums
        # 评论数
        item['comment_nums'] = comment_nums
        # 文章内容
        item['content'] = content
        # 标签
        item['tags'] = tags

        print(item)

        # 返回数据，不经过pipelines
        # return item
        # 将获取的数据交给pipelines
        yield item