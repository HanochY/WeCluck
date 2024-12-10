from pydantic import BaseModel
from uuid import UUID, uuid4

class RequestLog(BaseModel):
    req_id: UUID = uuid4()
    method: str
    route: str
    ip: str
    url: str
    host: str
    body: dict
    headers: dict
