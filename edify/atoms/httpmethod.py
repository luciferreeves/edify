"""``httpmethod`` — HTTP request-method name."""

from __future__ import annotations

from edify import Pattern, any_of

httpmethod = any_of(
    Pattern().string("OPTIONS"),
    Pattern().string("GET"),
    Pattern().string("HEAD"),
    Pattern().string("POST"),
    Pattern().string("PUT"),
    Pattern().string("DELETE"),
    Pattern().string("TRACE"),
    Pattern().string("CONNECT"),
    Pattern().string("PATCH"),
)
"""Composable :class:`Pattern` fragment for an HTTP request method."""
