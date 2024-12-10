from typing import Dict, Callable
from pydantic import Field, BaseModel
from pydantic_settings import BaseSettings
from loggers.filters.default import SensitiveDataFilter
class Formatter(BaseModel):
    instantiator: str = Field(alias="()", default="uvicorn.logging.DefaultFormatter")
    fmt: str = "[%(levelname)s] - %(asctime)s - %(name)s - %(message)s"

class Filter(BaseModel):
    instantiator: Callable = Field(alias="()", default=SensitiveDataFilter)

class ConsoleHandler(BaseModel):
    class_: str = Field(alias="class", default="logging.StreamHandler")
    formatter: str = "default_formatter"
    level: str = "DEBUG"
    stream: str = "ext://sys.stdout"
    filters: list[str] = ["default_filter"]

class FileHandler(BaseModel):
    formatter: str = "default"
    class_: str = Field(alias="class", 
                        default="logging.handlers.RotatingFileHandler")
    level: str = "DEBUG"
    filename: str = "log.log"
    mode: str = "a"
    
class Handler(BaseModel): 
    console: ConsoleHandler 
    file: FileHandler
    
class Logger(BaseModel):
    handlers: list[str]
    level: str
    propagate: bool

class LoggingSettings(BaseSettings):
    version: int = 1 
    disable_existing_loggers: bool = False
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
        "main_logger": Logger(
            handlers=["console", "file"],
            level="info",
            propagate=False
        ).model_dump(by_alias=True)
    }