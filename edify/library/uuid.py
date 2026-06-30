"""UUID-shape validator.

Validates the canonical 8-4-4-4-12 hex form with the version digit pinned
to ``1``-``5`` and the variant digit pinned to ``8``, ``9``, ``a``, or
``b``. Lowercase hex only.
"""

from __future__ import annotations

import re

_UUID_PATTERN = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-5][0-9a-f]{3}-[089ab][0-9a-f]{3}-[0-9a-f]{12}$"
)


def uuid(value: str) -> bool:
    """Return True when ``value`` matches the canonical UUID 8-4-4-4-12 shape.

    Args:
        value: The string to check.

    Returns:
        True for valid lowercase-hex UUIDs; False otherwise.
    """
    return _UUID_PATTERN.match(value) is not None
