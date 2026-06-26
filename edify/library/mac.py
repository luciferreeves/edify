"""MAC-address shape validator.

Validates the standard 6-octet IEEE 802 MAC address form (e.g.
``aa:bb:cc:dd:ee:ff`` or ``aa-bb-cc-dd-ee-ff``). Case-insensitive on the
hex digits.
"""

from __future__ import annotations

import re

_MAC_PATTERN = re.compile(r"^(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})$")


def mac(value: str) -> bool:
    """Return True when ``value`` matches the IEEE-802 MAC address shape.

    Args:
        value: The string to check.

    Returns:
        True for valid colon- or hyphen-separated 6-octet hex strings; False otherwise.
    """
    if not isinstance(value, str):
        return False
    return _MAC_PATTERN.match(value) is not None
