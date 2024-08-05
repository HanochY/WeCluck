from typing_extensions import TypedDict
from datetime import datetime
class BaseEntity(TypedDict):
    id: int
    created_at: datetime
    created_by: str
    modified_at: datetime
    modified_by: str