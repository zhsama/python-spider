# from Proxypool.proxypool.db import RedisClient
# from .crawler import Crawler
#
# POOL_UPPER_THRESHOLD = 1000
#
#
# class getter():
#     def __init__(self):
#         self.redis = RedisClient()
#         self.crawler = Crawler()
#
#     def is_over_threshould(self):
#         """
#         判断是否达到代理池限制
#         :return:
#         """
#         if self.redis.count() >= POOL_UPPER_THRESHOLD:
#             return True
#         else:
#             return False
#
#     def run(self):
#         print('获取器开始执行')
#         if not self.is_over_threshould():
#             for callback_label in range(self.crawler.__CrawFuncCount__):
#                 callback = self.crawler.__CrawFunc__[callback_label]
#                 proxies = self.crawler.get_proxies(callback)
#                 for proxy in proxies:
#                     self.redis.add(proxy)
#
#
#

from Proxypool.proxypool.tester import Tester
from Proxypool.proxypool.db import RedisClient
from Proxypool.proxypool.crawler import Crawler
from Proxypool.proxypool.setting import *
import sys


class Getter():
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()

    def is_over_threshold(self):
        """
        判断是否达到了代理池限制
        """
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        print('获取器开始执行')
        if not self.is_over_threshold():
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                callback = self.crawler.__CrawlFunc__[callback_label]
                # 获取代理
                proxies = self.crawler.get_proxies(callback)
                sys.stdout.flush()
                for proxy in proxies:
                    self.redis.add(proxy)
