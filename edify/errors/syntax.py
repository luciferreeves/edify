"""Syntax error class for malformed builder chains and invalid builder input.

Raised when:

* a quantifier is applied with no operand (e.g. ``RegexBuilder().exactly(3).to_regex()``),
* a quantifier is stacked on another quantifier,
* a builder method receives an argument of the wrong type or shape,
* a frame is closed that was never opened.

Inherits from :class:`edify.errors.base.EdifyError` so any ``except EdifyError``
clause catches it too.
"""

from __future__ import annotations

from edify.errors.base import EdifyError


class EdifySyntaxError(EdifyError):
    """Raised when a builder chain is malformed or a builder method receives invalid input."""
