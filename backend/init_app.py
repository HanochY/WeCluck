import secrets
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config.app import app

from routes.comments import comments_blueprint
from routes.users import users_blueprint
from routes.preflight import preflight_blueprint
from routes.authentication import authentication_blueprint
from routes.topics import topics_blueprint
from init_db import init_db

app.register_blueprint(comments_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(preflight_blueprint)
app.register_blueprint(authentication_blueprint)
app.register_blueprint(topics_blueprint)


with app.app_context():
    
    database = SQLAlchemy()
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.secret_key = secrets.token_urlsafe(32)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{DBNAME}.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    database.init_app(app)
    init_db()
    app.run(debug=True)
    