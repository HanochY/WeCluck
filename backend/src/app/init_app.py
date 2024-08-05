from flask import Flask
from flask_cors import CORS


from config.provider import ConfigProvider
from routes.user import users_blueprint
from routes.topic import topics_blueprint
from routes.authentication import authentication_blueprint
from routes.comment import comments_blueprint
from routes.preflight import preflight_blueprint


app = Flask(__name__)
app.register_blueprint(comments_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(preflight_blueprint)
app.register_blueprint(authentication_blueprint)
app.register_blueprint(topics_blueprint)

app_settings = ConfigProvider.app_settings()
db_settings = ConfigProvider.db_settings()

app.secret_key = app_settings.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = db_settings.SQLITE_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = app_settings.TRACK_MODIFICATIONS
app.config['DEBUG'] = app_settings.DEBUG
app.config['SERVER_NAME'] = f"{app_settings.ADDRESS}:{app_settings.PORT}"
app.config['THREADED'] = app_settings.THREAD_COUNT > 1
#CORS(app, origins=app_settings.ALLOWED_ORIGINS)