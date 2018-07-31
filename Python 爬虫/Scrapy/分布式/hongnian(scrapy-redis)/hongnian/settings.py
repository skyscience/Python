# -*- coding: utf-8 -*-



BOT_NAME = 'hongnian'
SPIDER_MODULES = ['hongnian.spiders']
NEWSPIDER_MODULE = 'hongnian.spiders'



#这个用的是scrapy-redis自带的去重组件，设置完之后就不会在使用scrapy模块下带的去重了
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#这个用的是scrapy-redis自带的调度器，设置完之后就不会在使用scrapy模块下带的调度器了
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#这个是保存暂停的开启的状态，为true表示会保存相关记录，下次请求会接着上一次
SCHEDULER_PERSIST = True
#第一个是scrapy-redis默认的队列（有优先级顺序）（一般使用默认的请求队列）
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# Obey robots.txt rules
ROBOTSTXT_OBEY = True



ITEM_PIPELINES = {
   'hongnian.pipelines.HongnianPipeline': 300,
   'scrapy_redis.pipelines.RedisPipeline': 400,
}



REDIS_HOST = '192.168.15.110'
REDIS_PORT = 6379