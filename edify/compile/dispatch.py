"""Top-level compile entry — render any :data:`Element` to its regex string.

Routes the element to the per-family renderer based on which union it
belongs to. The renderers that need to recurse into children receive
:func:`render_element` itself as their renderer argument, keeping the
recursive call site explicit instead of relying on circular imports.
"""

from __future__ import annotations

from edify.compile.captures import render_capture_group
from edify.compile.chars import render_char_shaped
from edify.compile.groups import render_grouping
from edify.compile.leaves import render_leaf
from edify.compile.quantifier import render_quantifier
from edify.compile.root import render_root
from edify.elements.types.root import RootElement
from edify.elements.types.union import (
    CaptureGroupElement,
    CharShapedElement,
    Element,
    GroupingElement,
    LeafElement,
    QuantifierElement,
)
from edify.errors.internal import UnknownElementTypeError


def render_element(element: Element) -> str:
    """Return the regex string produced by any element.

    Args:
        element: Any concrete element class in the :data:`Element` union.

    Returns:
        The rendered regex fragment for the element.

    Raises:
        UnknownElementTypeError: If ``element`` is not one of the recognised
            element kinds (which would indicate an AST built outside the builder).
    """
    if isinstance(element, LeafElement):
        return render_leaf(element)
    if isinstance(element, CharShapedElement):
        return render_char_shaped(element)
    if isinstance(element, CaptureGroupElement):
        return render_capture_group(element, render_element)
    if isinstance(element, GroupingElement):
        return render_grouping(element, render_element)
    if isinstance(element, QuantifierElement):
        return render_quantifier(element, render_element)
    if isinstance(element, RootElement):
        return render_root(element, render_element)
    element_type_name = type(element).__name__
    raise UnknownElementTypeError(element_type_name)
