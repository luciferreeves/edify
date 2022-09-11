import re

date_pattern = "^[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}$"
iso_date_pattern = "^(?:\\d{4})-(?:\\d{2})-(?:\\d{2})T(?:\\d{2}):(?:\\d{2}):(?:\\d{2}(?:\\.\\d*)?)(?:(?:-(?:\\d{2}):(?:\\d{2})|Z)?)$" # noqa


def date(date: str) -> bool:
    """Checks if a string is a valid date.

    Args:
        date (str): The string to check.
    Returns:
        bool: True if the string is a valid date, False otherwise.
    """

    if re.match(date_pattern, date):
        return True
    else:
        return False


def iso_date(date: str) -> bool:
    """Checks if a string is a valid ISO date.

    Args:
        date (str): The string to check.
    Returns:
        bool: True if the string is a valid ISO date, False otherwise.
    """

    if re.match(iso_date_pattern, date):
        return True
    else:
        return False
