# -*- coding: utf-8 -*-
import os

import scrapy
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError, TCPTimedOutError

from xiciSpider.items import GetproxyItem
from xiciSpider.custLog import CustLog
from time import sleep


class ProxyXiciSpider(scrapy.Spider):

    name = "proxyXiciSpider"
    allowed_domains = ["xicidaili.com"]
    # nn: 国内高匿代理		nt: 国内普通代理	wn: 国内 HTTPS 代理		wt: 国内 HTTP 代理
    wds = ['nn', 'nt', 'wn', 'wt']
    pages = 20
    sleepTime = 10
    start_urls = []
    download_delay = 5
    myLog = CustLog()

    for type in wds:
        for i in range(1, pages + 1):
            start_urls.append('http://www.xicidaili.com/' + type + '/' + str(i))

    def start_requests(self):
        for url in self.start_urls:
            print('开始请求: request url = %s' % url)
            sleep(self.sleepTime)  # 休眠, 防止封ip
            yield scrapy.Request(url, callback=self.parse_httpbin,
                                 errback=self.errback_httpbin,
                                 dont_filter=True)

    def parse_httpbin(self, response):
        self.myLog.info('响应成功, url={}'.format(response.url))
        return self.processData(response)

    def errback_httpbin(self, failure):
        # log all failures
        self.myLog.info('响应失败, {}'.format(repr(failure)))
        self.myLog.info(repr(failure))

        if failure.check(HttpError):
            response = failure.value.response
            self.myLog.info('HttpError错误 on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.myLog.info('DNSLookupError错误 on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.myLog.info('TimeoutError错误 on %s', request.url)

    # 重写了 start_requests() 处理 response，所以这个方法不会执行
    def parse(self, response):
        self.myLog.info('响应成功 parse() 的 response={}'.format(response))
        pass

    def processData(self, response):
        # self.myLog.debug('ProxyXiciSpider parse response=%s' % (response.text))

        subSelector = response.xpath('//tr[@class=""]|//tr[@class="odd"]')
        items = []
        for sub in subSelector:
            item = GetproxyItem()

            item['ip'] = sub.xpath('.//td[2]/text()').extract()[0]
            item['port'] = sub.xpath('.//td[3]/text()').extract()[0]
            item['type'] = sub.xpath('.//td[5]/text()').extract()[0]
            if sub.xpath('.//td[4]/a/text()'):
                item['loction'] = sub.xpath('//td[4]/a/text()').extract()[0]
            else:
                item['loction'] = sub.xpath('.//td[4]/text()').extract()[0]
            item['protocol'] = sub.xpath('.//td[6]/text()').extract()[0]
            item['source'] = 'xicidaili'
            items.append(item)
        return items


if __name__ == "__main__":
    os.system("scrapy crawl ProxyXiciSpider")