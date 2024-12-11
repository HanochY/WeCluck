from dal._schema.logs.uvicorn import UvicornLog
from fastapi.requests import Request
from fastapi.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware
#from fastapi.concurrency import iterate_in_threadpool
#from uuid import uuid4
#import json
import logging
import json

logger = logging.getLogger("uvicorn")

async def generate_log(request: Request, response: Response) -> UvicornLog:
    return UvicornLog(
        client_addr= request.client.host,
        method = request.method,
        full_path= str(request.url),
        http_version= request.scope['http_version'],
        status_code= int(response.status_code),
    )
class LoggingMiddleware(BaseHTTPMiddleware):

   # def __init__(self, app):
   #     super().__init__(app)
        
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            log = await generate_log(request, response)
            logger.info("%s %s %s %s %d", *log.model_dump().values())
            return response
    #        response_body = ""
    #        if response.headers.get("content-type") == "application/json":
    #            response_body = [chunk async for chunk in response.body_iterator]
    #            response.body_iterator = iterate_in_threadpool(iter(response_body))
        except Exception as e:
            logger.error(json.loads(UvicornLog(error_message=str(e)).model_dump_json()))
            
