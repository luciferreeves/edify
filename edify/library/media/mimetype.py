"""``mimetype`` — RFC 6838 MIME type shape."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

mimetype = RegexBackedPattern(r"^[a-zA-Z][a-zA-Z0-9!#$&\-^_.+]*/[a-zA-Z][a-zA-Z0-9!#$&\-^_.+]*$")
"""Callable :class:`Pattern` for the ``type/subtype`` MIME shape."""
