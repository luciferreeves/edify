from abc import ABC
from abc import abstractmethod


class Builder(ABC):
    @abstractmethod
    def build(self):
        pass

    def __str__(self):
        return self.build()
