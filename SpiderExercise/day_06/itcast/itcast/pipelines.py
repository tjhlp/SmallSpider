# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
from pymongo import *
from itcast.items import YgItem, ItcastItem


class ItcastPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonPipeline(object):
    def open_spider(self, spider):
        self.out_file = open('result.json', 'w', encoding='utf-8')
        self.out_file.write('[')

    def process_item(self, item, spider):
        print("JsonPipeline:", item)
        if isinstance(item, YgItem):
            json.dump(dict(item), self.out_file, ensure_ascii=True)
        return item

    def close_spider(self, spider):
        self.out_file.write(']')
        self.out_file.close()


class MongodbPipeline(object):

    def open_spider(self, spider):
        client = MongoClient(host='192.168.146.134', port=27017)
        self.db = client.test1

    def process_item(self, item, spider):
        if isinstance(item, ItcastItem):
            self.db.itcast_items.insert(dict(item))
            print("MongodbPipeline:", item)

        elif isinstance(item, YgItem):
            self.db.yg.insert(dict(item))
