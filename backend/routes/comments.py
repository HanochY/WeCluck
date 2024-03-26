from flask import Blueprint, request, jsonify
import controllers.comments as controller
from utils.exceptions import *
from middleware.authorization import token_required

comments_blueprint = Blueprint("comments_blueprint", __name__)


@comments_blueprint.route('/comments/', methods=['POST', 'GET'])
@token_required
def comment(current_user):
    if request.method == 'GET':
        response, code = controller.get_comments()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add("Access-Control-Allow-Headers", "X-Requested-With")
        response.headers.add("Access-Control-Allow-Methods", "GET")
        return response, code
        
    elif request.method == 'POST':
        response, code = controller.post_comment(current_user)
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add("Access-Control-Allow-Headers", "X-Requested-With")
        response.headers.add("Access-Control-Allow-Methods", "POST")
        return response, code