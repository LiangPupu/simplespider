# -*- coding: utf-8 -*-
import scrapy
from ..items import FangItemxf, FangItemes
from scrapy_redis.spiders import RedisSpider
from lxml import etree


class FangspiderSpider(RedisSpider):
    name = 'fangspider'
    allowed_domains = ['fang.com']
    # start_urls = ['https://www.fang.com/SoufunFamily.htm']
    redis_key = "fang:start_urls"

    def parse(self, response):
        for i in range(1,31):
            if i < 10:
                i = '0'+str(i)
            else:
                i = str(i)
            prov =response.xpath("//tr[contains(@id,'sffamily_B03_{}')]".format(i))
            father = prov.xpath("./td[2]/strong/text()").get()
            if father == "其它":
                continue

            for p in prov:
                # item = FangItem()
                urls = p.xpath("./td/a")
                for u in urls:
                    url = u.xpath("./@href").get()
                    # print("城市",url)
                    city = u.xpath("./text()").get()
                    # item['father'] = father
                    # item['city'] = city
                    # print(city,'-------',url)
                    yield scrapy.Request(url, callback=self.get_city, meta={'father': father, 'city': city})
            # print('-----')

    def get_city(self, response):
        houre_url = {}
        xf = response.xpath("//div[contains(@track-id, 'newhouse')]/div[contains(@class, 's4Box')]/a/@href").get()
        es = response.xpath("//div[contains(@track-id, 'esf')]/div[contains(@class, 's4Box')]/a/@href").get()
        # print("新房：", xf, "---------二手", es)
        if xf:
            houre_url['xf'] = xf
        if es:
            houre_url['es'] = es
        # print(houre_url)
        for key, value in houre_url.items():
            # print(key, '-----', value)
            # print(key, '-----', value.strip())
            response.meta['house_label'] = key
            if key == 'xf':
                yield scrapy.Request(value, callback=self.get_new_hours, meta=response.meta)
            if key == 'es':
                yield scrapy.Request(value, callback=self.get_es_hours, meta=response.meta)

    def get_new_hours(self, response):

        hours = response.xpath("//div[contains(@class, 'nlc_details')]")
        for h in hours:
            hname = h.xpath(".//div[contains(@class,'nlcd_name')]/a/text()").get().strip()
            price = str(h.xpath(".//div[contains(@class,'nhouse_price')]/span/text()").get())+" 元/㎡"
            hstype = h.xpath("normalize-space(.//div[contains(@class,'house_type')])").get()
            addr = h.xpath("normalize-space(.//div[contains(@class,'address')])").get()
            fangyuan = h.xpath("normalize-space(.//div[contains(@class,'fangyuan')])").get()

            item = FangItemxf(father=response.meta['father'],city=response.meta['city'],hname=hname,price=price,hstype=hstype,addr=addr,fangyuan=fangyuan,xf_or_es=response.meta['house_label'])
            # print(item['father'])

            yield item

        next_url = h.xpath("//div[contains(@class,'page')]//a[contains(@class,'next')]/@href").get()
        # print('url--------' + response.urljoin(next_url))
        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url),callback=self.get_new_hours,meta=response.meta)


    def get_es_hours(self,response):
        hours = response.xpath("//dl[contains(@dataflag,'bg')]")

        for h in hours:
            htitle = h.xpath("./dd/h4/text()").get().strip()
            tel_shop = h.xpath("normalize-space(.//p[contains(@class, 'tel_shop')])").get()
            add_shop = h.xpath("normalize-space(.//p[contains(@class, 'add_shop')])").get()
            label = h.xpath("normalize-space(.//p[contains(@class, 'label')])").get()
            price = h.xpath("normalize-space(.//dd[contains(@class, 'price_right')])").get()
            # print(htitle, tel_shop, add_shop, label, price)
            item = FangItemes(father=response.meta['father'],city=response.meta['city'],htitle=htitle,tel_shop=tel_shop,add_shop=add_shop,label=label,price=price,xf_or_es=response.meta['house_label'])
            yield item

        next_url = h.xpath("//div[contains(@class,'page_al')]/p[3]/a/@href").get()

        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url),callback=self.get_new_hours,meta=response.meta)



