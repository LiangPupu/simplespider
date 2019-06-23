# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from .settings import USER_AGENT
import random


class UserAgentDownloadMiddleware(object):

    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENT)
        request.headers['User-Agent'] = user_agent

