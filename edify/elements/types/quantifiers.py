"""Quantifier element classes — operators that repeat a single child element.

Each quantifier wraps exactly one child element and renders the appropriate
suffix at compile time (``?``, ``*``, ``+``, ``{n}``, ``{n,m}``, plus the
lazy variants).

Greedy quantifiers:

* :class:`OptionalElement` — ``?`` (zero or one).
* :class:`ZeroOrMoreElement` — ``*``.
* :class:`OneOrMoreElement` — ``+``.
* :class:`ExactlyElement` — ``{n}``.
* :class:`AtLeastElement` — ``{n,}``.
* :class:`AtMostElement` — ``{0,n}``.
* :class:`BetweenElement` — ``{lower,upper}``.

Lazy variants:

* :class:`ZeroOrMoreLazyElement` — ``*?``.
* :class:`OneOrMoreLazyElement` — ``+?``.
* :class:`BetweenLazyElement` — ``{lower,upper}?``.
"""

from __future__ import annotations

from dataclasses import dataclass

from edify.elements.types.base import BaseElement


@dataclass(frozen=True)
class OptionalElement(BaseElement):
    """Greedy ``?`` quantifier — zero or one match.

    Attributes:
        child: The element this quantifier applies to.
    """

    child: BaseElement


@dataclass(frozen=True)
class ZeroOrMoreElement(BaseElement):
    """Greedy ``*`` quantifier — zero or more matches.

    Attributes:
        child: The element this quantifier applies to.
    """

    child: BaseElement


@dataclass(frozen=True)
class ZeroOrMoreLazyElement(BaseElement):
    """Lazy ``*?`` quantifier — zero or more matches, prefer fewer.

    Attributes:
        child: The element this quantifier applies to.
    """

    child: BaseElement


@dataclass(frozen=True)
class OneOrMoreElement(BaseElement):
    """Greedy ``+`` quantifier — one or more matches.

    Attributes:
        child: The element this quantifier applies to.
    """

    child: BaseElement


@dataclass(frozen=True)
class OneOrMoreLazyElement(BaseElement):
    """Lazy ``+?`` quantifier — one or more matches, prefer fewer.

    Attributes:
        child: The element this quantifier applies to.
    """

    child: BaseElement


@dataclass(frozen=True)
class ExactlyElement(BaseElement):
    """``{times}`` quantifier — exactly ``times`` matches.

    Attributes:
        times: The exact number of repetitions required.
        child: The element this quantifier applies to.
    """

    times: int
    child: BaseElement


@dataclass(frozen=True)
class AtLeastElement(BaseElement):
    """``{times,}`` quantifier — at least ``times`` matches.

    Attributes:
        times: The minimum number of repetitions required.
        child: The element this quantifier applies to.
    """

    times: int
    child: BaseElement


@dataclass(frozen=True)
class AtMostElement(BaseElement):
    """``{0,times}`` quantifier — at most ``times`` matches.

    Attributes:
        times: The maximum number of repetitions allowed.
        child: The element this quantifier applies to.
    """

    times: int
    child: BaseElement


@dataclass(frozen=True)
class BetweenElement(BaseElement):
    """``{lower,upper}`` greedy quantifier — between ``lower`` and ``upper`` matches.

    Attributes:
        lower: The minimum number of repetitions required.
        upper: The maximum number of repetitions allowed.
        child: The element this quantifier applies to.
    """

    lower: int
    upper: int
    child: BaseElement


@dataclass(frozen=True)
class BetweenLazyElement(BaseElement):
    """``{lower,upper}?`` lazy quantifier — between ``lower`` and ``upper`` matches, prefer fewer.

    Attributes:
        lower: The minimum number of repetitions required.
        upper: The maximum number of repetitions allowed.
        child: The element this quantifier applies to.
    """

    lower: int
    upper: int
    child: BaseElement
