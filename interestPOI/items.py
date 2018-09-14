# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class InterestpoiItem(scrapy.Item):
    # define the fields for your item here like:
    code = scrapy.Field()
    name = scrapy.Field()
    lon = scrapy.Field()
    lat = scrapy.Field()

class StaionPOIItem(scrapy.Item):
    # define the fields for your item here like:

    name_orien = scrapy.Field()
    # name_amap = scrapy.Field()
    lon = scrapy.Field()
    lat = scrapy.Field()
