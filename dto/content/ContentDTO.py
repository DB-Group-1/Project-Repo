import json


class ContentDTO:
    def __init__(
            self,
            videoId: int,
            name: str,
            image: str,
            type: str,
            description: str,
            publisher: str,
            episode: int,
    ):
        self.videoId = videoId
        self.name = name
        self.image = image
        self.type = type
        self.description = description
        self.publisher = publisher
        self.episode = episode

    def toJson(self) -> bytes:
        obj = {
            'videoId': self.videoId,
            'name': self.name,
            'image': self.image,
            'type': self.type,
            'description': self.description,
            'publisher': self.publisher,
            'episode': self.episode,
        }
        return json.dumps(obj, ensure_ascii=False).encode('utf8')