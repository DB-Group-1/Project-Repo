import json

from flask import Response

from repository.GenreRepository import GenreRepository


class GenreService:
    def __init__(self):
        self.repo = GenreRepository()

    def getGenresByCategory(self) -> Response:
        result = self.repo.selectGenre()
        result = json.dumps(result, ensure_ascii=False).encode('utf-8')
        return Response(result, content_type='application/json; charset=utf-8')