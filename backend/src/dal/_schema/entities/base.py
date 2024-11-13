from pydantic import BaseModel

class BaseEntity:
    class Base(BaseModel):
        pass

    class Public(BaseModel):
        pass

    class Private(BaseModel):
        pass

    class Create(BaseModel):
        pass

    class Read(BaseModel):
        pass

    class Update(BaseModel):
        pass
