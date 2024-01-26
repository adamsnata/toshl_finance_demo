from dataclasses import dataclass
from enum import Enum


@dataclass
class Category:
    id: str
    name: str


@dataclass
class Tag:
    id: str
    name: str


class EntryType(Enum):
    EXPENSE = 1
    INCOME = 2
