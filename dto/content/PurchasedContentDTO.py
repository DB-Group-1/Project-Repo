import json
from datetime import datetime

from utils.DateFormat import DateFormat


class PurchasedContentDTO:
    def __init__(
            self,
            videoId:int,
            name:str,
            image:str,
            type:str,
            runtime:int,
            price:int,
            date:datetime,
    ):
        self.videoId = videoId
        self.name = name
        self.image = image
        self.type = type
        self.runtime = runtime
        self.price = price
        self.date = date

    @staticmethod
    def fromJson(jsonObj:dict):
        return PurchasedContentDTO(
            jsonObj['video_id'],
            jsonObj['name'],
            jsonObj['image'],
            jsonObj['type'],
            jsonObj['runtime'],
            jsonObj['price'],
            DateFormat.parse(jsonObj['date'], DateFormat.all)
        )

    def toJson(self) -> dict:
        return {
            "video_id": self.videoId,
            "name": self.name,
            "image": self.image,
            "type": self.type,
            "runtime": self.runtime,
            "price": self.price,
            "date": DateFormat.format(self.date)
        }