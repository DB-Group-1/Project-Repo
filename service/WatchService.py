import json

from flask import Response

from repository.ContentRepository import ContentRepository
from repository.UserRepository import UserRepository


class WatchService:
    def __init__(self):
        self.contentRepo = ContentRepository()
        self.userRepo = UserRepository()

    def getContentWatchingNow(self, userId:int, videoId:int):
        self.userRepo.updateUserWatching(userId, videoId)
        result = self.contentRepo.selectContentWatchingNow(userId, videoId)
        result = json.dumps(result[0], ensure_ascii=False).encode('utf-8')
        return Response(result, content_type='application/json; charset=utf-8')