from pydantic import BaseModel, create_model

    
def join(Model1: BaseModel, Model2: BaseModel,
         on_attr: str) -> BaseModel:
    return create_model("JoinedModel",
    **{f'{Model1.__name__.lower()}_{key}': (value.annotation, value)
       for key, value in list(Model1.__fields__.items()) if key != on_attr},
    **{f'{Model2.__name__.lower()}_{key}': (value.annotation, value)
       for key, value in list(Model2.__fields__.items())}
)
