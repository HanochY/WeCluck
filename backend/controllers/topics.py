from flask import request, jsonify
from utils.exceptions import *
from models.topic import *


def validate_topic(name):
    if check_topic_exists_by_name(name):
        raise TopicAlreadyExistsError
    
def post_topic():
    try:
        name = request.json.get('name')
        validate_topic(name)
        create_topic(name)
    except TopicAlreadyExistsError as error:
        return jsonify({
                'message': 'Failed to post topic!', 
                'data': None, 
                'error': str(error)
            }), 400
    except Exception as error:
        return jsonify({
                'message': 'Failed to post topic!', 
                'data': None, 
                'error': str(error)
            }), 500
    else:
        return jsonify({
                'message': 'Successfully posted topic!', 
                'data': None, 
                'error': None
            }), 200

def get_topics():
    try:
        topics = list(map(lambda topic: topic.to_dict(), get_all_topics()))
        
    except Exception as error:
        return jsonify({
                'message': 'Failed to fetch topics!', 
                'data': None, 
                'error': str(error)
            }), 500
    else:
        return jsonify({
                'message': 'Successfully fetched topics!', 
                'data': topics, 
                'error': None
            }), 200