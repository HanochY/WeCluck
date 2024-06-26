from flask import Blueprint, request
from controllers.topic import TopicController
from utils.exceptions import *
from middleware.authorization import token_required

topics_blueprint = Blueprint('topics_blueprint', __name__)

controller = TopicController()

@topics_blueprint.route('/topics/', methods=['POST', 'GET'])
@token_required
async def topics(current_user):
    if request.method == 'GET':
        response, code = await controller.get_topics()
        return response, code
        
    elif request.method == 'POST':
        response, code = await controller.post_topic()
        return response, code