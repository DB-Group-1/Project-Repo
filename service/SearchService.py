import json

from flask import Response

from repository.GenreRepository import GenreRepository
from repository.SearchRepository import SearchRepository
from repository.UserRepository import UserRepository


class SearchService:
    def __init__(self):
        self.searchRepo = SearchRepository()
        self.userRepo = UserRepository()
        self.genreRepo = GenreRepository()

    def searchByActor(self, actor: str):
        result = self.searchRepo.selectContentsByActor(actor)
        result = json.dumps(result, ensure_ascii=False).encode('utf-8')
        return Response(result, content_type='application/json; charset=utf-8')

    def searchByTitle(self, title: str):
        result = self.searchRepo.selectContentsByTitle(title)
        result = json.dumps(result, ensure_ascii=False).encode('utf-8')
        return Response(result, content_type='application/json; charset=utf-8')

    def getRealtimePopularContents(self):
        result = self.searchRepo.selectRealtimePopularContents()
        result = json.dumps(result, ensure_ascii=False).encode('utf-8')
        return Response(result, content_type='application/json; charset=utf-8')

    def recommendByLike(self, userId:int):
        likedContent = self.userRepo.selectLikedContents(userId)
        likedContent = tuple(content['content_id'] for content in likedContent)
        favorGenres = self.genreRepo.selectFavorGenres(likedContent)
        favorGenres = tuple(genre['genre_id'] for genre in favorGenres)
        result = self.searchRepo.selectContentsByGenres(favorGenres)
        result = json.dumps(result, ensure_ascii=False).encode('utf-8')
        return Response(result, content_type='application/json; charset=utf-8')

    def recommendByWatch(self, userId:int):
        watchedContent = self.userRepo.selectWatchedContents(userId)
        watchedContent = tuple(content['content_id'] for content in watchedContent)
        favorGenres = self.genreRepo.selectFavorGenres(watchedContent)
        favorGenres = tuple(genre['genre_id'] for genre in favorGenres)
        result = self.searchRepo.selectContentsByGenres(favorGenres)
        result = json.dumps(result, ensure_ascii=False).encode('utf-8')
        return Response(result, content_type='application/json; charset=utf-8')