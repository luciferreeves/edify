"""Render the top-of-tree :class:`RootElement` to its full regex string.

The root holds the ordered list of top-level children that make up the
whole pattern. Rendering it is the concatenation of every child's
rendered fragment.
"""

from __future__ import annotations

from edify.compile.types import ElementRenderer
from edify.elements.types.root import RootElement


def render_root(root: RootElement, render_element: ElementRenderer) -> str:
    """Return the regex string produced by the root element's children.

    Args:
        root: The top-of-tree element holding every child of the pattern.
        render_element: The dispatcher callable used to render each child.

    Returns:
        The concatenated regex string for the whole pattern.
    """
    rendered_children = [render_element(child) for child in root.children]
    return "".join(rendered_children)
