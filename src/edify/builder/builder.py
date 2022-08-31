from .abc import Builder
from .part import Part
from .errors import NotPart
from re import match


class RegexBuilder(Builder):
    def __init__(self):
        self.parts = []

    def build(self):
        return "".join(map(str, self.parts))

    def add(self, part):
        self.parts.append(part)

    def part(self, part):
        if not (issubclass(type(part), Builder) or isinstance(part, str)):
            raise NotPart(f"{part} is not a valid Part")

        self.parts.append(part)
        return self

    def match(self, regex):
        return match(self.build(), regex)
