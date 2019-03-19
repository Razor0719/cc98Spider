import jieba
import pymongo

class Cc98WordCloud(object):
    def __init__(self, mongoUrl, mongoPort, mongoDb):
        self.mongoUrl = mongoUrl
        self.mongoPort = mongoPort
        self.mongoDb = mongoDb
        self.text = ''

    def connect_mongo(self):
        self.client = pymongo.MongoClient(self.mongoUrl, self.mongoPort)
        self.db = self.client[self.mongoDb]

    def cut_text(self, content):
        return ' '.join(jieba.cut_for_search(content))

    def load_img(self):
        pass

    def generate_wordcloud(self, boardId, startTime, endTime):
        pass
