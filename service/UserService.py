import json

from flask import Response

from dto.content.LikedContentDTO import LikedContentDTO
from dto.content.PurchasedContentDTO import PurchasedContentDTO
from dto.content.WatchedContentDTO import WatchedContentDTO
from dto.user.UserDTO import UserDTO
from repository.UserRepository import UserRepository


class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def getUserInfo(self, userId:int):
        result = self.repo.selectUserInfo(userId)
        result = UserDTO.fromJson(result[0])
        result = result.toJson()
        return Response(result, mimetype='application/json, charset=utf-8')

    def getLikedContent(self, userId:int):
        result = self.repo.selectUserLikeContents(userId)
        result = [LikedContentDTO.fromJson(content) for content in result]
        result = [content.toJson() for content in result]
        result = json.dumps(result, ensure_ascii=False).encode('utf8')
        return Response(result, mimetype='application/json, charset=utf-8')

    def getPurchasedContent(self, userId:int):
        result = self.repo.selectUserPurchasingContents(userId)
        result = [PurchasedContentDTO.fromJson(content) for content in result]
        result = [content.toJson() for content in result]
        result = json.dumps(result, ensure_ascii=False).encode('utf8')
        return Response(result, mimetype='application/json, charset=utf-8')

    def getWatchedContent(self, userId:int):
        result = self.repo.selectUserWatchingContents(userId)
        result = [WatchedContentDTO.fromJson(content) for content in result]
        result = [content.toJson() for content in result]
        result = json.dumps(result, ensure_ascii=False).encode('utf8')
        return Response(result, mimetype='application/json, charset=utf-8')