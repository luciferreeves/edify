"""``mfa`` — MFA/TOTP six-to-eight digit code shape."""

from __future__ import annotations

from edify import Pattern

mfa = (
    Pattern()
    .start_of_input()
    .between(6, 8).digit()
    .end_of_input()
)
"""Callable :class:`Pattern` for the MFA/TOTP code shape: 6–8 decimal digits."""
