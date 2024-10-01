from flask import request, jsonify
from utils.exceptions import *
from models.comment import CommentModel
from models.topic import TopicModel


class CommentController:
    def __init__(self):
        self.model = CommentModel()
    
    async def post_comment(self, current_user):
        model = self.model
        requested_new_comment = request.json
        try:
            if not await TopicModel().get_topic_by_id(requested_new_comment['topic_id']):
                raise TopicNotFoundError
            elif not requested_new_comment['content']:
                raise EmptyCommentContentError
            await model.create_comment(uid=current_user['id'], **requested_new_comment)

        except (EmptyCommentContentError, TopicNotFoundError) as error:
            return jsonify({
                    'message': 'Failed to post comment!', 
                    'data': None, 
                    'error': str(error)
                }), 400

        #except Exception as error:
        #    return jsonify({
        #            'message': 'Failed to post comment!', 
        #            'data': None, 
        #            'error': str(error)
        #        }), 500
        else:
            return jsonify({
                    'message': 'Successfully posted comment!', 
                    'data': None, 
                    'error': None
                }), 200

    async def get_comments(self):
        model = self.model
        try:
            comments = await model.get_all_comments()
            
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