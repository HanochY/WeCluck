from fastapi_filter.contrib.sqlalchemy import Filter
from entities.user import UserPublic
from dal.models.user import User

class UserFilter(Filter, UserPublic):
    class Constants(Filter.Constants):
        model = User