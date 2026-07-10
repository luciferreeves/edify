"""Character-shaped element classes — single chars, strings, ranges, char classes.

These elements carry a value (a character, a string, or a pair of range
bounds) and emit the corresponding regex fragment at compile time.

* :class:`CharElement` — a single literal character.
* :class:`StringElement` — a multi-character literal; needs grouping when
  followed by a quantifier.
* :class:`RangeElement` — an inclusive ``[a-z]`` character range.
* :class:`AnyOfCharsElement` — an inline ``[abc]`` character class.
* :class:`AnythingButCharsElement` — an inline ``[^abc]`` negated class.
* :class:`AnythingButRangeElement` — a negated ``[^a-z]`` range.
* :class:`AnythingButStringElement` — a sequence of negated single-character classes.
"""

from __future__ import annotations

from dataclasses import dataclass

from edify.elements.types.base import BaseElement


@dataclass(frozen=True)
class CharElement(BaseElement):
    """A single literal character.

    Attributes:
        value: The character to match; already escaped for the compile path.
    """

    value: str


@dataclass(frozen=True)
class StringElement(BaseElement):
    """A multi-character literal string.

    Attributes:
        value: The string to match; already escaped for the compile path.
    """

    value: str


@dataclass(frozen=True)
class RangeElement(BaseElement):
    """An inclusive character range, rendered as ``[<start>-<end>]``.

    Attributes:
        start: The lower bound, a single character.
        end: The upper bound, a single character.
    """

    start: str
    end: str


@dataclass(frozen=True)
class AnyOfCharsElement(BaseElement):
    """An inline character class containing one or more characters.

    Attributes:
        value: The set of characters to match; already escaped for the compile path.
    """

    value: str


@dataclass(frozen=True)
class AnythingButCharsElement(BaseElement):
    """A negated character class, rendered as ``[^<value>]``.

    Attributes:
        value: The set of characters to reject; already escaped for the compile path.
    """

    value: str


@dataclass(frozen=True)
class AnythingButRangeElement(BaseElement):
    """A negated character range, rendered as ``[^<start>-<end>]``.

    Attributes:
        start: The lower bound, a single character.
        end: The upper bound, a single character.
    """

    start: str
    end: str


@dataclass(frozen=True)
class AnythingButStringElement(BaseElement):
    """A non-capturing group of per-character negations.

    Attributes:
        value: The string whose characters are each negated; already escaped for the compile path.
    """

    value: str
