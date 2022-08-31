import re

pattern = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
def email(email: str) -> bool:
    """Checks if a string is a valid email address.

    Args:
        email (str): The string to check.
    Returns:
        bool: True if the string is a valid email address, False otherwise.
    """

    if re.match(pattern, email):
        return True
    else:
        return False
