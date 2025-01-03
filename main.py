import json

from flask import Flask
from flask_restx import Api

from controller.ContentConroller import ContentNamespace
from controller.GenreController import GenreNamespace
from controller.SearchController import SearchNamespace
from controller.UserController import UserNamespace
from controller.WatchController import WatchNamespace

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

api = Api(app)
api.add_namespace(UserNamespace, "/user")
api.add_namespace(ContentNamespace, "/content")
api.add_namespace(SearchNamespace, "/search")
api.add_namespace(GenreNamespace, "/genre")
api.add_namespace(WatchNamespace, "/watch")

if __name__ == '__main__':
    app.run()