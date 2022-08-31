"""
    This file contains the datatypes used by the edify regex builder.

    The datatypes are:
        - letter: A single upper or lowercase letter (a-z or A-Z)
        - digit: A single digit (0-9)
        - word: A single word (a-z, A-Z, 0-9, _)
        - space: A single space (\s)
        - any: Any character or special character
"""


def letter(type: str = "all") -> str:
    """Returns a regex that matches a single letter.

        Parameters:
            type (str): The type of letter to match.
                - "all" (default): Matches any letter (a-z or A-Z)
                - "upper": Matches any upper case letter (A-Z)
                - "lower": Matches any lower case letter (a-z)

        Returns:
            str: A regex that matches a single letter.

        Raises:
            ValueError: If any of the parameters are invalid.
    """
    letters = "abcdefghijklmnopqrstuvwxyz"
    if type == "upper":
        letters = letters.upper()
    elif type == "lower":
        letters = letters
    elif type == "all":
        letters = letters + letters.upper()
    else:
        raise ValueError("Invalid letter type: " + type)
    return "[" + letters + "]"


def digit() -> str:
    """Returns a regex that matches a single digit.

        Returns:
            str: A regex that matches a single digit.
    """
    return "[1234567890]"


def word() -> str:
    """Returns a regex that matches a single word.

        Returns:
            str: A regex that matches a single word.
    """
    return "[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_]"


def space() -> str:
    """Returns a regex that matches a single space.

        Returns:
            str: A regex that matches a single space.
    """
    return "[\s]"


def any() -> str:
    """Returns a regex that matches any character.

        Returns:
            str: A regex that matches any character.
    """
    return "."
