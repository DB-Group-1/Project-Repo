from flask import request
from flask_restx import Namespace, Resource

from service.ContentService import ContentService

ContentNamespace = Namespace('content', description='Content operations')

ContentListNamespace = Namespace('content_list', description='Content list operations')
ContentNamespace.add_resource(ContentListNamespace, '/list')

@ContentListNamespace.route('/popular', methods=['GET'])
class PopularContentController(Resource):
    def get(self):
        return ContentService().getPopularContentList()

@ContentListNamespace.route('/recently', methods=['GET'])
class RecentlyContentController(Resource):
    def get(self):
        return ContentService().getRecentlyContentList()

@ContentListNamespace.route('/publisher', methods=['GET'])
class PublisherContentController(Resource):
    def get(self):
        request_json = request.get_json()
        publisher = request_json['publisher']
        return ContentService().getContentListByPublisher(publisher)


@ContentListNamespace.route('/genre', methods=['GET'])
class GenreContentController(Resource):
    def get(self):
        request_json = request.get_json()
        genre = request_json['genre']
        return ContentService().getContentListByGenre(genre)