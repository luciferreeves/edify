"""US Social Security Number shape validator.

Validates the ``AAA-GG-SSSS`` shape with the documented blocked ranges:
``000``, ``666`` and ``9xx`` for the area, ``00`` for the group, ``0000``
for the serial. Shape-only — does not verify issuance.
"""

from __future__ import annotations

import re

_SSN_PATTERN = re.compile(r"^(?!666|000|9\d{2})\d{3}-(?!00)\d{2}-(?!0{4})\d{4}$")


def ssn(value: str) -> bool:
    """Return True when ``value`` matches the US SSN shape with blocked-range exclusions.

    Args:
        value: The string to check.

    Returns:
        True for valid ``AAA-GG-SSSS`` strings with the area / group /
        serial blocks respected; False otherwise.
    """
    if not isinstance(value, str):
        return False
    return _SSN_PATTERN.match(value) is not None
