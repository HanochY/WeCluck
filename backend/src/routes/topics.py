from flask import Blueprint, request, jsonify
import controllers.topics as controller
from utils.exceptions import *
from middleware.authorization import token_required

topics_blueprint = Blueprint('topics_blueprint', __name__)


@topics_blueprint.route('/topics/', methods=['POST', 'GET'])
@token_required
def topics(current_user):
    if request.method == 'GET':
        response, code = controller.get_topics()
        return response, code
        
    elif request.method == 'POST':
        response, code = controller.post_topic()
        return response, code