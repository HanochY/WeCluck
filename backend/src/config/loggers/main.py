from typing import Dict, Callable
from pydantic import Field, BaseModel
from pydantic_settings import BaseSettings
from config.loggers.filters.default import SensitiveDataFilter
class Formatter(BaseModel):
    instantiator: str = Field(alias="()", default="uvicorn.logging.DefaultFormatter")
    fmt: str = "[%(levelname)s] - %(asctime)s - %(name)s - %(message)s"
    use_colors: bool = True

class Filter(BaseModel):
    instantiator: Callable = Field(alias="()", default=SensitiveDataFilter)
class Handler(BaseModel): 
    pass
class ConsoleHandler(Handler):
    class_: str = Field(alias="class", default="logging.StreamHandler")
    formatter: str = "default_formatter"
    level: str = "INFO"
    stream: str = "ext://sys.stdout"
    filters: list[str] = ["default_filter"]

class FileHandler(Handler):
    formatter: str = "default"
    class_: str = Field(alias="class", 
                        default="logging.handlers.RotatingFileHandler")
    level: str = "ERROR"
    filename: str = "log.log"
    mode: str = "a"
    

    
class Logger(BaseModel):
    handlers: list[str]
    level: str
    propagate: bool

class Logging:
    class Development(BaseSettings):
        version: int = 1 
        disable_existing_loggers: bool = True
        formatters: Dict[str, Formatter] = {
            "default_formatter": Formatter().model_dump(by_alias=True)
        }
        filters: Dict[str, Filter] = {
            "default_filter": Filter().model_dump(by_alias=True)
        }
        handlers: Dict[str, Handler] = {
            "console": ConsoleHandler(level="DEBUG").model_dump(by_alias=True),
            "file": FileHandler().model_dump(by_alias=True)
        }
        loggers: Dict[str, Logger] = {
            "uvicorn.access": Logger(
                handlers=["console", "file"],
                level="DEBUG",
                propagate=False
            ).model_dump(by_alias=True)
        }
        
    class Production(BaseSettings):
        version: int = 1 
        disable_existing_loggers: bool = True
        formatters: Dict[str, Formatter] = {
            "default_formatter": Formatter().model_dump(by_alias=True)
        }
        filters: Dict[str, Filter] = {
            "default_filter": Filter().model_dump(by_alias=True)
        }
        handlers: Dict[str, Handler] = {
            "console": ConsoleHandler().model_dump(by_alias=True),
            "file": FileHandler().model_dump(by_alias=True)
        }
        loggers: Dict[str, Logger] = {
            "uvicorn.access": Logger(
                handlers=["console", "file"],
                level="INFO",
                propagate=False
            ).model_dump(by_alias=True)
        }