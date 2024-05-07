from flask import Flask
from flask_cors import CORS

from config.manager import config
from routes.comments import comments_blueprint
from routes.users import users_blueprint
from routes.preflight import preflight_blueprint
from routes.authentication import authentication_blueprint
from routes.topics import topics_blueprint


app = Flask(__name__)
app.register_blueprint(comments_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(preflight_blueprint)
app.register_blueprint(authentication_blueprint)
app.register_blueprint(topics_blueprint)
app.secret_key = config.app.secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = f'{config.db.vendor}:///{config.db.name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.app.track_modifications
app.config['DEBUG'] = config.app.debug
app.config['SERVER_NAME'] = f'{config.app.host}:{config.app.port}'
app.config['THREADED'] = config.app.threaded
CORS(app, origins=config.app.allowed_origins)