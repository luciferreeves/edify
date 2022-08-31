from .abc import Builder

class RegexBuilder(Builder):
    def __init__(self):
        self.parts = []

    def build(self):
        return "".join(map(str, self.parts))

    def add(self, part):
        if not (issubclass(type(part), Builder) or isinstance(part, str)):
            raise ValueError(f"{part} is not a valid Part")

        self.parts.append(part)
        return self
