from models.user import *
from utils.exceptions import *
from flask import request, jsonify
from config.app import app
import jwt


def register():
    try:
        requested_new_user = request.json
        if read_user(name=requested_new_user['name']):
            raise UserAlreadyExistsError
        User(**requested_new_user).create()
    except UserAlreadyExistsError as error:
        return jsonify({
            'message': 'Registration declined!',
            'data': None,
            'error': str(error)
        }), 400
    except Exception as error:
        print(error)
        return jsonify({
            'message': 'Registration failed!',
            'data': None,
            'error': str(error)
        }), 500
    else:
        return jsonify({
            'message': 'Successfully registered new user',
            'data': None,
            'error': None
        }), 201
