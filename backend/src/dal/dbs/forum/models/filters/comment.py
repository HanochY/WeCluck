from fastapi_filter.contrib.sqlalchemy import Filter
from entities.comment import CommentRead
from models.comment import Comment

class CommentFilter(Filter, CommentRead):
    class Constants(Filter.Constants):
        model = Comment