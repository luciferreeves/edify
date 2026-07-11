"""``roman`` — Roman-numeral shape (1-3999)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

roman = RegexBackedPattern(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")
"""Callable :class:`Pattern` for a Roman-numeral value 1-3999."""
