from .abc import Builder
from abc import abstractmethod


class Part(Builder):
    def __init__(self, target):
        self.target = target

    @abstractmethod
    def build(self):
        pass


class Any(Part):
    def __init__(self, *targets, capture = True, name = None):
        if not capture and name:
            raise ValueError("Cannot specify group name without capturing")

        if name == "":
            raise ValueError("Cannot specify empty group name")

        super().__init__(targets)
        self.capture = capture
        self.name = name

    def build(self):
        targets = "|".join(map(str, self.target))
        capture = "" if self.capture else "?: "
        name = f"<{self.name}>" if self.name else ""
        return f"{capture}{name}{targets}"
