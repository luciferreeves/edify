"""RFC 5322 strict-email-shape validator.

Validates the full RFC 5322 mailbox shape — quoted-string local parts,
IP-literal domains, and the related corner cases. Use this when the
permissive :func:`edify.library.email.basic.email` is too lax.
"""

from __future__ import annotations

import re

_EMAIL_RFC_5322_PATTERN = re.compile(
    r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"
    r"\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|"
    r"\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")"
    r"@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|"
    r"\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}"
    r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:"
    r"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|"
    r"\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
)


def email_rfc_5322(value: str) -> bool:
    """Return True when ``value`` matches the RFC 5322 mailbox shape.

    Args:
        value: The string to check.

    Returns:
        True for valid RFC 5322 mailboxes; False otherwise.
    """
    return _EMAIL_RFC_5322_PATTERN.match(value) is not None
