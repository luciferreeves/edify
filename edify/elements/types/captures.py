"""Capture-group and back-reference element classes.

Capture-group elements collect child elements and emit a parenthesised group
that the underlying ``re`` engine numbers. Back-references re-match what a
capture group already matched, addressed by index (``\\1``) or by name
(``\\k<name>`` on emit, ``(?P=name)`` for the equivalent stdlib form).

* :class:`CaptureElement` — ``(...)`` numbered capture.
* :class:`NamedCaptureElement` — ``(?P<name>...)`` named capture.
* :class:`BackReferenceElement` — ``\\<index>`` numbered back-reference.
* :class:`NamedBackReferenceElement` — ``(?P=name)`` named back-reference.

Recursive ``children`` references use :class:`BaseElement` so the dataclass
field annotations type-check without importing the full ``Element`` union
(which would form a cycle).
"""

from __future__ import annotations

from dataclasses import dataclass, field

from edify.elements.types.base import BaseElement


@dataclass(frozen=True)
class CaptureElement(BaseElement):
    """A numbered capture group containing an ordered list of child elements.

    Attributes:
        children: The elements rendered inside the parentheses, in order.
    """

    children: tuple[BaseElement, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class NamedCaptureElement(BaseElement):
    """A named capture group rendered as ``(?P<name>...)``.

    Attributes:
        name: The capture-group name (alphanumerics and underscores, leading alpha).
        children: The elements rendered inside the parentheses, in order.
    """

    name: str
    children: tuple[BaseElement, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class BackReferenceElement(BaseElement):
    """A back-reference addressed by capture-group index.

    Attributes:
        index: The 1-based capture-group index.
    """

    index: int


@dataclass(frozen=True)
class NamedBackReferenceElement(BaseElement):
    """A back-reference addressed by capture-group name.

    Attributes:
        name: The name of the previously-declared :class:`NamedCaptureElement`.
    """

    name: str
