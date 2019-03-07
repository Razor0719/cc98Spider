# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Cc98Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BoardItem(Cc98Item):
    id = scrapy.Field()
    name = scrapy.Field()


class TopicItem(Cc98Item):
    id = scrapy.Field()
    boardId = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    hitCount = scrapy.Field()
