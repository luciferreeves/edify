from abc import abstractmethod

from .abc import Builder


class Quantifier(Builder):
    def __init__(self, target):
        self.target = target

    @abstractmethod
    def build(self):
        pass


class Optional(Quantifier):
    def build(self):
        return f"{self.target}?"


class ZeroOrMore(Quantifier):
    def build(self):
        return f"{self.target}*"


class OneOrMore(Quantifier):
    def build(self):
        return f"{self.target}+"


class Exact(Quantifier):
    def __init__(self, target, count):
        super().__init__(target)
        self.count = count

    def build(self):
        return f"{self.target}{{self.count}}"


class Range(Quantifier):
    def __init__(self, target, min, max):
        super().__init__(target)
        self.min = min
        self.max = max

    def build(self):
        return f"{self.target}{{self.min, self.max}}"


class AtLeast(Quantifier):
    def __init__(self, target, min):
        super().__init__(target)
        self.min = min

    def build(self):
        return f"{self.target}{{self.min,}}"


class AtMost(Quantifier):
    def __init__(self, target, max):
        super().__init__(target)
        self.max = max

    def build(self):
        return f"{self.target}{{,self.max}}"
