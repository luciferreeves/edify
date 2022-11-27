import re


def password(
    password: str,
    min_length: int = 8,
    max_length: int = 64,
    min_upper: int = 1,
    min_lower: int = 1,
    min_digit: int = 1,
    min_special: int = 1,
    special_chars: str = "!@#$%^&*()_+-=[]{}|;':\",./<>?",
) -> bool:
    """Check if the given string is a valid password.

    Args:
        password (str): The string to check.
        min_length (int): The minimum length of the password.
        max_length (int): The maximum length of the password.
        min_upper (int): The minimum number of upper case characters.
        min_lower (int): The minimum number of lower case characters.
        min_digit (int): The minimum number of digits.
        min_special (int): The minimum number of special characters.
        special_chars (str): The special characters to check for.

    Returns:
        bool: True if the string is a valid password, False otherwise.
    """
    if len(password) < min_length or len(password) > max_length:
        return False

    upper = re.findall("[A-Z]", password or "")
    lower = re.findall("[a-z]", password or "")
    digit = re.findall("[0-9]", password or "")
    special = [c for c in password if c in special_chars]

    if len(upper) < min_upper or len(lower) < min_lower or len(digit) < min_digit or len(special) < min_special:
        return False

    return True
