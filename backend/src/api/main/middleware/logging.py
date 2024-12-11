from dal._schema.logs.request import RequestLog
from fastapi.requests import Request
from starlette.middleware.base import BaseHTTPMiddleware
#from fastapi.concurrency import iterate_in_threadpool
#from uuid import uuid4
#import json
from dal._schema.logs.error import ErrorLog
import logging
import json

logger = logging.getLogger("uvicorn.access")
print(logger)
async def generate_fastapi_request_log(request: Request) -> RequestLog:
    return RequestLog(
        method = request.method,
        route = request['path'],
        ip = request.client.host,
        url = str(request.url),
        host = request.url.hostname,
        body = json.loads(await request.body() or "{}"),
        headers = dict(request.headers.items())
    )
class LoggingMiddleware(BaseHTTPMiddleware):

   # def __init__(self, app):
   #     super().__init__(app)
        
    async def dispatch(self, request: Request, call_next):
        try:
            log = await generate_fastapi_request_log(request)
            logger.info("a %(a)d b %(b)s", {'a':1, 'b':2})
            logging.LogRecord
            response = await call_next(request)
            return response
    #        response_body = ""
    #        if response.headers.get("content-type") == "application/json":
    #            response_body = [chunk async for chunk in response.body_iterator]
    #            response.body_iterator = iterate_in_threadpool(iter(response_body))
        except Exception as e:
            logger.error(json.loads(ErrorLog(error_message=str(e)).model_dump_json()))
            
