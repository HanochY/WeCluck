from models.user import *
from utils.exceptions import *
from flask import request, jsonify
from config.app import app
import jwt


def validate_user_exists(username):
    if not check_user_exists(username):
        raise UserNotFoundError


def validate_password(username, password):
    if not get_password(username) == password:
        raise WrongPasswordError


def validate_username_available(username):
    if check_user_exists(username):
        raise UserAlreadyExistsError


def login():
    try:
        user = request.json
        username = user['username']
        password = user['password']
        uid = get_user_id_by_username(username) #add input validation in controler
        print(uid)
        # validate input
        #if not validate_email_and_password(data.get('email'), data.get('password')): return dict(message='Invalid data', data=None, error=is_validated), 400
        validate_user_exists(username)
        validate_password(username, password)
    except UserNotFoundError as error:
        return jsonify({
                "message": "Login declined!",
                "data": None,
                "error": str(error)
            }), 404
    except Exception as error:
        return jsonify(
            {
                "message": "Login failed!",
                "data": None,
                "error": str(error)
            }), 500
    else:
        user["token"] = jwt.encode(
            {"user_id": uid},
            app.config["SECRET_KEY"],
            algorithm="HS256"
        )
        return jsonify({
            "message": "Successfully fetched token",
            "data": user,
            "error": None
        }), 200
    
    

def register():
    try:
        user = request.json
        username = user['username']
        password = user['password'] #add input validation in controler
        validate_username_available(username)
        create_user(username, password)
    except UserAlreadyExistsError as error:
        return jsonify({
            "message": "Registration declined!",
            "data": None,
            "error": str(error)
        }), 400
    except Exception as error:
        return jsonify({
            "message": "Registration failed!",
            "data": None,
            "error": str(error)
        }), 500
    else:
        return jsonify({
            "message": "Successfully registered new user",
            "data": user,
            "error": None
        }), 201
