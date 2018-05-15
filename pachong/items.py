# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class Mp4Item(scrapy.Item):
    mp4 = scrapy.Field()
    name = scrapy.Field()

class PachongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    href = scrapy.Field()
    text = scrapy.Field()

class MyImgItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_paths = scrapy.Field()