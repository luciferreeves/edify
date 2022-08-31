from abc import ABC


class Builder(ABC):
    def __str__(self):
        return self.build()
