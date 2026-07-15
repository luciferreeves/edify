"""Functional assertion factories — the free-function counterpart to :class:`AssertionsMixin`.

Each factory returns a fresh :class:`Pattern` whose root frame holds a
single lookaround element wrapping the supplied operand's children.

* :func:`assert_ahead` — ``(?=...)``.
* :func:`assert_not_ahead` — ``(?!...)``.
* :func:`assert_behind` — ``(?<=...)``.
* :func:`assert_not_behind` — ``(?<!...)``.
"""

from __future__ import annotations

from edify.builder.types.protocol import BuilderProtocol
from edify.elements.types.base import BaseElement
from edify.elements.types.groups import (
    AssertAheadElement,
    AssertBehindElement,
    AssertNotAheadElement,
    AssertNotBehindElement,
)
from edify.pattern.composition import Pattern
from edify.pattern.factories.wrap import pattern_containing


def assert_ahead(operand: BuilderProtocol) -> Pattern:
    """Return a positive lookahead ``(?=operand)``."""
    return pattern_containing(AssertAheadElement(children=_operand_children(operand)))


def assert_not_ahead(operand: BuilderProtocol) -> Pattern:
    """Return a negative lookahead ``(?!operand)``."""
    return pattern_containing(AssertNotAheadElement(children=_operand_children(operand)))


def assert_behind(operand: BuilderProtocol) -> Pattern:
    """Return a positive lookbehind ``(?<=operand)``."""
    return pattern_containing(AssertBehindElement(children=_operand_children(operand)))


def assert_not_behind(operand: BuilderProtocol) -> Pattern:
    """Return a negative lookbehind ``(?<!operand)``."""
    return pattern_containing(AssertNotBehindElement(children=_operand_children(operand)))


def _operand_children(operand: BuilderProtocol) -> tuple[BaseElement, ...]:
    """Return ``operand``'s root-frame children as an immutable tuple."""
    return tuple(operand._state.top_frame.children)
