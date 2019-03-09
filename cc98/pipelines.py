# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class Cc98Pipeline(object):
    def __init__(self, mongoUrl, mongoPort, mongoDb):
        self.mongoUrl = mongoUrl
        self.mongoPort = mongoPort
        self.mongoDb = mongoDb

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongoUrl=crawler.settings.get('MONGO_URL'),
            mongoPort=crawler.settings.get('MONGO_PORT'),
            mongoDb=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongoUrl, self.mongoPort)
        self.db = self.client[self.mongoDb]

    def close_spider(self, spider):
        self.client.close()


class Cc98BoardsPipeline(Cc98Pipeline):

    def __init__(self, mongoUrl, mongoPort, mongoDb):
        super().__init__(mongoUrl, mongoPort, mongoDb)
        self.mongoCollection = 'boards'

    def open_spider(self, spider):
        super().open_spider(spider)
        self.collection = self.db[self.mongoCollection]

    def process_item(self, item, spider):
        self.collection.update({'id': item['id']}, item, upsert=True)
        return item


class Cc98TopicsPipeline(Cc98Pipeline):

    def __init__(self, mongoUrl, mongoPort, mongoDb):
        super().__init__(mongoUrl, mongoPort, mongoDb)
        self.mongoCollection = 'topics'

    def open_spider(self, spider):
        super().open_spider(spider)
        self.collection = self.db[self.mongoCollection]

    def process_item(self, item, spider):
        self.collection.update({'id': item['id']}, item, upsert=True)
        return item


class Cc98TopicPipeline(Cc98Pipeline):

    def __init__(self, mongoUrl, mongoPort, mongoDb):
        super().__init__(mongoUrl, mongoPort, mongoDb)
        self.mongoCollection = 'topic'

    def open_spider(self, spider):
        super().open_spider(spider)
        self.collection = self.db[self.mongoCollection]

    def process_item(self, item, spider):
        self.collection.update({'id': item['id']}, item, upsert=True)
        return item
