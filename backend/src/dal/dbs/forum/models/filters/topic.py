from fastapi_filter.contrib.sqlalchemy import Filter
from entities.topic import TopicRead
from models.topic import Topic

class TopicFilter(Filter, TopicRead):
    class Constants(Filter.Constants):
        model = Topic