from flask import Blueprint, request, jsonify
from controllers.users import *
from utils.exceptions import *
from config.app import app
import jwt


users_blueprint = Blueprint("users_blueprint", __name__)


@users_blueprint.route("/users/", methods=["POST"])
def register():
   try:
      user = request.json
      register(**user) #add input validation in controler
   except (PasswordConfirmationError, UserAlreadyExistsError) as error:
      return jsonify(
         {
            "message": "Registration declined!",
            "data": None,
            "error": error.message
         }), 400
   except Exception as error:
      return jsonify(
         {
            "message": "Registration failed!",
            "data": None,
            "error": error.message
         }), 500
   else:
      return jsonify(
         {
            "message": "Successfully registered new user",
            "data": user,
            "error": None
         }), 201


@users_blueprint.route("/users/login", methods=["POST"])
def login():
   try:
      user = request.json
      uid = login(**user) #add input validation in controler
      # validate input
        #if not validate_email_and_password(data.get('email'), data.get('password')): return dict(message='Invalid data', data=None, error=is_validated), 400
   except (PasswordConfirmationError, UserNotFoundError) as error:
      return jsonify(
         {
            "message": "Login declined!",
            "data": None,
            "error": error.message
         }), 404
   except Exception as error:
      return jsonify(
         {
            "message": "Login failed!",
            "data": None,
            "error": error.message
         }), 500
   else:
      user["token"] = jwt.encode(
          {"user_id": uid},
          app.config["SECRET_KEY"],
          algorithm="HS256"
      )
      return {
          "message": "Successfully fetched auth token",
          "data": user
      }
   

