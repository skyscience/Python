# -*- coding: utf-8 -*-

# Scrapy settings for mk project


BOT_NAME = 'mk'

SPIDER_MODULES = ['mk.spiders']
NEWSPIDER_MODULE = 'mk.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mk (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True


ITEM_PIPELINES = {
   'mk.pipelines.MkPipeline': 300,
}

