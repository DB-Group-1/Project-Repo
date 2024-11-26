import json


class UserDTO:
    def __init__(
            self,
            userId: int,
            name: str,
            image: str,
            email: str,
            phone: str,
            deviceId: str,
    ):
        self.userId = userId
        self.name = name
        self.image = image
        self.email = email
        self.phone = phone
        self.deviceId = deviceId

    def toJson(self) -> bytes:
        obj = {
            'userId': self.userId,
            'name': self.name,
            'image': self.image,
            'email': self.email,
            'phone': self.phone,
            'deviceId': self.deviceId,
        }
        return json.dumps(obj, ensure_ascii=False).encode('utf8')