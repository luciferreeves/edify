"""Render leaf elements to their regex string.

Every leaf in :mod:`edify.elements.types.leaves` maps to a fixed string that
never depends on children or quantifier state, so the renderer is a single
``match`` over the leaf union.
"""

from __future__ import annotations

from edify.elements.types.leaves import (
    AnyCharElement,
    CarriageReturnElement,
    DigitElement,
    EndOfInputElement,
    NewLineElement,
    NonDigitElement,
    NonWhitespaceCharElement,
    NonWordBoundaryElement,
    NonWordElement,
    NoopElement,
    NullByteElement,
    StartOfInputElement,
    TabElement,
    WhitespaceCharElement,
    WordBoundaryElement,
    WordElement,
)
from edify.elements.types.union import LeafElement


def render_leaf(element: LeafElement) -> str:
    """Return the regex string produced by the given leaf element.

    Args:
        element: One of the 16 leaf element classes.

    Returns:
        The exact regex fragment (e.g. ``"^"``, ``"\\d"``, ``""`` for noop).
    """
    match element:
        case StartOfInputElement():
            return "^"
        case EndOfInputElement():
            return "$"
        case AnyCharElement():
            return "."
        case WhitespaceCharElement():
            return "\\s"
        case NonWhitespaceCharElement():
            return "\\S"
        case DigitElement():
            return "\\d"
        case NonDigitElement():
            return "\\D"
        case WordElement():
            return "\\w"
        case NonWordElement():
            return "\\W"
        case WordBoundaryElement():
            return "\\b"
        case NonWordBoundaryElement():
            return "\\B"
        case NewLineElement():
            return "\\n"
        case CarriageReturnElement():
            return "\\r"
        case TabElement():
            return "\\t"
        case NullByteElement():
            return "\\0"
        case NoopElement():
            return ""
