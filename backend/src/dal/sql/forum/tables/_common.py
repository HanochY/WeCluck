from sqlmodel import SQLModel, Field
from datetime import datetime
from dal._schema.metadata import Metadata as MetadataGlobal

class SQLModelCommon(SQLModel, MetadataGlobal):
    id: int | None = Field(default=None, primary_key=True)
    is_deleted: bool = Field(default=False)
    created_at: datetime = Field(default=datetime.now) 
    created_by: str
    modified_at: datetime = Field(default=datetime.now)
    modified_by: str
    deleted_at: datetime | None = Field(default=None)
    deleted_by: str | None