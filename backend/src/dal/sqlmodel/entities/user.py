from dal.sqlalchemy.entities.base import BaseEntity
from app.db_manager import db_manager

database = db_manager.database

class UserEntity(BaseEntity, db_manager.database.Model):
    id = database.Column('id', database.Integer, primary_key=True)
    name = database.Column(database.String(32))
    password = database.Column(database.String(32))