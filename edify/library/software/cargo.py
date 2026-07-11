"""``cargo`` — Rust Cargo crate identifier shape (``name`` or ``name@version``)."""
from __future__ import annotations
from edify.library._support.regex import RegexBackedPattern
cargo = RegexBackedPattern(r"^[a-zA-Z][a-zA-Z0-9_-]{0,63}(?:@\d+(?:\.\d+){0,3}(?:[-.+][a-zA-Z0-9.\-]+)?)?$")
"""Callable :class:`Pattern` for a Cargo crate identifier."""
