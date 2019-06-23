# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter

class FangPipeline(object):
    def __init__(self):
        self.xf = open('xf.json','wb')
        self.es = open('es.json', 'wb')
        self.xf_ex = JsonLinesItemExporter(self.xf, ensure_ascii=False, encoding='utf-8')
        self.es_ex = JsonLinesItemExporter(self.es, ensure_ascii=False, encoding='utf-8')

    def process_item(self, item, spider):

        if item['xf_or_es']=='xf':
            self.xf_ex.export_item(item)
        elif item['xf_or_es']=='es':
            self.es_ex.export_item(item)
        return item

    def close(self):
        self.xf.close()
        self.es.close()
