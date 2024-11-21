from flask import Flask
from flask_restx import Api

from controller.TempController import Friend

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

api = Api(app)
api.add_namespace(Friend, "/friends")

if __name__ == '__main__':
    app.run()