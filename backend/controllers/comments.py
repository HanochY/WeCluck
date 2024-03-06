from flask import request, jsonify
from utils.exceptions import *
from models.comment import *
from models.topic import *

def check_form_submitted_comment():
    return request.form["button"] == "comment"

def validate_comment_content(content):
    if not content:
        raise EmptyCommentContentError
        
def validate_topic_name(name):
    if not name:
        raise EmptyTopicNameError
    
def post_comment(current_user):
    try:
        user = current_user.name
        content = request.json.get("content")
        topic_name = request.json.get("topic")
        if not check_topic_exists(topic_name):
            create_topic(topic_name)
        topic_id = get_topic_id_by_name(topic_name)
        create_comment(user, content, topic_id)
    except EmptyCommentContentError as error:
        return jsonify({
                "message": "Failed to post comment!", 
                "data": None, 
                "error": str(error)
            }), 400
    else:
        return jsonify({
                "message": "Successfully posted comment!", 
                "data": None, 
                "error": None
            }), 200

def get_comments():
    try:
        topics = list(map(lambda topic: topic.to_dict(), get_all_topics()))
        comments = list(map(lambda comment: comment.to_dict(), get_all_comments()))
        
    except Exception as error:
        return jsonify({
                "message": "Failed to fetch comments!", 
                "data": None, 
                "error": str(error)
            }), 500
    else:
        return jsonify({
                "message": "Successfully fetched comments!", 
                "data": {"topics": topics, "comments": comments}, 
                "error": None
            }), 200





