from fastapi import APIRouter, Depends
from api.main.controllers.topic import TopicController
from utils.exceptions import *
from dal.schema.resources.topic import TopicPublic, TopicFullInput, TopicPartialInput
from typing_extensions import Annotated
from uuid import UUID

router = APIRouter(prefix="/topic", tags=["topic"])

controller = TopicController()

@router.post('/', status_code=201)
async def create_topic(topic: Annotated[TopicFullInput, Depends]) -> UUID | None:
    response: UUID | None = await controller.create(data=topic)
    return response
        
@router.get('/all', status_code=200, response_model=list[TopicPublic])
async def read_all_topics() -> list[TopicPublic] | None:
    response: list[TopicPublic] | None = await controller.read_all()
    return response

@router.patch('/{id}', status_code=200)
async def update_topic(id: UUID, topic_update: Annotated[TopicPartialInput, Depends]) -> None:
    await controller.update(id=id, new_data=topic_update)

@router.delete('/{id}', status_code=204)
async def delete_topic(id: UUID) -> None:
    await controller.delete(id=id)
