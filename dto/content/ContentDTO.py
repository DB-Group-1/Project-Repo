import json


class ContentDTO:
    def __init__(
            self,
            videoId: int,
            name: str,
            image: str,
            category: str,
            description: str,
            publisher: str,
            episode: int,
    ):
        self.videoId = videoId
        self.name = name
        self.image = image
        self.category = category
        self.description = description
        self.publisher = publisher
        self.episode = episode

    @staticmethod
    def fromDict(obj: dict):
        return ContentDTO(
            obj['videoId'],
            obj['name'],
            obj['image'],
            obj['type'],
            obj['description'],
            obj['publisher'],
            obj['episode'],
        )

    def toJson(self) -> bytes:
        obj = {
            'videoId': self.videoId,
            'name': self.name,
            'image': self.image,
            'type': self.category,
            'description': self.description,
            'publisher': self.publisher,
            'episode': self.episode,
        }
        return json.dumps(obj, ensure_ascii=False).encode('utf8')