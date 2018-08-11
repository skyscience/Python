from scrapy_redis.spiders import RedisSpider
from example.items import ExampleItem
from scrapy import Request

class MySpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'myspider_redis'

    # 可以直接设置允许爬取的域
    allowed_domains = ['jobbole.com']

    redis_key = 'myspider:start_urls'


    # def __init__(self, *args, **kwargs):
    #     # Dynamically define the allowed domains list.
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(MySpider, self).__init__(*args, **kwargs)

    def parse(self, response):

        list = response.xpath('//div[@class="post floated-thumb"]')

        for node in list:
            item = ExampleItem()
            item['name'] = node.xpath('.//div[@class="post-thumb"]/a/@title').extract_first()
            item['detailurl'] = node.xpath('.//div[@class="post-thumb"]/a/@href').extract_first()
            yield item

        #取到当前页面下其他页面的ｕｒｌ
        next_urls = response.xpath('//a[@class="page-numbers"]/@href').extract()
        print(next_urls)
        for url in next_urls:
            yield Request(url=url,callback=self.parse)





