"""Collapse fusable char-class elements inside an ``any_of`` alternation.

Inside an :class:`AnyOfElement`, child elements that resolve to a single
character or a character range can collapse into one ``[...]`` bracket
expression. Anything that does not collapse remains in the alternation and
joins via ``|``. This module partitions the children and renders the
combined char-class body.
"""

from __future__ import annotations

from edify.elements.types.base import BaseElement
from edify.elements.types.chars import AnyOfCharsElement, CharElement, RangeElement


def fuse_char_class_members(
    children: tuple[BaseElement, ...],
) -> tuple[str, tuple[BaseElement, ...]]:
    """Split ``children`` into the fused char-class body and the non-fusable tail.

    Args:
        children: The ordered child elements of an :class:`AnyOfElement`.

    Returns:
        A tuple ``(fused_body, remainder)`` where ``fused_body`` is the
        joined char-class fragment (empty string when nothing fuses) and
        ``remainder`` is the tuple of children that must be rendered as
        alternation arms instead.
    """
    fusable_members, remainder = _partition_by_fusability(children)
    fragments = [_fragment_for(member) for member in fusable_members]
    fused_body = "".join(fragments)
    return fused_body, remainder


def _is_fusable(member: BaseElement) -> bool:
    """Return True when ``member`` can collapse into the shared char-class body."""
    return isinstance(member, CharElement | AnyOfCharsElement | RangeElement)


def _partition_by_fusability(
    children: tuple[BaseElement, ...],
) -> tuple[tuple[BaseElement, ...], tuple[BaseElement, ...]]:
    """Split ``children`` into ``(fusable, non_fusable)`` preserving input order."""
    fusable: list[BaseElement] = []
    non_fusable: list[BaseElement] = []
    for member in children:
        if _is_fusable(member):
            fusable.append(member)
        else:
            non_fusable.append(member)
    return tuple(fusable), tuple(non_fusable)


def _fragment_for(member: BaseElement) -> str:
    """Return the char-class fragment produced by a single fusable element."""
    if isinstance(member, CharElement):
        return member.value
    if isinstance(member, AnyOfCharsElement):
        return member.value
    assert isinstance(member, RangeElement)
    return f"{member.start}-{member.end}"
