from flask import Blueprint, request, jsonify
from controllers.users import *
from controllers.comments import *
from utils.exceptions import *


comments_blueprint = Blueprint("comments_blueprint", __name__)


@comments_blueprint.route('/comment/', methods=['POST', 'GET'])
def comment():
   if request.method == 'GET':
      try:
         topics = list(map(lambda x: x.to_json(), Topic.query.all()))
         comments = list(map(lambda x: x.to_json(), Comment.query.all()))
         return jsonify({"topics": topics, "comments": comments})
      except Exception as error:
         return jsonify({"message": error.message}), 500
   elif request.method == 'POST':
      try:
         user = request.json.get("username")
         content = request.json.get("content")
         topic_name = request.json.get("topic")
         post_comment(user, content, topic_name)
      except EmptyCommentContentError:
         return jsonify({"message": "Comment must have content!"}), 400
      else:
         return jsonify({"message": "Comment created!"}), 201
