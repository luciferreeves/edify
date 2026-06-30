"""Render the suffix of a quantifier element.

A quantifier element (``*``, ``+``, ``?``, ``{n}``, ``{n,m}``, plus the
lazy variants) compiles to a suffix string that follows the already-rendered
child fragment. This module owns that suffix translation and nothing else;
the surrounding grouping logic (whether to wrap the child in ``(?:...)``)
is the apply step's responsibility.
"""

from __future__ import annotations

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
from edify.elements.types.union import QuantifierElement


def quantifier_suffix(quantifier: QuantifierElement) -> str:
    """Return the regex suffix string for the given quantifier element.

    Args:
        quantifier: One of the nine quantifier element classes.

    Returns:
        The exact suffix string, e.g. ``"?"``, ``"+?"``, ``"{3}"``, ``"{1,4}?"``.
    """
    match quantifier:
        case OptionalElement():
            return "?"
        case ZeroOrMoreElement():
            return "*"
        case ZeroOrMoreLazyElement():
            return "*?"
        case OneOrMoreElement():
            return "+"
        case OneOrMoreLazyElement():
            return "+?"
        case ExactlyElement(times=exact_count):
            return f"{{{exact_count}}}"
        case AtLeastElement(times=minimum_count):
            return f"{{{minimum_count},}}"
        case BetweenElement(lower=lower_bound, upper=upper_bound):
            return f"{{{lower_bound},{upper_bound}}}"
        case BetweenLazyElement(lower=lower_bound, upper=upper_bound):
            return f"{{{lower_bound},{upper_bound}}}?"
