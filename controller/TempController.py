from flask_restx import Namespace, Resource
from flask import request

from service.TempService import TempService

Friend = Namespace('Friend', description='Friend related operations')

@Friend.route('')
class Friends(Resource):
    def get(self):
        request_json = request.get_json()
        cust_id = request_json['cust_id']
        return TempService(cust_id).getFriendList()

@Friend.route('/lately')
class FriendsLately(Resource):
    def get(self):
        request_json = request.get_json()
        cust_id = request_json['cust_id']
        return TempService(cust_id).getUpdatedFriendList()

@Friend.route('/birthday')
class FriendsBirthday(Resource):
    def get(self):
        request_json = request.get_json()
        cust_id = request_json['cust_id']
        return TempService(cust_id).getBirthdayFriendList()

@Friend.route('/recommend')
class FriendsRecommend(Resource):
    def get(self):
        request_json = request.get_json()
        cust_id = request_json['cust_id']
        return TempService(cust_id).getRecommendFriendList()
