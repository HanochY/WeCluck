from entities.user import User

from app.db_manager import db_manager

database = db_manager.database

class UserRepository:

    @staticmethod
    def add_user(data: dict):
        user = User(**data)
        database.session.add(user)
        database.session.commit()
        return user

    @staticmethod
    def get_users(**kwargs):
        query = database.session.query(User)
        if kwargs:
            return query.filter_by(**kwargs).all()
        else:
            return query.all()
        
    @classmethod
    def get_user(cls, **kwargs):
        users = cls.read_users(**kwargs)
        return users[0] if users else None
    
    @classmethod
    def edit_user(cls, user_id: int, new_data: dict):
        user = user
        database.session.commit()

    @classmethod
    def remove_user(cls, user_id: int):
        database.session.delete(user)
        database.session.commit()


    