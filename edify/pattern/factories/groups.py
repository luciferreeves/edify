"""Functional grouping factories — non-capturing groups, captures, alternation, back-references.

Each factory returns a fresh :class:`Pattern` whose root frame holds a
single grouping element built from the supplied operand(s).

* :func:`group` — wrap into a non-capturing ``(?:...)``.
* :func:`capture` — wrap into a numbered capture ``(...)``.
* :func:`named_capture` — wrap into ``(?P<name>...)``.
* :func:`back_reference` — emit ``\\<index>``.
* :func:`named_back_reference` — emit ``(?P=name)``.
* :func:`any_of` — emit ``(?:a|b|c)`` alternation across the operands.
"""

from __future__ import annotations

from edify.builder.types.protocol import BuilderProtocol
from edify.elements.types.base import BaseElement
from edify.elements.types.captures import (
    BackReferenceElement,
    CaptureElement,
    NamedBackReferenceElement,
    NamedCaptureElement,
)
from edify.elements.types.groups import AnyOfElement, GroupElement
from edify.errors.input import MustBeAtLeastTwoOperandsError, MustBePositiveIntegerError
from edify.pattern.composition import Pattern
from edify.pattern.factories.wrap import pattern_containing, target_element


def group(operand: BuilderProtocol) -> Pattern:
    """Return ``operand`` wrapped in a non-capturing ``(?:...)`` group."""
    return pattern_containing(GroupElement(children=_operand_children(operand)))


def capture(operand: BuilderProtocol) -> Pattern:
    """Return ``operand`` wrapped in a numbered capture ``(...)``."""
    return pattern_containing(CaptureElement(children=_operand_children(operand)))


def named_capture(name: str, operand: BuilderProtocol) -> Pattern:
    """Return ``operand`` wrapped in a named capture ``(?P<name>...)``."""
    return pattern_containing(NamedCaptureElement(name=name, children=_operand_children(operand)))


def back_reference(index: int) -> Pattern:
    """Return a numbered back-reference ``\\<index>``."""
    _ensure_positive_integer("index", index)
    return pattern_containing(BackReferenceElement(index=index))


def named_back_reference(name: str) -> Pattern:
    """Return a named back-reference ``(?P=name)``."""
    return pattern_containing(NamedBackReferenceElement(name=name))


def any_of(*operands: BuilderProtocol) -> Pattern:
    """Return an alternation ``(?:a|b|c)`` across the supplied operands."""
    if len(operands) < 2:
        raise MustBeAtLeastTwoOperandsError("any_of")
    child_elements = [target_element(operand) for operand in operands]
    children = tuple(child_elements)
    return pattern_containing(AnyOfElement(children=children))


def _operand_children(operand: BuilderProtocol) -> tuple[BaseElement, ...]:
    """Return ``operand``'s root-frame children as an immutable tuple."""
    return tuple(operand._state.top_frame.children)


def _ensure_positive_integer(label: str, value: int) -> None:
    """Raise :class:`MustBePositiveIntegerError` when ``value`` is not a strictly positive int."""
    if isinstance(value, int) and not isinstance(value, bool) and value > 0:
        return
    raise MustBePositiveIntegerError(label)
