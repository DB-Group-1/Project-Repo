import json
from datetime import datetime
from utils.DateFormat import DateFormat


class LikedContentDTO:
    def __init__(
            self,
            videoId:int,
            name:str,
            image:str,
            runtime:int,
            date:datetime,
    ):
        self.videoId = videoId
        self.name = name
        self.image = image
        self.runtime = runtime
        self.date = date

    @staticmethod
    def fromJson(jsonData:dict) -> 'LikedContentDTO':
        return LikedContentDTO(
            videoId=jsonData['video_id'],
            name=jsonData['name'],
            image=jsonData['image'],
            runtime=jsonData['runtime'],
            date=DateFormat.parse(jsonData['date'], DateFormat.all)
        )

    def toJson(self) -> dict:
        return {
            "videoId": self.videoId,
            "name": self.name,
            "image": self.image,
            "runtime": self.runtime,
            "date": DateFormat.format(self.date)
        }