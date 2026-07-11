"""``url`` — HTTP/HTTPS URL shape (with or without protocol)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

url = RegexBackedPattern(
    r"^(?:https?://)?"
    r"(?:www\.)?"
    r"[-a-zA-Z0-9@:%._\+~#=]{1,256}"
    r"\.[a-zA-Z0-9()]{1,6}"
    r"\b(?:[-a-zA-Z0-9()@:%_\+.~#?&/=]*)$"
)
"""Callable :class:`Pattern` for the URL shape: optional ``http[s]://``,
optional ``www.``, host with dot-separated labels, TLD, and optional path.
"""
