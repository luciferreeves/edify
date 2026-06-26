"""Basic email-shape validator.

Validates the common email shape used in most application UX (local-part,
``@``, domain with at least one dot). Lower-case only.
"""

from __future__ import annotations

import re

_EMAIL_PATTERN = re.compile(
    r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*"
    r"@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
)


def email(value: str) -> bool:
    """Return True when ``value`` matches the common email shape.

    Args:
        value: The string to check.

    Returns:
        True for valid basic-shape email addresses; False otherwise.
    """
    return _EMAIL_PATTERN.match(value) is not None
