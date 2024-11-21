import json

from flask import Response

from repository.TempRepository import TempRepository


class TempService:
    def __init__(self, cust_id):
        self.repo = TempRepository()
        self.cust_id = cust_id

    def getFriendList(self):
        result = self.repo.getFriendList(self.cust_id)
        result = json.dumps(result, ensure_ascii=False).encode('utf8')
        return Response(result, content_type='application/json; charset=utf-8')

    def getUpdatedFriendList(self):
        result = self.repo.getUpdatedFriendList(self.cust_id)
        result = json.dumps(result, ensure_ascii=False).encode('utf8')
        return Response(result, content_type='application/json; charset=utf-8')

    def getBirthdayFriendList(self):
        result = {}
        result['today'] = self.repo.getNowBirthdayFriendList(self.cust_id)
        result['before'] = self.repo.getBeforeBirthdayFriendList(self.cust_id)
        result['after'] = self.repo.getAfterBirthdayFriendList(self.cust_id)
        result = json.dumps(result, ensure_ascii=False).encode('utf8')
        return Response(result, content_type='application/json; charset=utf-8')

    def getRecommendFriendList(self):
        result = self.repo.getRecommendedFriendList(self.cust_id)
        result = json.dumps(result, ensure_ascii=False).encode('utf8')
        return Response(result, content_type='application/json; charset=utf-8')