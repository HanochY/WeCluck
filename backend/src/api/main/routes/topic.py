from fastapi import APIRouter, Depends
from api.main.controllers.crud import Controller
from utils.exceptions import *
from dal.sql.forum.tables.topic import TopicModels, Topic
from typing_extensions import Annotated

router = APIRouter(prefix="/topic", tags=["topic"])

controller = Controller(Topic)

@router.post('/', status_code=201)
async def create_topic(topic: Annotated[TopicModels.Create, Depends]):
    response = await controller.create(**dict(topic))
    return response
        
@router.get('/all', status_code=200, response_model=list[TopicModels.Public])
async def read_all_topics():
    response = await controller.read_all()
    return response

@router.put('/', status_code=200)
async def update_topic(update: Annotated[TopicModels.Update, Depends]):
    response = await controller.update(**dict(update))
    return response

@router.delete('/', status_code=204)
async def delete_topic(id: int):
    response = await controller.delete(id)
    return response