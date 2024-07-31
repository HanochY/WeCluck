from base import BaseEntity
class Comment(BaseEntity):
    content: str
    topic_id: int
