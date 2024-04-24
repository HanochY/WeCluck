from flask import request, jsonify
from utils.exceptions import *
from models.topic import *


def post_topic():
    try:
        requested_new_topic = request.json
        if read_topic(name=requested_new_topic['name']):
            raise TopicAlreadyExistsError
        Topic(**requested_new_topic).create()
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
        topics = list(map(lambda topic: topic.to_dict(), read_topics()))   
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