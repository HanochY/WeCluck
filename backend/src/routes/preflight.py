from flask import Blueprint, request, Response


preflight_blueprint = Blueprint('preflight_blueprint', __name__)


@preflight_blueprint.before_app_request
def handle_preflight():
    if request.method == 'OPTIONS':
        response = Response()
        response.headers.add('X-Content-Type-Options', '*')
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', '*')
        response.headers.add('Access-Control-Allow-Methods', '*')
        return response
