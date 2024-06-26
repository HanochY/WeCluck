from flask import Blueprint, request
from controllers.comment import CommentController
from utils.exceptions import *
from middleware.authorization import token_required

comments_blueprint = Blueprint('comments_blueprint', __name__)

controller = CommentController()

@comments_blueprint.route('/comments/', methods=['POST', 'GET'])
@token_required
async def comments(current_user):
    if request.method == 'GET':
        response, code = await controller.get_comments()
        return response, code
        
    elif request.method == 'POST':
        response, code = await controller.post_comment(current_user)
        return response, code