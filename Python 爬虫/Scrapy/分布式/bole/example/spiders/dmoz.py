from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from example.items import ExampleItem


class DmozSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'dmoz'
    allowed_domains = ['jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/page/1/']

    rules = [
        Rule(LinkExtractor(allow=r'page/\d+/'), callback='parse_directory', follow=True),
    ]

    def parse_directory(self, response):
        print(response.status)

        list = response.xpath('//div[@class="post floated-thumb"]')
        for node in list:
            item = ExampleItem()
            item['name'] = node.xpath('//div[@class="post-thumb"]/a/@title').extract_first()

            item['url'] = node.xpath('//div[@class="post-thumb"]/a/@href').extract_first()

            yield item


