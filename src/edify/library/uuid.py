import re

pattern = "^[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}$"


def uuid(uuid: str) -> bool:
    """Checks if a string is a valid UUID.

    Args:
        uuid (str): The string to check.
    Returns:
        bool: True if the string is a valid UUID, False otherwise.
    """
    return re.match(pattern, uuid) is not None
