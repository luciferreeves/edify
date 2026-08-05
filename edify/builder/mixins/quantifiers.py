"""The :class:`QuantifiersMixin` — chain methods that set the pending quantifier."""

from __future__ import annotations

from typing import Self, TypeVar

from edify.builder.types.frame import PendingQuantifier
from edify.builder.types.protocol import BuilderProtocol
from edify.elements.types.base import BaseElement
from edify.elements.types.quantifiers import (
    AtLeastElement,
    AtLeastPossessiveElement,
    AtMostElement,
    AtMostPossessiveElement,
    BetweenElement,
    BetweenLazyElement,
    BetweenPossessiveElement,
    ExactlyElement,
    OneOrMoreElement,
    OneOrMoreLazyElement,
    OneOrMorePossessiveElement,
    OptionalElement,
    OptionalPossessiveElement,
    ZeroOrMoreElement,
    ZeroOrMoreLazyElement,
    ZeroOrMorePossessiveElement,
)
from edify.errors.context import CallerContext, capture_caller_context
from edify.errors.input import (
    MustBeIntegerGreaterThanZeroError,
    MustBeLessThanError,
    MustBePositiveIntegerError,
)
from edify.errors.quantifier import StackedQuantifierError

_TBuilder = TypeVar("_TBuilder", bound=BuilderProtocol)


class QuantifiersMixin(BuilderProtocol):
    """Provides the quantifier chain methods that set the pending quantifier."""

    def optional(self) -> Self:
        """Return a new builder with ``?`` queued as the pending quantifier."""
        call_site = capture_caller_context()
        return _set_pending(self, _optional_factory, call_site, "optional()")

    def zero_or_more(self) -> Self:
        """Return a new builder with ``*`` queued as the pending quantifier."""
        call_site = capture_caller_context()
        return _set_pending(self, _zero_or_more_factory, call_site, "zero_or_more()")

    def zero_or_more_lazy(self) -> Self:
        """Return a new builder with ``*?`` queued as the pending quantifier."""
        call_site = capture_caller_context()
        return _set_pending(self, _zero_or_more_lazy_factory, call_site, "zero_or_more_lazy()")

    def one_or_more(self) -> Self:
        """Return a new builder with ``+`` queued as the pending quantifier."""
        call_site = capture_caller_context()
        return _set_pending(self, _one_or_more_factory, call_site, "one_or_more()")

    def one_or_more_lazy(self) -> Self:
        """Return a new builder with ``+?`` queued as the pending quantifier."""
        call_site = capture_caller_context()
        return _set_pending(self, _one_or_more_lazy_factory, call_site, "one_or_more_lazy()")

    def exactly(self, count: int) -> Self:
        """Return a new builder with ``{count}`` queued as the pending quantifier.

        Args:
            count: How many repetitions the next element must have. Must be at least 1.

        Raises:
            MustBePositiveIntegerError: If ``count`` is not an int of 1 or more.
        """
        _ensure_positive_integer("count", count)
        call_site = capture_caller_context()
        return _set_pending(self, _exactly_factory(count), call_site, f"exactly({count})")

    def at_least(self, count: int) -> Self:
        """Return a new builder with ``{count,}`` queued as the pending quantifier.

        Args:
            count: The minimum number of repetitions; the maximum is unbounded. Must be
                at least 1.

        Raises:
            MustBePositiveIntegerError: If ``count`` is not an int of 1 or more.
        """
        _ensure_positive_integer("count", count)
        call_site = capture_caller_context()
        return _set_pending(self, _at_least_factory(count), call_site, f"at_least({count})")

    def at_most(self, count: int) -> Self:
        """Return a new builder with ``{0,count}`` queued as the pending quantifier.

        Args:
            count: The maximum number of repetitions; the minimum is zero. Must be at
                least 1.

        Raises:
            MustBePositiveIntegerError: If ``count`` is not an int of 1 or more.
        """
        _ensure_positive_integer("count", count)
        call_site = capture_caller_context()
        return _set_pending(self, _at_most_factory(count), call_site, f"at_most({count})")

    def between(self, lower: int, upper: int) -> Self:
        """Return a new builder with ``{lower,upper}`` queued as the pending quantifier.

        Args:
            lower: The minimum number of repetitions. Must be zero or more.
            upper: The maximum number of repetitions. Must be greater than ``lower``.

        Raises:
            MustBeIntegerGreaterThanZeroError: If ``lower`` is negative.
            MustBePositiveIntegerError: If ``upper`` is not an int of 1 or more.
            MustBeLessThanError: If ``lower`` is not strictly less than ``upper``.
        """
        _ensure_non_negative_integer("lower", lower)
        _ensure_positive_integer("upper", upper)
        _ensure_strictly_ascending("lower", "upper", lower, upper)
        call_site = capture_caller_context()
        return _set_pending(
            self, _between_factory(lower, upper), call_site, f"between({lower}, {upper})"
        )

    def optional_possessive(self) -> Self:
        """Return a new builder with ``?+`` queued as the pending quantifier."""
        call_site = capture_caller_context()
        return _set_pending(self, _optional_possessive_factory, call_site, "optional_possessive()")

    def zero_or_more_possessive(self) -> Self:
        """Return a new builder with ``*+`` queued as the pending quantifier."""
        call_site = capture_caller_context()
        return _set_pending(
            self, _zero_or_more_possessive_factory, call_site, "zero_or_more_possessive()"
        )

    def one_or_more_possessive(self) -> Self:
        """Return a new builder with ``++`` queued as the pending quantifier."""
        call_site = capture_caller_context()
        return _set_pending(
            self, _one_or_more_possessive_factory, call_site, "one_or_more_possessive()"
        )

    def at_least_possessive(self, count: int) -> Self:
        """Return a new builder with ``{count,}+`` queued as the pending quantifier.

        Args:
            count: The minimum number of repetitions; the maximum is unbounded. Must be
                at least 1.

        Raises:
            MustBePositiveIntegerError: If ``count`` is not an int of 1 or more.
        """
        _ensure_positive_integer("count", count)
        call_site = capture_caller_context()
        return _set_pending(
            self, _at_least_possessive_factory(count), call_site, f"at_least_possessive({count})"
        )

    def at_most_possessive(self, count: int) -> Self:
        """Return a new builder with ``{0,count}+`` queued as the pending quantifier.

        Args:
            count: The maximum number of repetitions; the minimum is zero. Must be at
                least 1.

        Raises:
            MustBePositiveIntegerError: If ``count`` is not an int of 1 or more.
        """
        _ensure_positive_integer("count", count)
        call_site = capture_caller_context()
        return _set_pending(
            self, _at_most_possessive_factory(count), call_site, f"at_most_possessive({count})"
        )

    def between_possessive(self, lower: int, upper: int) -> Self:
        """Return a new builder with ``{lower,upper}+`` queued as the pending quantifier.

        Args:
            lower: The minimum number of repetitions. Must be zero or more.
            upper: The maximum number of repetitions. Must be greater than ``lower``.

        Raises:
            MustBeIntegerGreaterThanZeroError: If ``lower`` is negative.
            MustBePositiveIntegerError: If ``upper`` is not an int of 1 or more.
            MustBeLessThanError: If ``lower`` is not strictly less than ``upper``.
        """
        _ensure_non_negative_integer("lower", lower)
        _ensure_positive_integer("upper", upper)
        _ensure_strictly_ascending("lower", "upper", lower, upper)
        call_site = capture_caller_context()
        return _set_pending(
            self,
            _between_possessive_factory(lower, upper),
            call_site,
            f"between_possessive({lower}, {upper})",
        )

    def between_lazy(self, lower: int, upper: int) -> Self:
        """Return a new builder with ``{lower,upper}?`` queued as the pending quantifier.

        Args:
            lower: The minimum number of repetitions. Must be zero or more.
            upper: The maximum number of repetitions. Must be greater than ``lower``.

        Raises:
            MustBeIntegerGreaterThanZeroError: If ``lower`` is negative.
            MustBePositiveIntegerError: If ``upper`` is not an int of 1 or more.
            MustBeLessThanError: If ``lower`` is not strictly less than ``upper``.
        """
        _ensure_non_negative_integer("lower", lower)
        _ensure_positive_integer("upper", upper)
        _ensure_strictly_ascending("lower", "upper", lower, upper)
        call_site = capture_caller_context()
        return _set_pending(
            self,
            _between_lazy_factory(lower, upper),
            call_site,
            f"between_lazy({lower}, {upper})",
        )


