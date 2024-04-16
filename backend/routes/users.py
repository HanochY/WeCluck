from flask import Blueprint, request, jsonify
import controllers.users as controller
from utils.exceptions import *


users_blueprint = Blueprint('users_blueprint', __name__)


@users_blueprint.route('/users/', methods=['POST'])
def users():
    response, code = controller.register()
    return response, code #add input validation in controler
