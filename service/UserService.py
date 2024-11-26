from repository.UserRepository import UserRepository


class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def getUserInfo(self, userId:int):
        pass

    def getLikedContent(self, userId:int):
        pass

    def getPurchasedContent(self, userId:int):
        pass

    def getWatchedContent(self, userId:int):
        pass