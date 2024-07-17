from dal.base import BaseRepository
from dal.sqlalchemy.entities.user import UserEntity as User
from app.db_manager import db_manager

database = db_manager.database

class UserRepository(BaseRepository):
    entity = User
    
    @staticmethod
    async def add(**data):
        user = User(**data)
        database.session.add(user)
        database.session.commit()

    @staticmethod
    async def get(**filter):
        query = database.session.query(User)
        if filter:
            return query.filter_by(**filter).all()
        else:
            return query.all()
    
    @staticmethod
    async def edit(id: int, **new_data):
        user = database.session.query(User).filter_by(id=id).first()
        if user:
            user.update(new_data)
            database.session.commit()
    
    @staticmethod
    async def remove(id: int):
        user = database.session.query(User).filter_by(id=id).first()
        if user:
            database.session.delete(user)
            database.session.commit()