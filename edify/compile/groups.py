"""Render grouping elements to their regex string.

Covers non-capturing groups, alternation (with char-class fusion),
subexpressions, and the four lookaround assertions. Each renderer recurses
into the element's children via the passed :data:`ElementRenderer` callable.
"""

from __future__ import annotations

from edify.compile.fuse import fuse_char_class_members
from edify.compile.types import ElementRenderer
from edify.elements.types.base import BaseElement
from edify.elements.types.groups import (
    AnyOfElement,
    AssertAheadElement,
    AssertBehindElement,
    AssertNotAheadElement,
    AssertNotBehindElement,
    GroupElement,
    SubexpressionElement,
)
from edify.elements.types.union import GroupingElement


def render_grouping(element: GroupingElement, render_element: ElementRenderer) -> str:
    """Return the regex string produced by a grouping element.

    Args:
        element: One of the seven grouping element classes.
        render_element: The dispatcher callable used to render child elements.

    Returns:
        The rendered regex fragment.
    """
    match element:
        case GroupElement(children=child_elements):
            return _render_non_capturing_group(child_elements, render_element)
        case SubexpressionElement(children=child_elements):
            return _render_subexpression(child_elements, render_element)
        case AnyOfElement(children=child_elements):
            return _render_alternation(child_elements, render_element)
        case AssertAheadElement(children=child_elements):
            inner = _render_concatenation(child_elements, render_element)
            return f"(?={inner})"
        case AssertNotAheadElement(children=child_elements):
            inner = _render_concatenation(child_elements, render_element)
            return f"(?!{inner})"
        case AssertBehindElement(children=child_elements):
            inner = _render_concatenation(child_elements, render_element)
            return f"(?<={inner})"
        case AssertNotBehindElement(children=child_elements):
            inner = _render_concatenation(child_elements, render_element)
            return f"(?<!{inner})"


def _render_concatenation(
    children: tuple[BaseElement, ...], render_element: ElementRenderer
) -> str:
    """Render a sequence of children and concatenate their fragments."""
    rendered = [render_element(child) for child in children]
    return "".join(rendered)


def _render_non_capturing_group(
    children: tuple[BaseElement, ...], render_element: ElementRenderer
) -> str:
    """Wrap the concatenated children in a non-capturing group."""
    inner = _render_concatenation(children, render_element)
    return f"(?:{inner})"


def _render_subexpression(
    children: tuple[BaseElement, ...], render_element: ElementRenderer
) -> str:
    """Render a subexpression as its raw concatenated children (no wrapping)."""
    return _render_concatenation(children, render_element)


def _render_alternation(children: tuple[BaseElement, ...], render_element: ElementRenderer) -> str:
    """Render an ``any_of`` element with char-class fusion for simple members."""
    fused_body, remaining_members = fuse_char_class_members(children)
    if not remaining_members:
        return f"[{fused_body}]"
    rendered_remainder = [render_element(member) for member in remaining_members]
    joined_remainder = "|".join(rendered_remainder)
    if not fused_body:
        return f"(?:{joined_remainder})"
    return f"(?:{joined_remainder}|[{fused_body}])"
