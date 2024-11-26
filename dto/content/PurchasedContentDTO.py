import json
from datetime import datetime


class PurchasedContentDTO:
    def __init__(
            self,
            videoId:int,
            name:str,
            image:str,
            type:str,
            episode:int,
            price:int,
            date:datetime,
    ):
        self.videoId = videoId
        self.name = name
        self.image = image
        self.type = type
        self.episode = episode
        self.price = price
        self.date = date

    def toJson(self) -> bytes:
        obj = {
            "videoId": self.videoId,
            "name": self.name,
            "image": self.image,
            "type": self.type,
            "episode": self.episode,
            "price": self.price,
            "date": self.date.strftime("%Y-%m-%d")
        }
        return json.dumps(obj, ensure_ascii=False).encode('utf-8')