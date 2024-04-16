from models.user import *
from utils.exceptions import *
from flask import request, jsonify
from config.app import app
import jwt


def authenticate():
    try:
        requested_user = request.json
        user = read_user(**requested_user) #add input validation in controler
        if not user:
            if read_user(name=requested_user['name']):
                raise WrongPasswordError
            else:
                raise UserNotFoundError
            
    except UserNotFoundError as error:
        return jsonify({
                'message': 'Login declined!',
                'data': None,
                'error': str(error)
            }), 404
    except Exception as error:
        return jsonify(
            {
                'message': 'Login failed!',
                'data': None,
                'error': str(error)
            }), 500
    else:
        token = jwt.encode(
            {'user_id': user._id},
            app.config['SECRET_KEY'],
            algorithm='HS256'
        )
        return jsonify({
            'message': 'Successfully fetched token',
            'data': token,
            'error': None
        }), 200
        
        