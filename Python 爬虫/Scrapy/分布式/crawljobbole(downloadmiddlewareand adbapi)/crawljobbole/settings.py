# -*- coding: utf-8 -*-

# Scrapy settings for crawljobbole project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

# 项目的名字,这将用来构造默认 User-Agent,同时也用来log,当您使用 startproject 命令创建项目时其也被自动赋值。
BOT_NAME = 'crawljobbole'

##Scrapy搜索spider的模块列表
SPIDER_MODULES = ['crawljobbole.spiders']

NEWSPIDER_MODULE = 'crawljobbole.spiders'

# 爬取的默认User-Agent
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'crawljobbole (+http://www.yourdomain.com)'

# 如果启用,Scrapy将会采用 robots.txt策略
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

#Scrapy downloader 并发请求(concurrent requests)的最大值,默认: 16
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 为同一网站的请求配置延迟（默认值：0）
#下载器在下载同一个网站下一个页面前需要等待的时间,该选项可以用来限制爬取速度,减轻服务器压力。同时也支持小数:0.25 以秒为单位
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#下载延迟设置只有一个有效
# 对单个网站进行并发请求的最大值。
#CONCURRENT_REQUESTS_PER_DOMAIN = 16

# 对单个IP进行并发请求的最大值。如果非0,则忽略
# CONCURRENT_REQUESTS_PER_DOMAIN 设定,使用该设定。
# 也就是说,并发限制将针对IP,而不是网站。该设定也影响 DOWNLOAD_DELAY:
# 如果 CONCURRENT_REQUESTS_PER_IP 非0,下载延迟应用在IP而不是网站上。
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#禁用Cookie（默认情况下启用）
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#禁用Telnet控制台（默认启用）
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:

# 覆盖默认请求标头：
DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',
  'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36',
  'referer':'https://www.zhihu.com/'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#爬虫中间件
#SPIDER_MIDDLEWARES = {
#    'crawljobbole.middlewares.CrawljobboleSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#下载中间件
# DOWNLOADER_MIDDLEWARES = {
#     'crawljobbole.middlewares.RandomUserAgentMiddleware':300,
#
#     'crawljobbole.middlewares.RandomIPMiddleware': 302,
#
#     'crawljobbole.middlewares.CrawljobboleDownloaderMiddleware': None,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#启用或者禁用扩展
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'crawljobbole.pipelines.CrawljobbolePipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html

# 启用和配置AutoThrottle扩展（默认情况下禁用）
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
#初始下载延迟
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#在高延迟的情况下设置的最大下载延迟
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#Scrapy请求的平均数量应该并行发送每个远程服务器
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#启用显示所收到的每个响应的调节统计信息：
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#启用和配置HTTP缓存（默认情况下禁用）
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

USERAGENTS = [
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
]

PROXIES = [
    {'IP':'https://112.95.88.50:9999','user_pwd':'ljh:1234567'},
    {'IP':'https://112.95.88.50:9999','user_pwd':None},
    {'IP':'https://112.95.88.50:9999','user_pwd':None},
    {'IP':'https://112.95.88.50:9999','user_pwd':None},
]

COOKIES = [
    {'ALIPAYBUMNGJSESSIONID':'GZ00hCopoavt2A0DgtoUE8151luAXXmobilecodecGZ00','ctoken':'fozhT2P3s_dT2dTJ','zone':'GZ00C'},
    {'ALIPAYBUMNGJSESSIONID': 'GZ00hCopoavt2A0DgtoUE8151luAXXmobilecodecGZ00', 'ctoken': 'fozhT2P3s_dT2dTJ','zone':'GZ00C'},
    {'ALIPAYBUMNGJSESSIONID':'GZ00hCopoavt2A0DgtoUE8151luAXXmobilecodecGZ00','ctoken':'fozhT2P3s_dT2dTJ','zone':'GZ00C'},
    {'ALIPAYBUMNGJSESSIONID':'GZ00hCopoavt2A0DgtoUE8151luAXXmobilecodecGZ00','ctoken':'fozhT2P3s_dT2dTJ','zone':'GZ00C'},
]

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PWD = 'ljh1314'
MYSQL_DB = 'jobbole'
MYSQL_PORT = 3306