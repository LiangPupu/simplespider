# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from .settings import USER_AGENT, PROXY_URL, PROXYES
import random
import requests
import json


class UserAgentDownloadMiddleware(object):

    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENT)
        request.headers['User-Agent'] = user_agent
        # print(user_agent)


class IPProxyDownloadMiddleware(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXYES)
        request.meta['proxy'] = proxy
        # print(proxy)


