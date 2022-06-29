
from enum import Enum


OUTPUT_FOLDER = ".\\result\\"

class ItemType(Enum):
    NEW = 0
    UPDATE = 1
    DELETE = 2
    NOCHANGE = 3