from flask import request
from flask_restx import Namespace, Resource

from service.ContentService import ContentService

ContentNamespace = Namespace('content', description='Content operations')

@ContentNamespace.route('/list/popular', methods=['GET'])
class PopularContentController(Resource):
    def get(self):
        return ContentService().getPopularContentList()

@ContentNamespace.route('/list/recently', methods=['GET'])
class RecentlyContentController(Resource):
    def get(self):
        return ContentService().getRecentlyContentList()

@ContentNamespace.route('/list/genre', methods=['GET'])
class GenreContentController(Resource):
    def get(self):
        request_json = request.get_json()
        genre = request_json['genre']
        return ContentService().getContentListByGenre(genre)

@ContentNamespace.route('', methods=['GET'])
class ContentDetailController(Resource):
    def get(self):
        request_json = request.get_json()
        contentId = request_json['content_id']
        return ContentService().getContentDetail(contentId)

@ContentNamespace.route('/recommend', methods=['GET'])
class RecommendContentController(Resource):
    def get(self):
        request_json = request.get_json()
        contentId = request_json['content_id']
        return ContentService().getRelatedContent(contentId)