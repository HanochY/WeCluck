from fastapi import APIRouter, Depends
from fastapi_filter import FilterDepends
from controllers.crud import Controller
from utils.exceptions import *
from entities.topic import TopicBase, TopicCreate, TopicUpdate
from dal.dbs.forum.models.topic import Topic
from dal.dbs.forum.models.filters.topic import TopicFilter
from typing_extensions import Annotated

router = APIRouter(prefix="/topic", tags=["topic"])

controller = Controller(Topic)

@router.post('/', status_code=201)
async def create_topic(topic: Annotated[TopicCreate, Depends]):
    response = await controller.create(topic)
    return response
        
@router.get('/', status_code=200, response_model=TopicBase)
async def read_topic(filter: Annotated[TopicFilter, FilterDepends]):
    response = await controller.read(filter)
    return response

@router.put('/', status_code=200)
async def update_topic(update: Annotated[TopicUpdate, Depends]):
    response = await controller.update(update)
    return response

@router.delete('/', status_code=204)
async def delete_topic(id: int):
    response = await controller.delete(id)
    return response