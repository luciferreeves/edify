"""Functional quantifier factories — the free-function counterpart to :class:`QuantifiersMixin`.

Each factory takes a single :class:`~edify.builder.types.protocol.BuilderProtocol` operand
and returns a fresh :class:`Pattern` whose sole element is the quantified form.

Single-element operands are wrapped directly so ``exactly(3, DIGIT)`` emits
``\\d{3}`` rather than ``(?:\\d){3}``; multi-element operands bundle into a
:class:`SubexpressionElement` which the compile path parenthesises as
needed.
"""

from __future__ import annotations

from edify.builder.types.protocol import BuilderProtocol
from edify.elements.types.quantifiers import (
    AtLeastElement,
    BetweenElement,
    BetweenLazyElement,
    ExactlyElement,
    OneOrMoreElement,
    OneOrMoreLazyElement,
    OptionalElement,
    ZeroOrMoreElement,
    ZeroOrMoreLazyElement,
)
from edify.errors.input import (
    MustBeIntegerGreaterThanZeroError,
    MustBeLessThanError,
    MustBePositiveIntegerError,
)
from edify.pattern.composition import Pattern
from edify.pattern.factories.wrap import pattern_containing, target_element


def optional(operand: BuilderProtocol) -> Pattern:
    """Return ``operand`` wrapped in a greedy ``?`` quantifier."""
    return pattern_containing(OptionalElement(child=target_element(operand)))


def zero_or_more(operand: BuilderProtocol) -> Pattern:
    """Return ``operand`` wrapped in a greedy ``*`` quantifier."""
    return pattern_containing(ZeroOrMoreElement(child=target_element(operand)))


def zero_or_more_lazy(operand: BuilderProtocol) -> Pattern:
    """Return ``operand`` wrapped in a lazy ``*?`` quantifier."""
    return pattern_containing(ZeroOrMoreLazyElement(child=target_element(operand)))


def one_or_more(operand: BuilderProtocol) -> Pattern:
    """Return ``operand`` wrapped in a greedy ``+`` quantifier."""
    return pattern_containing(OneOrMoreElement(child=target_element(operand)))


def one_or_more_lazy(operand: BuilderProtocol) -> Pattern:
    """Return ``operand`` wrapped in a lazy ``+?`` quantifier."""
    return pattern_containing(OneOrMoreLazyElement(child=target_element(operand)))


def exactly(count: int, operand: BuilderProtocol) -> Pattern:
    """Return ``operand`` wrapped in ``{count}``."""
    _ensure_positive_integer("count", count)
    return pattern_containing(ExactlyElement(times=count, child=target_element(operand)))


def at_least(count: int, operand: BuilderProtocol) -> Pattern:
    """Return ``operand`` wrapped in ``{count,}``."""
    _ensure_positive_integer("count", count)
    return pattern_containing(AtLeastElement(times=count, child=target_element(operand)))


def between(lower: int, upper: int, operand: BuilderProtocol) -> Pattern:
    """Return ``operand`` wrapped in a greedy ``{lower,upper}`` quantifier."""
    _ensure_non_negative_integer("x", lower)
    _ensure_positive_integer("y", upper)
    _ensure_strictly_ascending("X", "Y", lower, upper)
    return pattern_containing(
        BetweenElement(lower=lower, upper=upper, child=target_element(operand))
    )


def between_lazy(lower: int, upper: int, operand: BuilderProtocol) -> Pattern:
    """Return ``operand`` wrapped in a lazy ``{lower,upper}?`` quantifier."""
    _ensure_non_negative_integer("x", lower)
    _ensure_positive_integer("y", upper)
    _ensure_strictly_ascending("X", "Y", lower, upper)
    return pattern_containing(
        BetweenLazyElement(lower=lower, upper=upper, child=target_element(operand))
    )


def _ensure_positive_integer(label: str, value: int) -> None:
    """Raise :class:`MustBePositiveIntegerError` when ``value`` is not a strictly positive int."""
    if isinstance(value, int) and not isinstance(value, bool) and value > 0:
        return
    raise MustBePositiveIntegerError(label)


def _ensure_non_negative_integer(label: str, value: int) -> None:
    """Raise :class:`MustBeIntegerGreaterThanZeroError` when ``value`` is not a non-negative int."""
    if isinstance(value, int) and not isinstance(value, bool) and value >= 0:
        return
    raise MustBeIntegerGreaterThanZeroError(label)


def _ensure_strictly_ascending(lower_label: str, upper_label: str, lower: int, upper: int) -> None:
    """Raise :class:`MustBeLessThanError` when ``lower`` is not strictly less than ``upper``."""
    if lower < upper:
        return
    raise MustBeLessThanError(lower_label, upper_label)
