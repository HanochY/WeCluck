from flask import request, jsonify
from utils.exceptions import *
from models.comment import *
from models.topic import *


def validate_content(content):
    if not content:
        raise EmptyCommentContentError
        
def validate_comment_topic(id):
    if not check_topic_exists(id):
        raise TopicNotFoundError
    
def post_comment(current_user):
    try:
        uid = current_user._id
        content = request.json.get('content')
        topic_id = request.json.get('topic_id')
        validate_content(content)
        validate_comment_topic(topic_id)
        create_comment(uid, content, topic_id)
    except EmptyCommentContentError as error:
        return jsonify({
                'message': 'Failed to post comment!', 
                'data': None, 
                'error': str(error)
            }), 400
    except Exception as error:
        return jsonify({
                'message': 'Failed to post comment!', 
                'data': None, 
                'error': str(error)
            }), 500
    else:
        return jsonify({
                'message': 'Successfully posted comment!', 
                'data': None, 
                'error': None
            }), 200

def get_comments():
    try:
        comments = list(map(lambda comment: comment.to_dict(), get_all_comments()))
        
    except Exception as error:
        return jsonify({
                'message': 'Failed to fetch comments!', 
                'data': None, 
                'error': str(error)
            }), 500
    else:
        return jsonify({
                'message': 'Successfully fetched comments!', 
                'data': comments, 
                'error': None
            }), 200