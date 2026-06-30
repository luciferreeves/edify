"""IPv4-address shape validator.

Validates the standard dotted-quad ``a.b.c.d`` shape with each octet in
the ``0``-``255`` range.
"""

from __future__ import annotations

import re

_IPV4_PATTERN = re.compile(
    r"^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
    r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
    r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
    r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
)


def ipv4(value: str) -> bool:
    """Return True when ``value`` matches the dotted-quad IPv4 shape with bounded octets.

    Args:
        value: The string to check.

    Returns:
        True for valid IPv4 addresses (each octet ``0``-``255``); False otherwise.
    """
    return _IPV4_PATTERN.match(value) is not None
