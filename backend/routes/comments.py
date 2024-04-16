from flask import Blueprint, request, jsonify
import controllers.comments as controller
from utils.exceptions import *
from middleware.authorization import token_required

comments_blueprint = Blueprint('comments_blueprint', __name__)


@comments_blueprint.route('/comments/', methods=['POST', 'GET'])
@token_required
def comments(current_user):
    if request.method == 'GET':
        response, code = controller.get_comments()
        return response, code
        
    elif request.method == 'POST':
        response, code = controller.post_comment(current_user)
        return response, code