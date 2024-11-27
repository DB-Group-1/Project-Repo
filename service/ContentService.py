import json

from flask import Response

from dto.content.ContentDTO import ContentDTO
from repository.ContentRepository import ContentRepository
from repository.GenreRepository import GenreRepository


class ContentService:
    def __init__(self):
        self.repo = ContentRepository()

    def getPopularContentList(self):
        result = self.repo.selectPopularContent()
        result = json.dumps(result, ensure_ascii=False).encode('utf8')
        return Response(result, mimetype='application/json, charset=utf-8')

    def getRecentlyContentList(self):
        result = self.repo.selectRecentlyContent()
        result = json.dumps(result, ensure_ascii=False).encode('utf8')
        return Response(result, mimetype='application/json, charset=utf-8')

    def getContentListByGenre(self, genre:str):
        result = self.repo.selectContentListByGenre(genre)
        result = json.dumps(result, ensure_ascii=False).encode('utf8')
        return Response(result, mimetype='application/json, charset=utf-8')

    def getContentDetail(self, contentId:int):
        mainInfo = self.repo.selectContentInfo(contentId)
        actorInfo = self.repo.selectActorInContent(contentId)
        episodeInfo = self.repo.selectEpisodeOfContent(contentId)
        for i in range(len(episodeInfo)):
            episodeInfo[i]['episode_number'] = i+1
        result = mainInfo[0]
        result['actor'] = actorInfo
        result['episode'] = episodeInfo
        result = json.dumps(result, ensure_ascii=False).encode('utf8')
        return Response(result, mimetype='application/json, charset=utf-8')

    def getRelatedContent(self, contentId:int):
        relatedGenre = GenreRepository().selectRelatedGenre(contentId)
        relatedGenre = relatedGenre[0]['genre_id']
        relatedActor = self.repo.selectRelatedActor(contentId)
        relatedActor = tuple(actor['cast_id'] for actor in relatedActor)
        relatedPublisher = self.repo.selectRelatedPublisher(contentId)
        relatedPublisher = relatedPublisher[0]['publisher']
        result = self.repo.selectRelatedContent(contentId, relatedGenre, relatedActor, relatedPublisher)
        result = json.dumps(result, ensure_ascii=False).encode('utf8')
        return Response(result, mimetype='application/json, charset=utf-8')