from flask_restx import Namespace, Resource
from flask import request
from sqlalchemy import create_engine
import pandas as pd

from common.config.Config import connect_db
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

@Friend.route('/test')
class Test(Resource):
    def get(self):
        sql = """
            select * from t_customer where cust_id=1005;"""
        result = connect_db(sql)
        result['birthday'] = result['birthday'].astype(str)
        result = result.to_dict(orient='records')
        return result

    def post(self):
        sql = """
            insert into t_customer
            values (
                1005,
                "test",
                "2024-11-24"
            );"""
        connect_db(sql)

    def delete(self):
        sql = """
            delete from t_customer
            where cust_id = 1005;"""
        connect_db(sql)

    def patch(self):
        sql = """
            update t_customer
            set birthday = "2024-11-25"
            where cust_id = 1005;"""
        connect_db(sql)