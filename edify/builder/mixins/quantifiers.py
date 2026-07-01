"""The :class:`QuantifiersMixin` — chain methods that set the pending quantifier.

A quantifier method does NOT consume the previous element — it stores a
deferred factory on the top frame. The next call that appends an element
sees the pending quantifier and wraps the element with it before storing
the result.
"""

from __future__ import annotations

from typing import Self

from edify.builder.types.frame import PendingQuantifier
from edify.builder.types.protocol import BuilderProtocol
from edify.elements.types.base import BaseElement
from edify.elements.types.quantifiers import (
    AtLeastElement,
    AtMostElement,
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


class QuantifiersMixin(BuilderProtocol):
    """Provides the nine quantifier chain methods that set the pending quantifier."""

    def optional(self) -> Self:
        """Return a new builder with ``?`` queued as the pending quantifier."""
        return _set_pending(self, _optional_factory)

    def zero_or_more(self) -> Self:
        """Return a new builder with ``*`` queued as the pending quantifier."""
        return _set_pending(self, _zero_or_more_factory)

    def zero_or_more_lazy(self) -> Self:
        """Return a new builder with ``*?`` queued as the pending quantifier."""
        return _set_pending(self, _zero_or_more_lazy_factory)

    def one_or_more(self) -> Self:
        """Return a new builder with ``+`` queued as the pending quantifier."""
        return _set_pending(self, _one_or_more_factory)

    def one_or_more_lazy(self) -> Self:
        """Return a new builder with ``+?`` queued as the pending quantifier."""
        return _set_pending(self, _one_or_more_lazy_factory)

    def exactly(self, count: int) -> Self:
        """Return a new builder with ``{count}`` queued as the pending quantifier."""
        _ensure_positive_integer("count", count)
        return _set_pending(self, _exactly_factory(count))

    def at_least(self, count: int) -> Self:
        """Return a new builder with ``{count,}`` queued as the pending quantifier."""
        _ensure_positive_integer("count", count)
        return _set_pending(self, _at_least_factory(count))

    def at_most(self, count: int) -> Self:
        """Return a new builder with ``{0,count}`` queued as the pending quantifier."""
        _ensure_positive_integer("count", count)
        return _set_pending(self, _at_most_factory(count))

    def between(self, lower: int, upper: int) -> Self:
        """Return a new builder with ``{lower,upper}`` queued as the pending quantifier."""
        _ensure_non_negative_integer("x", lower)
        _ensure_positive_integer("y", upper)
        _ensure_strictly_ascending("X", "Y", lower, upper)
        return _set_pending(self, _between_factory(lower, upper))

    def between_lazy(self, lower: int, upper: int) -> Self:
        """Return a new builder with ``{lower,upper}?`` queued as the pending quantifier."""
        _ensure_non_negative_integer("x", lower)
        _ensure_positive_integer("y", upper)
        _ensure_strictly_ascending("X", "Y", lower, upper)
        return _set_pending(self, _between_lazy_factory(lower, upper))


def _set_pending(builder: BuilderProtocol, pending_quantifier: PendingQuantifier):
    """Replace the top frame with one carrying the given pending quantifier."""
    new_top_frame = builder._state.top_frame.with_quantifier(pending_quantifier)
    new_state = builder._state.with_top_frame_replaced(new_top_frame)
    return builder._with_state(new_state)


def _optional_factory(child: BaseElement) -> OptionalElement:
    return OptionalElement(child=child)


def _zero_or_more_factory(child: BaseElement) -> ZeroOrMoreElement:
    return ZeroOrMoreElement(child=child)


def _zero_or_more_lazy_factory(child: BaseElement) -> ZeroOrMoreLazyElement:
    return ZeroOrMoreLazyElement(child=child)


def _one_or_more_factory(child: BaseElement) -> OneOrMoreElement:
    return OneOrMoreElement(child=child)


def _one_or_more_lazy_factory(child: BaseElement) -> OneOrMoreLazyElement:
    return OneOrMoreLazyElement(child=child)


def _exactly_factory(count: int) -> PendingQuantifier:
    def factory(child: BaseElement) -> ExactlyElement:
        return ExactlyElement(times=count, child=child)

    return factory


def _at_least_factory(count: int) -> PendingQuantifier:
    def factory(child: BaseElement) -> AtLeastElement:
        return AtLeastElement(times=count, child=child)

    return factory


def _at_most_factory(count: int) -> PendingQuantifier:
    def factory(child: BaseElement) -> AtMostElement:
        return AtMostElement(times=count, child=child)

    return factory


def _between_factory(lower: int, upper: int) -> PendingQuantifier:
    def factory(child: BaseElement) -> BetweenElement:
        return BetweenElement(lower=lower, upper=upper, child=child)

    return factory


def _between_lazy_factory(lower: int, upper: int) -> PendingQuantifier:
    def factory(child: BaseElement) -> BetweenLazyElement:
        return BetweenLazyElement(lower=lower, upper=upper, child=child)

    return factory


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
