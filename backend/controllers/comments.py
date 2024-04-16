from flask import request, jsonify
from utils.exceptions import *
from models.comment import *
from models.topic import *


def post_comment(current_user):
    try:
        requested_new_comment = request.json
        if read_topic(name=requested_new_comment['topic_id']):
            raise TopicNotFoundError
        if not requested_new_comment['content']:
            raise EmptyCommentContentError
        Comment(uid=current_user._id, **requested_new_comment).create()

    except (EmptyCommentContentError, TopicNotFoundError) as error:
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
        comments = list(map(lambda comment: comment.to_dict(), read_comments()))
        
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