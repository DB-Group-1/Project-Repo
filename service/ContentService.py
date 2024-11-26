from repository.ContentRepository import ContentRepository


class ContentService:
    def __init__(self):
        self.repo = ContentRepository()

    def getPopularContentList(self):
        pass

    def getRecentlyContentList(self):
        pass

    def getContentListByPublisher(self, publisher:str):
        pass

    def getContentListByGenre(self, genre:str):
        pass