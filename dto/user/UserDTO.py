import json


class UserDTO:
    def __init__(
            self,
            uid: int,
            name: str,
            image: str,
            email: str,
            phone: str,
            cash: int,
            payment: int
    ):
        self.uid = uid
        self.name = name
        self.image = image
        self.email = email
        self.phone = phone
        self.cash = cash,
        self.payment = payment,

    @staticmethod
    def fromJson(obj:dict) -> 'UserDTO':
        return UserDTO(
            obj['uid'],
            obj['name'],
            obj['image'],
            obj['email'],
            obj['phone'],
            obj['cash'],
            obj['payment']
        )

    def toJson(self) -> bytes:
        obj = {
            'uid': self.uid,
            'name': self.name,
            'image': self.image,
            'email': self.email,
            'phone': self.phone,
            'cash': self.cash[0],
            'payment': self.payment[0]
        }
        return json.dumps(obj, ensure_ascii=False).encode('utf8')