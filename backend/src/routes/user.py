from flask import Blueprint
from controllers.user import UserController
from utils.exceptions import *

users_blueprint = Blueprint('users_blueprint', __name__)

controller = UserController()

@users_blueprint.route('/users/', methods=['POST'])
async def users():
    response, code = await controller.register()
    return response, code #add input validation in controler
