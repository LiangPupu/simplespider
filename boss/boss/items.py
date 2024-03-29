# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BossItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    salary = scrapy.Field()
    addr = scrapy.Field()
    job_year = scrapy.Field()
    edu = scrapy.Field()
    master = scrapy.Field()
    company_name = scrapy.Field()
    text = scrapy.Field()
