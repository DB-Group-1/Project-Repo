import json
from datetime import datetime

from utils.DateFormat import DateFormat


class WatchedContentDTO:
    def __init__(
            self,
            videoId:int,
            name:str,
            image:str,
            date:datetime,
            runtime:int,
    ):
        self.videoId = videoId
        self.name = name
        self.image = image
        self.date = date
        self.runtime = runtime

    @staticmethod
    def fromJson(jsonObj:dict):
        return WatchedContentDTO(
            jsonObj['video_id'],
            jsonObj['name'],
            jsonObj['image'],
            DateFormat.parse(jsonObj['date'], DateFormat.all),
            jsonObj['runtime']
        )

    def toJson(self) -> dict:
        return {
            "videoId": self.videoId,
            "name": self.name,
            "image": self.image,
            "date": DateFormat.format(self.date),
            "runtime": self.runtime
        }