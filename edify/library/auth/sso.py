"""``sso`` — SSO ticket/assertion shape (base64 or hex, 20–2048 chars)."""

from __future__ import annotations

from edify import Pattern

sso = (
    Pattern()
    .start_of_input()
    .between(20, 2048)
    .any_of().range("A", "Z").range("a", "z").range("0", "9").any_of_chars("+/=_-.").end()
    .end_of_input()
)
"""Callable :class:`Pattern` for an SSO ticket/assertion opaque payload:
20–2048 base64-family characters (letters, digits, ``+``, ``/``, ``=``,
``_``, ``-``, ``.``).
"""
