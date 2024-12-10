from fastapi import HTTPException
from fastapi.requests import Request
#from fastapi.concurrency import iterate_in_threadpool
#from uuid import uuid4
#import json
from dal._schema.logs.error import ErrorLog
from src.api.main.middleware.logging.generators import generate_fastapi_request_log
import logging
logger = logging.getLogger("default_logger")

async def log_middleware(request: Request, call_next):
    try:
        log = await generate_fastapi_request_log(request)
        logger.info(log.model_dump())
        response = await call_next(request)
#        response_body = ""
#        if response.headers.get("content-type") == "application/json":
#            response_body = [chunk async for chunk in response.body_iterator]
#            response.body_iterator = iterate_in_threadpool(iter(response_body))
    except Exception as e:
        logger.error(ErrorLog(error_message=str(e)))
    finally:
        return response
        