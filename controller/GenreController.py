from flask import request
from flask_restx import Namespace, Resource

from service.GenreService import GenreService

GenreNamespace = Namespace('genre', description='Genre operations')

@GenreNamespace.route('', methods=['GET'])
class GenreController(Resource):
    def get(self):
        request_json = request.get_json()
        category = request_json['category']
        return GenreService().getGenresByCategory(category)