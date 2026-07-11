"""``digest`` — content-addressable digest shape (``algorithm:hex``)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

digest = RegexBackedPattern(r"^(?:sha256|sha512|sha1|md5|blake2[bs]?)(?::|-)[a-fA-F0-9]{32,128}$")
"""Callable :class:`Pattern` for a content-addressable digest."""
