import json

from flask import Response

from dto.content.ContentDTO import ContentDTO
from repository.ContentRepository import ContentRepository


class ContentService:
    def __init__(self):
        self.repo = ContentRepository()

    def getPopularContentList(self):
        result = self.repo.selectPopularContent()
        result = json.dumps(result, ensure_ascii=False).encode('utf8')
        return Response(result, mimetype='application/json, charset=utf-8')

    def getRecentlyContentList(self):
        result = self.repo.selectRecentlyContent()
        result = json.dumps(result, ensure_ascii=False).encode('utf8')
        return Response(result, mimetype='application/json, charset=utf-8')

    def getContentListByGenre(self, genre:str):
        result = self.repo.selectContentListByGenre(genre)
        result = json.dumps(result, ensure_ascii=False).encode('utf8')
        return Response(result, mimetype='application/json, charset=utf-8')