from fastapi.requests import Request
from uuid import uuid4
import json
from dal._schema.logs.request import RequestLog


async def generate_fastapi_request_log(request: Request) -> RequestLog:
    return RequestLog(
        method = request.method,
        route = request['path'],
        ip = request.client.host,
        url = request.url,
        host = request.url.hostname,
        body = json.loads(await request.body() or "{}"),
        headers = dict(request.headers.items())
    )