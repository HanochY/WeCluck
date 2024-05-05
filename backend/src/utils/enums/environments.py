from enum import auto
from strenum import UppercaseStrEnum

class Environment(UppercaseStrEnum):
    integration = auto()
    production = auto()
