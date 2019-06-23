# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import BossItem


class ZhipingSpider(CrawlSpider):
    name = 'zhiping'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101280100/?query=python&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+query=python&page=\d'), follow=True),
        Rule(LinkExtractor(allow=r'.+job_detail/.+\.html'), callback="parse_item", follow=False),
    )

    def parse_item(self, response):
        title = response.xpath("//div[contains(@class, 'info-primary')]//div[contains(@class, name)]/h1/text()").get()
        salary = response.xpath("//div[contains(@class, 'info-primary')]//div[contains(@class, name)]/span/text()").get()
        demand = response.xpath("//div[contains(@class, 'job-primary')]//div[contains(@class, 'info-primary')]/p/text()").getall()
        addr = demand[0]
        job_year = demand[1]
        edu = demand[2]
        master = response.xpath("//h2[contains(@class, 'name')]/text()").get()
        company_name = response.xpath("//div[contains(@class, 'job-sec')]/div[contains(@class, 'name')]/text()").get()
        text = response.xpath("//div[contains(@class, 'job-sec')][1]//text()").getall()
        text = ''.join(text).strip()
        item = BossItem(title=title, salary=salary, addr=addr, job_year=job_year, edu=edu, master=master, company_name=company_name, text=text)

        yield item
