import logging
import re
from typing import Annotated, Dict, Callable
from pydantic import Field, BaseModel
from pydantic_settings import BaseSettings

class SensitiveDataFilter(logging.Filter):
    # Define a list of keys that values are sensitive data
    SENSITIVE_KEYS = (
        "credentials",
        "authorization",
        "token",
        "password",
        "access_token",
    )
    TOKEN_PATTERN = rf"token=([^;]+)"

    def filter(self, record):
        try:
            record.args = self.mask_sensitive_args(record.args)
            record.msg = self.mask_sensitive_msg(record.msg)
            return True
        except Exception as e:
            return True

    def mask_sensitive_args(self, args):
        if isinstance(args, dict):
            new_args = args.copy()
            for key in args.keys():
                if key.lower() in self.SENSITIVE_KEYS:
                    new_args[key] = "******"
                else:
                    # mask sensitive data in dict values
                    new_args[key] = self.mask_sensitive_msg(args[key])
            return new_args
        # when there are multi arg in record.args
        return tuple([self.mask_sensitive_msg(arg) for arg in args])

    def mask_sensitive_msg(self, message):
        # mask sensitive data in multi record.args
        if isinstance(message, dict):
            return self.mask_sensitive_args(message)
        if isinstance(message, str):
            replace = f"token=******"
            message = re.sub(self.TOKEN_PATTERN, replace, message)
        return message


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