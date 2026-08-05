"""Functional grouping factories — non-capturing groups, captures, alternation, back-references.

Each factory returns a fresh :class:`Pattern` whose root frame holds a
single grouping element built from the supplied operand(s).

* :func:`group` — wrap into a non-capturing ``(?:...)``.
* :func:`capture` — wrap into a numbered capture ``(...)``.
* :func:`named_capture` — wrap into ``(?P<name>...)``.
* :func:`back_reference` — emit ``\\<index>``.
* :func:`named_back_reference` — emit ``(?P=name)``.
* :func:`any_of` — emit ``(?:a|b|c)`` alternation across the operands.
* :func:`anything_but_any_of` — emit ``[^abc]`` rejecting the operands.
* :func:`atomic` — wrap into an atomic ``(?>...)`` group.
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
from edify.elements.types.groups import (
    AnyOfElement,
    AnythingButAnyOfElement,
    AtomicElement,
    GroupElement,
)
from edify.errors.input import (
    MustBeAtLeastOneOperandError,
    MustBeAtLeastTwoOperandsError,
    MustBePositiveIntegerError,
)
from edify.pattern.composition import Pattern
from edify.pattern.factories.wrap import pattern_containing, target_element


def group(operand: BuilderProtocol) -> Pattern:
    """Return ``operand`` wrapped in a non-capturing ``(?:...)`` group.

    Args:
        operand: The pattern to bundle into one unit.
    """
    return pattern_containing(GroupElement(children=_operand_children(operand)))


def capture(operand: BuilderProtocol) -> Pattern:
    """Return ``operand`` wrapped in a numbered capture ``(...)``.

    Args:
        operand: The pattern whose matched text is kept.
    """
    return pattern_containing(CaptureElement(children=_operand_children(operand)))


def named_capture(name: str, operand: BuilderProtocol) -> Pattern:
    """Return ``operand`` wrapped in a named capture ``(?P<name>...)``.

    Args:
        name: The group's name. Must be a valid Python identifier.
        operand: The pattern whose matched text is kept under ``name``.
    """
    return pattern_containing(NamedCaptureElement(name=name, children=_operand_children(operand)))


def back_reference(index: int) -> Pattern:
    """Return a numbered back-reference ``\\<index>``.

    Args:
        index: The 1-based number of the capture to rematch.

    Raises:
        MustBePositiveIntegerError: If ``index`` is not an int of 1 or more.
    """
    _ensure_positive_integer("index", index)
    return pattern_containing(BackReferenceElement(index=index))


def named_back_reference(name: str) -> Pattern:
    """Return a named back-reference ``(?P=name)``.

    Args:
        name: The name of the capture to rematch.
    """
    return pattern_containing(NamedBackReferenceElement(name=name))


def any_of(*operands: BuilderProtocol) -> Pattern:
    """Return an alternation ``(?:a|b|c)`` across the supplied operands.

    Branches are tried left to right and the first to match wins.

    Args:
        *operands: The alternatives. At least two are required.

    Raises:
        MustBeAtLeastTwoOperandsError: If fewer than two operands are given.
    """
    if len(operands) < 2:
        raise MustBeAtLeastTwoOperandsError("any_of")
    child_elements = [target_element(operand) for operand in operands]
    children = tuple(child_elements)
    return pattern_containing(AnyOfElement(children=children))


def atomic(operand: BuilderProtocol) -> Pattern:
    """Return ``operand`` wrapped in an atomic group ``(?>...)``.

    Args:
        operand: The pattern to bundle into one non-backtracking unit.
    """
    return pattern_containing(AtomicElement(children=_operand_children(operand)))


def anything_but_any_of(*operands: BuilderProtocol) -> Pattern:
    """Return a negated character class ``[^abc]`` rejecting the supplied operands.

    Args:
        *operands: The rejected members. At least one is required, and each must
            be a single character, a character set, or a character range.

    Raises:
        MustBeAtLeastOneOperandError: If no operands are given.
        CannotNegateNonCharacterMemberError: At compile time, if an operand is
            wider than a single character.
    """
    if not operands:
        raise MustBeAtLeastOneOperandError("anything_but_any_of")
    child_elements = [target_element(operand) for operand in operands]
    children = tuple(child_elements)
    return pattern_containing(AnythingButAnyOfElement(children=children))


def _operand_children(operand: BuilderProtocol) -> tuple[BaseElement, ...]:
    """Return ``operand``'s root-frame children as an immutable tuple."""
    return tuple(operand.state.top_frame.children)


def _ensure_positive_integer(label: str, value: int) -> None:
    """Raise :class:`MustBePositiveIntegerError` when ``value`` is not a strictly positive int."""
    if not isinstance(value, bool) and value > 0:
        return
    raise MustBePositiveIntegerError(label)
