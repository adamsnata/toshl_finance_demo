from enum import Enum


class Context(Enum):
    CLOUD = 'cloud'
    LOCAL = 'local'

    def __str__(self):
        return self.value
