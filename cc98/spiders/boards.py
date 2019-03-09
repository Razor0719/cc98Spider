import json

import scrapy

from cc98.items import BoardItem


class cc98Login(scrapy.Spider):
    name = 'cc98Boards'
    custom_settings = {
        'ITEM_PIPELINES': {
            'cc98.pipelines.Cc98BoardPipeline': 300,
        }
    }

    def start_requests(self):
        return [scrapy.FormRequest("https://api.cc98.org/Board/all",
                                   method='GET',
                                   callback=self.all_boards)]

    def all_boards(self, response):
        body = json.loads(response.body)
        for boards in body:
            for board in boards.get('boards'):
                board_item = BoardItem()
                board_item['id'] = board.get('id')
                board_item['name'] = board.get('name')
                board_item['topicCount'] = board.get('topicCount')
                board_item['postCount'] = board.get('postCount')
                board_item['description'] = board.get('description')
                yield board_item
