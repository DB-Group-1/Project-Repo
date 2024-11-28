from flask import request
from flask_restx import Namespace, Resource

from service.WatchService import WatchService

WatchNamespace = Namespace('watch', description='Watch operations')

@WatchNamespace.route('', methods=['GET'])
class WatchController(Resource):
    def get(self):
        request_json = request.get_json()
        userId = request_json['uid']
        videoId = request_json['video_id']
        return WatchService().getContentWatchingNow(userId, videoId)
