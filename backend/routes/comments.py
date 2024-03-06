from flask import Blueprint, request, jsonify
import controllers.comments as controller
from utils.exceptions import *
from middleware.authorization import token_required

comments_blueprint = Blueprint("comments_blueprint", __name__)


@comments_blueprint.route('/comments/', methods=['POST', 'GET'])
@token_required
def comment(current_user):
    if request.method == 'GET':
        return controller.get_comments()
        
    elif request.method == 'POST':
        return controller.post_comment(current_user)