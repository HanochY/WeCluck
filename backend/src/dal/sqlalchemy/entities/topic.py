from dal.sqlalchemy.entities.base import BaseEntity
from datetime import datetime
from app.db_manager import db_manager

database = db_manager.database

class TopicEntity(BaseEntity, db_manager.database.Model):
    id = database.Column('id', database.Integer, primary_key=True)
    name = database.Column(database.String(32))
    timestamp = database.Column(
         database.DateTime, nullable=False, default=datetime.now
    )