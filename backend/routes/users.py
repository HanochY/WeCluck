from flask import Blueprint, request, jsonify
from controllers.users import *
from utils.exceptions import *


users_blueprint = Blueprint("users_blueprint", __name__)


@users_blueprint.route('/user/', methods=['POST'])
def user():
   if request.method == 'POST':
      try:
         username = request.json.get("username")
         password = request.json.get("password")
         confirm_password = request.json.get("confirm_password")
         authenticate_registration(username, password, confirm_password)
      except (PasswordConfirmationError, UserAlreadyExistsError) as error:
         return jsonify({"message": error.message}), 400
      else:
         return jsonify({"message": "User registered!"}), 201
   else:
      return jsonify({"message": "Bad request!"}), 400
