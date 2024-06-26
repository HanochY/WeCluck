from flask import Blueprint
from controllers.authentication import AuthenticationController
from utils.exceptions import *

authentication_blueprint = Blueprint('authentication_blueprint', __name__)

controller = AuthenticationController()

@authentication_blueprint.route('/auth/', methods=['POST'])
async def authenticate():
    response, code = await controller.authenticate()
    return response, code
