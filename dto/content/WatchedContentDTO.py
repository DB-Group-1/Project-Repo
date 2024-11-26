import json
from datetime import datetime


class WatchedContentDTO:
    def __init__(
            self,
            videoId:int,
            name:str,
            image:str,
            episode:int,
            date:datetime,
            runtime:int,
    ):
        self.videoId = videoId
        self.name = name
        self.image = image
        self.episode = episode
        self.date = date
        self.runtime = runtime

    def toJson(self) -> bytes:
        obj = {
            "videoId": self.videoId,
            "name": self.name,
            "image": self.image,
            "episode": self.episode,
            "date": self.date.strftime("%Y-%m-%d"),
            "runtime": self.runtime
        }
        return json.dumps(obj, ensure_ascii=False).encode('utf-8')