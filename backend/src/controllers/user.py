from models.user import UserModel
from utils.exceptions import *
from flask import request, jsonify

class UserController:
    def __init__(self):
        self.model = UserModel()
    
    async def register(self):
        model = self.model
        try:
            requested_new_user = request.json
            if await model.get_users_by_filter(name=requested_new_user['name']):
                raise UserAlreadyExistsError
            await model.create_user(**requested_new_user)
        except UserAlreadyExistsError as error:
            return jsonify({
                'message': 'Registration declined!',
                'data': None,
                'error': str(error)
            }), 400
        else:
            return jsonify({
                'message': 'Successfully registered new user',
                'data': None,
                'error': None
            }), 201
