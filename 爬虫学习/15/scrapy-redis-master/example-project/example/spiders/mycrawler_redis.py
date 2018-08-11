from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy_redis.spiders import RedisCrawlSpider

from example.items import ExampleItem

class MyCrawler(RedisCrawlSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'mycrawler_redis'
    redis_key = 'mycrawler:start_urls'

    rules = [
        Rule(LinkExtractor(allow=r'page/\d+/'), callback='parse_directory', follow=True),
        ]

    #可以直接设置允许爬取的域
    allowed_domains = ['jobbole.com']

    #动态获取允许爬取的域

    # def __init__(self, *args, **kwargs):
    #     # Dynamically define the allowed domains list.
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(MyCrawlyer, self).__init__(*args, **kwargs)

    def parse_directory(self, response):
        list = response.xpath('//div[@class="post floated-thumb"]')
        for node in list:
            item = ExampleItem()
            item['name'] = node.xpath('//div[@class="post-thumb"]/a/@title').extract_first()

            item['url'] = node.xpath('//div[@class="post-thumb"]/a/@href').extract_first()

            yield item
