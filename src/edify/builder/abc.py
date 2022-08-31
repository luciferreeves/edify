from abc import ABC, abstractmethod


class Builder(ABC):
    @abstractmethod
    def build(self):
        pass

    def __str__(self):
        return self.build()
