import json

import math
import scrapy

from cc98.items import TopicItem
from cc98.spiders.parse import Cc98parse


class cc98Topics(scrapy.Spider):
    name = 'cc98Topics'
    custom_settings = {
        'ITEM_PIPELINES': {
            'cc98.pipelines.Cc98TopicsPipeline': 300,
        }
    }

    def __init__(self, boardId=None, *args, **kwargs):
        super(cc98Topics, self).__init__(*args, **kwargs)
        self.boardId = boardId

    def start_requests(self):
        yield scrapy.Request('https://api.cc98.org/board/%s' % self.boardId,
                             method='GET',
                             callback=self.parse_board)

    def parse_board(self, response):
        pages = math.ceil(json.loads(response.body).get('topicCount') / 20)
        for offset in range(0, 500):
            yield scrapy.Request(
                'https://api.cc98.org/board/%s/topic?from=%s&size=20' % (self.boardId, offset * 20),
                method='GET',
                headers={'Referer': 'http://www.cc98.org/board/%s' % self.boardId})

    def parse(self, response):
        topics = json.loads(response.body)
        for topic in topics:
            date = topic.get('time')
            topic_item = TopicItem()
            topic_item['id'] = topic.get('id')
            topic_item['boardId'] = topic.get('boardId')
            topic_item['title'] = topic.get('title')
            topic_item['replyCount'] = topic.get('replyCount')
            topic_item['hitCount'] = topic.get('hitCount')
            Cc98parse.parse_tz(topic_item, date)
            yield topic_item
