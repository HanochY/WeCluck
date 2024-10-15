from utils.exceptions import *
from dal.dbs.forum.models.topic import Topic
from dal.repositories.sqlmodel import SQLModelRepository 


async def post_topic(self):
    model = self.model
    requested_new_topic = request.json
    try:
        if await model.get_topics_by_filter(name=requested_new_topic['name']):
            raise TopicAlreadyExistsError
        await model.create_topic(**requested_new_topic)
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
async def get_topics(self):
    model = self.model
    try:
        topics = await model.get_all_topics()
    except Exception as error:
        return jsonify({
                'message': 'Failed to fetch topics!', 
                'data': None, 
                'error': str(error)
            }), 500
    else:
        print('s')
        return jsonify({
                'message': 'Successfully fetched topics!', 
                'data': topics, 
                'error': None
            }), 200