from fastapi import APIRouter, Depends
from api.main.controllers.crud import Controller
from utils.exceptions import *
from dal.sql.forum.models.topic import Topic, TopicTable
from typing_extensions import Annotated

router = APIRouter(prefix="/topic", tags=["topic"])

controller = Controller(TopicTable)

@router.post('/', status_code=201)
async def create_topic(topic: Annotated[Topic.Create, Depends]):
    response = await controller.create(topic)
    return response
        
@router.get('/', status_code=200, response_model=Topic.Model.Public)
async def read_all_topics():
    response = await controller.read()
    return response

@router.put('/', status_code=200)
async def update_topic(update: Annotated[Topic.Model.Update, Depends]):
    response = await controller.update(update)
    return response

@router.delete('/', status_code=204)
async def delete_topic(id: int):
    response = await controller.delete(id)
    return response