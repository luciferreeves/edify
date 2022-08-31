"""This is the main module for the edify builder. It is responsible for building
Regular Expressions from simple function chains.
"""

class RegexBuilder:
    """RegexBuilder helps build and use regular expressions using its methods.
    """

    regex = None

    def __init__(self):
        """Initialize the RegexBuilder.
        """
        self.regex = ""
