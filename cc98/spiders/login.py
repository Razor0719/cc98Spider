import json

import scrapy


class cc98Login(scrapy.Spider):
    name = 'cc98Login'

    def start_requests(self):
        return [scrapy.FormRequest("https://openid.cc98.org/connect/token",
                                   method='POST',
                                   formdata={'client_id':'',
                                             'client_secret':'',
                                             'username': '',
                                             'password': '',
                                             'grant_type': 'password',
                                             'scope': 'cc98-api openid offline_access'},
                                   callback=self.logged_in)]

    def logged_in(self, response):
        body = json.loads(response.body)
        print(body.get('access_token'))
