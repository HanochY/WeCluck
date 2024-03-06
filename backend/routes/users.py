from flask import Blueprint, request, jsonify
import controllers.users as controller
from utils.exceptions import *


users_blueprint = Blueprint("users_blueprint", __name__)


@users_blueprint.route("/users/", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        return controller.login()
    elif request.method == "POST":
        return controller.register() #add input validation in controler
