from backend.src.dal.base_repository import BaseRepository
from dal.sqlalchemy.entities.topic import TopicEntity as Topic
from app.db_manager import db_manager

database = db_manager.database

class TopicRepository(BaseRepository):
    entity = Topic
    
    @staticmethod
    async def add(**data):
        topic = Topic(**data)
        database.session.add(topic)
        database.session.commit()
        
    @staticmethod
    async def get(**filter):
        query = database.session.query(Topic)
        if filter:
            return query.filter_by(**filter).all()
        else:
            return query.all()
    
    @staticmethod
    async def edit(id: int, **new_data):
        topic = database.session.query(Topic).filter_by(id=id).first()
        if topic:
            topic.update(**new_data)
            database.session.commit()
    
    @staticmethod
    async def remove(id: int):
        topic = database.session.query(Topic).filter_by(id=id).first()
        if topic:
            database.session.delete(topic)
            database.session.commit()