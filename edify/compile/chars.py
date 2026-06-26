"""Render character-shaped elements to their regex string.

Covers single characters, multi-character literals, ranges, character
classes, and their negated variants. Values arrive already escaped from
the builder, so this module never calls into :mod:`edify.compile.escape`.
"""

from __future__ import annotations

from edify.elements.types.chars import (
    AnyOfCharsElement,
    AnythingButCharsElement,
    AnythingButRangeElement,
    AnythingButStringElement,
    CharElement,
    RangeElement,
    StringElement,
)
from edify.elements.types.union import CharShapedElement


def render_char_shaped(element: CharShapedElement) -> str:
    """Return the regex string produced by the given character-shaped element.

    Args:
        element: One of the seven char-shaped element classes.

    Returns:
        The rendered regex fragment.
    """
    match element:
        case CharElement(value=character):
            return character
        case StringElement(value=literal):
            return literal
        case RangeElement(start=lower_bound, end=upper_bound):
            return f"[{lower_bound}-{upper_bound}]"
        case AnyOfCharsElement(value=characters):
            return f"[{characters}]"
        case AnythingButCharsElement(value=characters):
            return f"[^{characters}]"
        case AnythingButRangeElement(start=lower_bound, end=upper_bound):
            return f"[^{lower_bound}-{upper_bound}]"
        case AnythingButStringElement(value=literal):
            per_character_negations = [f"[^{character}]" for character in literal]
            joined_negations = "".join(per_character_negations)
            return f"(?:{joined_negations})"
