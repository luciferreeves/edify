import re

mac_address_validate_pattern = "^(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})$"


def mac(mac: str) -> bool:
    """Validate a MAC (IEEE 802) address.

    Args:
        mac (str): The MAC address to validate.

    Returns:
        bool: True if the MAC address is valid, False otherwise.
    """
    if not isinstance(mac, str):
        return False
    return bool(re.match(mac_address_validate_pattern, mac))
