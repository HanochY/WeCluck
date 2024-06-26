from typing import TYPE_CHECKING

from dal.sqlalchemy.repositories.topic import TopicRepository


class TopicModel:
    def __init__(self):
        self.repository = TopicRepository()

    async def create_topic(self, **topic_data):
        await self.repository.add(**topic_data)

    async def get_topic_by_id(self, topic_id: int) -> dict:
        return (await self.repository.get(id=topic_id))[0].to_dict()

    async def get_all_topics(self) -> list[dict]:
        return list(map(lambda topic: topic.to_dict(), 
                        await self.repository.get())) 

    async def get_topics_by_filter(self, **filter) -> list[dict]:
        return list(map(lambda topic: topic.to_dict(), 
                        await self.repository.get(**filter))) 

    async def update_topic(self, topic_id: int, **new_data):
        await self.repository.edit(topic_id, **new_data)

    async def remove_topic_by_id(self, topic_id: int):
        await self.repository.remove(topic_id)