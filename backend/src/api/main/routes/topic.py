from fastapi import APIRouter, Depends
from controllers.topic import TopicController
from utils.exceptions import *
from middleware.authorization import token_required

router = APIRouter(prefix="/topics", tags=["topics"])

controller = TopicController()

@router.get('/')
@token_required
async def topics(current_user):
        response, code = await controller.get_topics()
        return response, code


@router.post('/')
@token_required
async def topics(current_user):
        response, code = await controller.post_topic()
        return response, code