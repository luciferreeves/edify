"""Render a quantifier element by combining its child with its suffix.

The quantifier suffix itself comes from
:func:`edify.compile.quantifier.suffix.quantifier_suffix`; this module
handles the surrounding logic of rendering the child element and wrapping
it in a non-capturing group when the regex grammar requires it (string
literals and subexpressions need ``(?:...)`` so the quantifier binds to
the whole fragment instead of only the last character).
"""

from __future__ import annotations

from edify.compile.quantifier.suffix import quantifier_suffix
from edify.compile.types import ElementRenderer
from edify.elements.types.base import BaseElement
from edify.elements.types.chars import StringElement
from edify.elements.types.groups import SubexpressionElement
from edify.elements.types.union import QuantifierElement


def render_quantifier(quantifier: QuantifierElement, render_element: ElementRenderer) -> str:
    """Return the regex string produced by a quantifier wrapping its child.

    Args:
        quantifier: One of the nine quantifier element classes.
        render_element: The dispatcher callable used to render the child element.

    Returns:
        The rendered child followed by the quantifier suffix, with the child
        wrapped in ``(?:...)`` when its grammar requires grouping.
    """
    child_element = quantifier.child
    rendered_child = render_element(child_element)
    grouped_child = _wrap_in_group_if_required(child_element, rendered_child)
    suffix = quantifier_suffix(quantifier)
    return f"{grouped_child}{suffix}"


def _wrap_in_group_if_required(child_element: BaseElement, rendered_child: str) -> str:
    """Return ``rendered_child`` wrapped in ``(?:...)`` when the child kind needs grouping."""
    if isinstance(child_element, StringElement | SubexpressionElement):
        return f"(?:{rendered_child})"
    return rendered_child
