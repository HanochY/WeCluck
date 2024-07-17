from dal.base import BaseRepository
from dal.sqlalchemy.entities.comment import CommentEntity as Comment
from app.db_manager import db_manager

database = db_manager.database

class CommentRepository(BaseRepository):
    entity = Comment
    
    @staticmethod
    async def add(**data):
        comment = Comment(**data)
        database.session.add(comment)
        database.session.commit()
    
    @staticmethod
    async def get(**filter):
        query = database.session.query(Comment)
        if filter:
            return query.filter_by(**filter).all()
        else:
            return query.all()
    
    @staticmethod
    async def edit(id: int, **new_data):
        comment = database.session.query(Comment).filter_by(id=id).first()
        if comment:
            comment.update(**new_data)
            database.session.commit()
    
    @staticmethod
    async def remove(id: int):
        comment = database.session.query(Comment).filter_by(id=id).first()
        if comment:
            database.session.delete(comment)
            database.session.commit()