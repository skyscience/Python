# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

#表示启用scrapy_redis自定义的去重组件，不使用ｓｃｒａｐｙ默认的去重组件
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#表示启用scrapy_redis自定义的调度器，不使用ｓｃｒａｐｙ默认的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#设置为ｔｕｒｅ表示会保存请求的记录，可以暂停和恢复。
SCHEDULER_PERSIST = True
#scrapy_redis默认的队列，有优先级。存的时候会按照优先级存储，取的时候会按照优先级取值
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#就是一个队列，相当于一个栈结构，先进先出
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#是一个类似堆的结构，先进后出
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"


#scrapy_redis.pipelines.RedisPipeline 激活这个管道，它能够实现将从
# 服务器获取到的ｉｔｅｍ存储在ｍａｔｓｅｒ的ｒｅｄｉｓ数据库中
ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

#打印ｌｏｇ日志的等级
LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
# 设置下载延迟
DOWNLOAD_DELAY = 1

#配置ｒｅｄｉｓ数据库的ｉｐ（ｍａｓｔｅｒ端）
REDIS_HOST = '192.168.15.110'
#配置ｒｅｄｉｓ数据库的端口号(ｍａｓｔｅｒ端）
REDIS_PORT = 6379