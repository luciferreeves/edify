"""``webauthn`` — WebAuthn assertion/attestation ID shape (base64url)."""

from __future__ import annotations

from edify import Pattern

webauthn = (
    Pattern()
    .start_of_input()
    .between(43, 512)
    .any_of().range("A", "Z").range("a", "z").range("0", "9").any_of_chars("_-").end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a WebAuthn credential/assertion base64url shape."""
