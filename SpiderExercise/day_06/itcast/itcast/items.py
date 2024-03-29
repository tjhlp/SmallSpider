# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ItcastItem(scrapy.Item):
    # define the fields for your item here like:
    num = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
    author = scrapy.Field()
    time = scrapy.Field()


class YgItem(scrapy.Item):
    num = scrapy.Field()
    title = scrapy.Field()
    status = scrapy.Field()
    author = scrapy.Field()
    time = scrapy.Field()

