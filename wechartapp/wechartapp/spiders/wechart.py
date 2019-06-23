# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import WechartappItem

class WechartSpider(CrawlSpider):
    name = 'wechart'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d'), follow=True),
        Rule(LinkExtractor(allow=r'.+article-.+\.html'), callback='parse_detail', follow=False)
    )

    def parse_detail(self, response):

        title = response.xpath("//h1[contains(@class, 'ph')]/text()").extract()[0]
        author_p = response.xpath("//p[contains(@class, 'authors')]")
        author_name = author_p.xpath("./a/text()").get()
        author_time = author_p.xpath("./span/text()").get()
        article_content = response.xpath("//td[contains(@id, 'article_content')]//text()").getall()
        article_content = ''.join(article_content).strip()

        print(title, author_name, author_time, article_content)
        item = WechartappItem(title=title, author=author_name, pub_time=author_time, content=article_content)
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        yield item