def _set_pending(
    builder: _TBuilder,
    pending_quantifier: PendingQuantifier,
    call_site: CallerContext | None,
    quantifier_name: str,
) -> _TBuilder:
    """Replace the top frame with one carrying the given pending quantifier."""
    if builder.state.top_frame.quantifier is not None:
        raise StackedQuantifierError()
    new_top_frame = builder.state.top_frame.with_quantifier(
        pending_quantifier, call_site, quantifier_name
    )
    new_state = builder.state.with_top_frame_replaced(new_top_frame)
    return builder.with_state(new_state)


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
    if not isinstance(value, bool) and value > 0:
        return
    raise MustBePositiveIntegerError(label)


def _ensure_non_negative_integer(label: str, value: int) -> None:
    """Raise :class:`MustBeIntegerGreaterThanZeroError` when ``value`` is not a non-negative int."""
    if not isinstance(value, bool) and value >= 0:
        return
    raise MustBeIntegerGreaterThanZeroError(label)


def _ensure_strictly_ascending(lower_label: str, upper_label: str, lower: int, upper: int) -> None:
    """Raise :class:`MustBeLessThanError` when ``lower`` is not strictly less than ``upper``."""
    if lower < upper:
        return
    raise MustBeLessThanError(lower_label, upper_label)


def _optional_possessive_factory(child: BaseElement) -> OptionalPossessiveElement:
    return OptionalPossessiveElement(child=child)


def _zero_or_more_possessive_factory(child: BaseElement) -> ZeroOrMorePossessiveElement:
    return ZeroOrMorePossessiveElement(child=child)


def _one_or_more_possessive_factory(child: BaseElement) -> OneOrMorePossessiveElement:
    return OneOrMorePossessiveElement(child=child)


def _at_least_possessive_factory(count: int) -> PendingQuantifier:
    def factory(child: BaseElement) -> AtLeastPossessiveElement:
        return AtLeastPossessiveElement(times=count, child=child)

    return factory


def _at_most_possessive_factory(count: int) -> PendingQuantifier:
    def factory(child: BaseElement) -> AtMostPossessiveElement:
        return AtMostPossessiveElement(times=count, child=child)

    return factory


def _between_possessive_factory(lower: int, upper: int) -> PendingQuantifier:
    def factory(child: BaseElement) -> BetweenPossessiveElement:
        return BetweenPossessiveElement(lower=lower, upper=upper, child=child)

    return factory
