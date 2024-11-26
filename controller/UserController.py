from flask import request
from flask_restx import Namespace, Resource

from service.UserService import UserService

UserNamespace = Namespace('user', description='user operations')

@UserNamespace.route('', methods=['GET'])
class UserInformationController(Resource):
    def get(self):
        request_json = request.get_json()
        userId = request_json['uid']
        return UserService().getUserInfo(userId)


@UserNamespace.route('/like', methods=['GET'])
class UserLikeController(Resource):
    def get(self):
        request_json = request.get_json()
        userId = request_json['uid']
        return UserService().getLikedContent(userId)


@UserNamespace.route('/purchase', methods=['GET'])
class UserPurchaseController(Resource):
    def get(self):
        request_json = request.get_json()
        userId = request_json['uid']
        return UserService().getPurchasedContent(userId)


@UserNamespace.route('/watch', methods=['GET'])
class UserWatchController(Resource):
    def get(self):
        request_json = request.get_json()
        userId = request_json['uid']
        return UserService().getWatchedContent(userId)