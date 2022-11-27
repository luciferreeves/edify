import re

proto = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
no_proto = "^[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"


def url(url: str, match: list = ["proto", "no_proto"]) -> bool:
    """Checks if a string is a valid URL.

    Args:
        url (str): The string to check.
        match (list): The protocols to match against. Defaults to ["https", "http", "no_proto"].
    Returns:
        bool: True if the string is a valid URL, False otherwise.
    """

    # Validate match argument
    if not isinstance(match, list):
        raise TypeError("match argument must be a list")

    if not match:
        raise ValueError("match argument must not be empty")

    # Validate protocols
    protocols = []
    for protocol in match:
        if protocol == "proto":
            protocols.append(proto)
        elif protocol == "no_proto":
            protocols.append(no_proto)
        else:
            raise ValueError("Invalid protocol: {}".format(protocol))

    # Check if URL matches any of the protocols
    for protocol in protocols:
        if re.match(protocol, url):
            return True

    return False
