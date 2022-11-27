import re

from .support.zip import ZIP_LOCALES

locales = [locale["abbrev"] for locale in ZIP_LOCALES]


def zip(zip: str, locale: str = "US") -> bool:
    """Check if a string is a valid zip code.

    Args:
        zip (str): The string to check.
        locale (str): (optional) The locale to check against. Defaults to "US".
    Returns:
        bool: True if the string is a valid zip code, False otherwise.
    """

    if not isinstance(locale, str):
        raise TypeError("locale must be a string")

    if locale == "":
        raise ValueError("locale cannot be empty")

    if locale not in locales:
        print(locales)
        raise ValueError("locale must be one of {}".format(locales))

    pattern = ZIP_LOCALES[locales.index(locale)]["zip"]
    return re.match(pattern, zip) is not None
