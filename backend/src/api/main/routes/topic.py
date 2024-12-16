from fastapi import APIRouter, Depends
from backend.src.api.main.controllers.topic import TopicController
from backend.src.dal._schema.resources.topic import Public
from utils.exceptions import *
from dal.sql.forum.tables.topic import TopicModels, Topic
from typing_extensions import Annotated
from uuid import UUID

router = APIRouter(prefix="/topic", tags=["topic"])

controller = TopicController()

@router.post('/', status_code=201)
async def create_topic(topic: Annotated[TopicModels.Create, Depends]) -> UUID | None:
    response: UUID | None = await controller.create(data=topic)
    return response
        
@router.get('/all', status_code=200, response_model=list[TopicModels.Public])
async def read_all_topics() -> list[TopicModels.Public] | None:
    response: list[TopicModels.Public] | None = await controller.read_all()
    return response

@router.put('/', status_code=200)
async def update_topic(id: UUID, topic_update: Annotated[TopicModels.Update, Depends]) -> None:
    await controller.update(id=id, new_data=topic_update)

@router.delete('/', status_code=204)
async def delete_topic(id: UUID) -> None:
    await controller.delete(id=id)
