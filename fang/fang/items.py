# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FangItemxf(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    father = scrapy.Field()
    city = scrapy.Field()
    hname = scrapy.Field()
    price = scrapy.Field()
    hstype = scrapy.Field()
    addr = scrapy.Field()
    fangyuan = scrapy.Field()
    xf_or_es = scrapy.Field()

class FangItemes(scrapy.Item):
    father = scrapy.Field()
    city = scrapy.Field()
    htitle = scrapy.Field()
    tel_shop = scrapy.Field()
    add_shop = scrapy.Field()
    label = scrapy.Field()
    price = scrapy.Field()
    xf_or_es = scrapy.Field()