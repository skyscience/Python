# -*- coding: utf-8 -*-


# 项目实现的bot的名字(也是项目名称)
BOT_NAME = 'hrtencent'


SPIDER_MODULES = ['hrtencent.spiders']
NEWSPIDER_MODULE = 'hrtencent.spiders'


# 爬取的默认User-Agent，除非被覆盖。
USER_AGENT = [
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
    ]


# PROXIES = [
#   {'ip_port': '111.8.60.9:8123', 'user_passwd': 'user1:pass1'},
#   {'ip_port': '101.71.27.120:80', 'user_passwd': 'user2:pass2'},
#   {'ip_port': '122.96.59.104:80', 'user_passwd': 'user3:pass3'},
#   {'ip_port': '122.224.249.122:8088', 'user_passwd': 'user4:pass4'},
# ]


# Obey robots.txt rules
ROBOTSTXT_OBEY = False



# Scrapy downloader 并发请求(concurrent requests)的最大值。
# CONCURRENT_REQUESTS = 32



# 爬取网站最大允许的深度(depth)值。如果为0，则没有限制。
DOWNLOAD_DELAY = 3



# 对单个网站进行并发请求的最大值。
#CONCURRENT_REQUESTS_PER_DOMAIN = 16



# 对单个IP进行并发请求的最大值。如果非0，则忽略 CONCURRENT_REQUESTS_PER_DOMAIN 设定， 
# 使用该设定。 也就是说，并发限制将针对IP，而不是网站。 
# 该设定也影响 DOWNLOAD_DELAY: 如果 CONCURRENT_REQUESTS_PER_IP 非0，下载延迟应用在IP而不是网站上。
#CONCURRENT_REQUESTS_PER_IP = 16




# 禁用Cookies
COOKIES_ENABLED = False




#  表明 telnet 终端 (及其插件)是否启用的布尔值。
#TELNETCONSOLE_ENABLED = False




# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:58.0) Gecko/20100101 Firefox/58.0',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}




# 保存项目中启用的pipeline及其顺序的字典。
# 该字典默认为空，值(value)任意，不过值(value)习惯设置在0-1000范围内，值越小优先级越高。
ITEM_PIPELINES = {
   'hrtencent.pipelines.HrtencentPipeline': 300,
}


#  该设置是一个字典(dict)，键为中间件类的路径，值为其中间件的顺序(order)。
#DOWNLOADER_MIDDLEWARES = {
#    'hrtencent.middlewares.HrtencentDownloaderMiddleware': 543,
#}



# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'hrtencent.middlewares.HrtencentSpiderMiddleware': 543,
#}



# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
