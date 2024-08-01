from models.user import UserModel
from utils.exceptions import *
from flask import request, jsonify, current_app
from backend.src.config.provider import config
import jwt

class AuthenticationController:
    def __init__(self):
        self.model = UserModel()
        
    async def authenticate(self):
        model = self.model
        try:
            requested_user = request.json
            user = (await model.get_users_by_filter(**requested_user))[0] #add input validation in controler
            if not user:
                if await model.get_users_by_filter(name=requested_user['name']):
                    raise WrongPasswordError
                else:
                    raise UserNotFoundError
                
        except UserNotFoundError as error:
            return jsonify({
                    'message': 'Login declined!',
                    'data': None,
                    'error': str(error)
                }), 404
        else:
            token = jwt.encode(
                {'user_id': user['id']},
                current_app.secret_key,
                algorithm='HS256'
        )
        return jsonify({
            'message': 'Successfully fetched token',
            'data': token,
            'error': None
        }), 200
        #   >
            