from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models import *

class DBManager:
    database = SQLAlchemy()

    def init_db(self, app: Flask):
        self.database.init_app(app)
        self.database.create_all()

db_manager = DBManager()