from flask import request
from flask_restx import Namespace, Resource

from service.SearchService import SearchService

SearchNamespace = Namespace('search', description='Search operations')

@SearchNamespace.route('/actor', methods=['POST'])
class SearchActorController(Resource):
    def post(self):
        request_json = request.get_json()
        actor = request_json['keyword']
        return SearchService().searchByActor(actor)

@SearchNamespace.route('/title', methods=['POST'])
class SearchTitleController(Resource):
    def post(self):
        request_json = request.get_json()
        title = request_json['keyword']
        return SearchService().searchByTitle(title)

@SearchNamespace.route('/popular', methods=['GET'])
class SearchPopularController(Resource):
    def post(self):
        return SearchService().getPopularContents()

@SearchNamespace.route('/recommend/like', methods=['GET'])
class RecommendLikeController(Resource):
    def get(self):
        request_json = request.get_json()
        userId = request_json['uid']
        return SearchService().recommendByLike(userId)

@SearchNamespace.route('/recommend/watch', methods=['GET'])
class RecommendWatchController(Resource):
    def get(self):
        request_json = request.get_json()
        userId = request_json['uid']
        return SearchService().recommendByWatch(userId)