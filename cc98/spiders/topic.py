import json

import math
import scrapy

from cc98.items import ContentItem
from cc98.spiders.parse import Cc98parse


class cc98Topic(scrapy.Spider):
    name = 'cc98Topic'
    custom_settings = {
        'ITEM_PIPELINES': {
            'cc98.pipelines.Cc98TopicPipeline': 300,
        }
    }

    def __init__(self, topicId=None, *args, **kwargs):
        super(cc98Topic, self).__init__(*args, **kwargs)
        self.topicId = topicId

    def start_requests(self):
        yield scrapy.Request('https://api.cc98.org/topic/%s' % self.topicId,
                             method='GET',
                             callback=self.parse_topic)

    def parse_topic(self, response):
        pages = math.ceil(json.loads(response.body).get('replyCount') / 10)
        for offset in range(0, pages):
            yield scrapy.Request(
                'https://api.cc98.org/Topic/%s/post?from=%s&size=10' % (self.topicId, offset * 20),
                method='GET',
                headers={'Referer': 'http://www.cc98.org/topic/%s/%d' % (self.topicId, offset + 1)})

    def parse(self, response):
        print(response.url)
        contents = json.loads(response.body)
        for content in contents:
            if content.get('isLZ'):
                date = content.get('time')
                content_item = ContentItem()
                content_item['id'] = content.get('id')
                content_item['boardId'] = content.get('boardId')
                content_item['topicId'] = content.get('topicId')
                content_item['content'] = content.get('content')
                content_item['floor'] = content.get('floor')
                content_item['isLZ'] = content.get('isLZ')
                content_item['length'] = content.get('length')
                content_item['parentId'] = content.get('parentId')
                content_item['userId'] = content.get('userId')
                content_item['userName'] = content.get('userName')
                Cc98parse.parse_tz(content_item, date)
                yield content_item
