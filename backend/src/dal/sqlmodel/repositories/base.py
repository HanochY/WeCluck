from dal.base_repository import BaseRepository
from app.db_manager import db_manager

database = db_manager.database

class SQLAlchemyRepository(BaseRepository):
    
    async def add(self, **data):
        topic = self.entity(**data)
        database.session.add(topic)
        database.session.commit()
        
    async def get(self, **filter):
        query = database.session.query(self.entity)
        if filter:
            return query.filter_by(**filter).all()
        else:
            return query.all()
    
    async def edit(self, id: int, **new_data):
        topic = database.session.query(self.entity).filter_by(id=id).first()
        if topic:
            topic.update(**new_data)
            database.session.commit()
    
    async def remove(self, id: int):
        topic = database.session.query(self.entity).filter_by(id=id).first()
        if topic:
            database.session.delete(topic)
            database.session.commit()