from pydantic import BaseModel
from datetime import datetime
class BaseEntity(BaseModel):
    id: int
    created_at: datetime
    created_by: str
    modified_at: datetime
    modified_by: str