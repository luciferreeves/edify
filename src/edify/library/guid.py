import re

pattern = "^(?:\\{{0,1}(?:[0-9a-fA-F]){8}-(?:[0-9a-fA-F]){4}-(?:[0-9a-fA-F]){4}-(?:[0-9a-fA-F]){4}-(?:[0-9a-fA-F]){12}\\}{0,1})$"


def guid(guid: str) -> bool:
    """Check if the given string is a valid GUID.

    Args:
        guid (str): The string to check.

    Returns:
        bool: True if the string is a valid GUID, False otherwise.
    """
    return bool(re.match(pattern, guid))
