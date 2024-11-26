from repository.SearchRepository import SearchRepository


class SearchService:
    def __init__(self):
        self.repo = SearchRepository()

    def searchByActor(self, actor: str):
        pass

    def searchByTitle(self, title: str):
        pass

    def getPopularContents(self):
        pass

    def recommendByLike(self, userId:int):
        pass

    def recommendByWatch(self, userId:int):
        pass