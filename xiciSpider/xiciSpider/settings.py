# -*- coding: utf-8 -*-

# Scrapy settings for xiciSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xiciSpider'

SPIDER_MODULES = ['xiciSpider.spiders']
NEWSPIDER_MODULE = 'xiciSpider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'xiciSpider (+http://www.yourdomain.com)'

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
# ITEM_PIPELINES 是个字典，key 是用来处理结果的类，value 表示执行顺序，值越小执行顺序越靠前，可以添加多个处理类，例如分别写入到 txt ，csv，json 文件中
ITEM_PIPELINES = {
    # 'xiciSpider.pipelines2txt.ToTxtPipeline': 100,
    # 'xiciSpider.pipelines.pipelines2txt.ToTxtPipeline': 100,
    # 'xiciSpider.pipelines.pipelines2csv.ToCsvPipeline': 101,
    'xiciSpider.pipelines.pipelines2json.ToJsonPipeline': 102,
    # 'xiciSpider.pipelines.pipelines2mysql.ToMysqlPipeline': 103,
    # 'xiciSpider.pipelines.pipelines2mongodb.ToMongoDbPipeline': 104,
}

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16
# 两次请求的时间间隔
DOWNLOAD_DELAY = 5

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'xiciSpider.middlewares.XicispiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'xiciSpider.middlewares.custom_user_agent.RandomUserAgent': 30,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,

    'xiciSpider.middlewares.custom_proxy.RandomProxy': 10,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 20

}
# scrapy.downloadermiddlewares.useragent


# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
LOG_LEVEL = 'INFO'
# 设置 LOG_LEVEL 防止 scrapy 抓取 item 完成总是打印:
# 2019-12-10 11:14:40 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.xicidaili.com/nn/1>
# { key:value,key:value}
