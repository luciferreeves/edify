from .abc import Builder


class Escaped(Builder):
    def __init__(self, target):
        self.target = target

    def build(self):
        return f"\\{self.target}"
