from flask import Blueprint, request, jsonify
import controllers.users as controller
from utils.exceptions import *


users_blueprint = Blueprint("users_blueprint", __name__)


@users_blueprint.route("/users/", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        response, code = controller.login()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add("Access-Control-Allow-Headers", "X-Requested-With")
        response.headers.add("Access-Control-Allow-Methods", "GET")
        return response, code
    
    elif request.method == "POST":
        response, code = controller.register()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add("Access-Control-Allow-Headers", "X-Requested-With")
        response.headers.add("Access-Control-Allow-Methods", "POST")
        return response, code #add input validation in controler
