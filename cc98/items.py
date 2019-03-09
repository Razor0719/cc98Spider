# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Cc98Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    pass


class BoardItem(Cc98Item):
    name = scrapy.Field()
    topicCount = scrapy.Field()
    postCount = scrapy.Field()
    description = scrapy.Field()


class TopicItem(Cc98Item):
    boardId = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    replyCount = scrapy.Field()
    hitCount = scrapy.Field()


class ContentItem(Cc98Item):
    boardId = scrapy.Field()
    content = scrapy.Field()
    floor = scrapy.Field()
    isLZ = scrapy.Field()
    length = scrapy.Field()
    parentId = scrapy.Field()
    userId = scrapy.Field()
    userName = scrapy.Field()
    time = scrapy.Field()
