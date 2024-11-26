import json
from datetime import datetime


class LikedContentDTO:
    def __init__(
            self,
            videoId:int,
            name:str,
            image:str,
            episode:int,
            date:datetime,
    ):
        self.videoId = videoId
        self.name = name
        self.image = image
        self.episode = episode
        self.date = date

    def toJson(self) -> bytes:
        obj = {
            "videoId": self.videoId,
            "name": self.name,
            "image": self.image,
            "episode": self.episode,
            "date": self.date.strftime("%Y-%m-%d")
        }
        return json.dumps(obj, ensure_ascii=False).encode('utf-8')