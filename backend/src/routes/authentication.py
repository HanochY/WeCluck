from flask import Blueprint, request, jsonify
import controllers.login as controller
from utils.exceptions import *


authentication_blueprint = Blueprint('authentication_blueprint', __name__)


@authentication_blueprint.route('/auth/', methods=['POST'])
def authenticate():
    response, code = controller.authenticate()
    return response, code
