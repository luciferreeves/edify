"""Render capture-group and back-reference elements to their regex string.

Capture and named-capture render their children recursively, so they take
an :data:`edify.compile.types.ElementRenderer` callable as a parameter
(the dispatcher passes itself). Back-references take no children and render
to a fixed-shape string.
"""

from __future__ import annotations

from edify.compile.types import ElementRenderer
from edify.elements.types.captures import (
    BackReferenceElement,
    CaptureElement,
    NamedBackReferenceElement,
    NamedCaptureElement,
)
from edify.elements.types.union import CaptureGroupElement


def render_capture_group(element: CaptureGroupElement, render_element: ElementRenderer) -> str:
    """Return the regex string produced by a capture or back-reference element.

    Args:
        element: One of the four capture-group element classes.
        render_element: The dispatcher callable used to render child elements.

    Returns:
        The rendered regex fragment.
    """
    match element:
        case CaptureElement(children=child_elements):
            rendered_children = [render_element(child) for child in child_elements]
            joined_children = "".join(rendered_children)
            return f"({joined_children})"
        case NamedCaptureElement(name=capture_name, children=child_elements):
            rendered_children = [render_element(child) for child in child_elements]
            joined_children = "".join(rendered_children)
            return f"(?P<{capture_name}>{joined_children})"
        case BackReferenceElement(index=capture_index):
            return f"\\{capture_index}"
        case NamedBackReferenceElement(name=capture_name):
            return f"(?P={capture_name})"
