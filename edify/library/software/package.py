"""``package`` — package identifier shape (``@scope/name`` or ``name``)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

package = RegexBackedPattern(r"^(?:@[a-z0-9][a-z0-9-]*/)?[a-z0-9][a-z0-9._-]{0,213}$")
"""Callable :class:`Pattern` for an npm/pypi-style package identifier."""
