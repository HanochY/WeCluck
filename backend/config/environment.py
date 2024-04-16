from enum import auto
from strenum import UppercaseStrEnum

class Emvironment(UppercaseStrEnum):
    integration = auto()
    production = auto()
