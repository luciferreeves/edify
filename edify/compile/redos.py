"""Build-time ReDoS detection over the element tree.

Walks a Pattern's element tree and emits :class:`ReDoSWarning` when it
finds constructs known to cause catastrophic backtracking. This is a
uniquely-structural check — impossible to do reliably against a raw
regex string — and it's the reason edify carries an AST at all: the
warning fires when :meth:`to_regex` is called, so the caller sees the
diagnosis before the pattern ever runs against user input.

The check is intentionally conservative: it flags only the classical
``(x+)+`` shape — an unbounded quantifier wrapping a single-child group
whose one child is itself an unbounded quantifier. That shape is the
one that turns linear input into exponential match time and is almost
never intentional. False positives on legitimate composite patterns
(``[^()]*(?:\\([^()]*\\)[^()]*)*``) are avoided by requiring the
group's children tuple to have length one.
"""

from __future__ import annotations

import warnings
from collections.abc import Iterable

from edify.elements.types.base import BaseElement
from edify.elements.types.groups import GroupElement
from edify.elements.types.quantifiers import (
    AtLeastElement,
    OneOrMoreElement,
    OneOrMoreLazyElement,
    ZeroOrMoreElement,
    ZeroOrMoreLazyElement,
)
from edify.elements.walk import walk_elements

UnboundedQuantifierElement = (
    OneOrMoreElement
    | OneOrMoreLazyElement
    | ZeroOrMoreElement
    | ZeroOrMoreLazyElement
    | AtLeastElement
)


class ReDoSWarning(UserWarning):
    """Warning raised when the compile path detects a catastrophic-backtracking construct."""


def warn_on_redos_constructs(roots: Iterable[BaseElement]) -> None:
    """Emit :class:`ReDoSWarning` once per detected ``(x+)+`` shape in ``roots``."""
    for element in walk_elements(roots):
        if not isinstance(element, UnboundedQuantifierElement):
            continue
        inner_quantifier = _extract_nested_bare_unbounded_quantifier(element)
        if inner_quantifier is None:
            continue
        message = (
            f"nested unbounded quantifier detected: "
            f"{_display_name_for(element)} wraps a single-child group whose only "
            f"child is {_display_name_for(inner_quantifier)} — this shape is "
            "vulnerable to catastrophic backtracking (ReDoS). Consider using a "
            "possessive quantifier or an atomic group; under engine='regex' the "
            "(?>...) atomic group is available."
        )
        warnings.warn(message, ReDoSWarning, stacklevel=3)


def _extract_nested_bare_unbounded_quantifier(
    outer: UnboundedQuantifierElement,
) -> UnboundedQuantifierElement | None:
    outer_child = outer.child
    if not isinstance(outer_child, GroupElement):
        return None
    group_children = outer_child.children
    if len(group_children) != 1:
        return None
    only_child = group_children[0]
    if not isinstance(only_child, UnboundedQuantifierElement):
        return None
    return only_child


def _display_name_for(element: UnboundedQuantifierElement) -> str:
    if isinstance(element, OneOrMoreElement):
        return "one_or_more()"
    if isinstance(element, OneOrMoreLazyElement):
        return "one_or_more_lazy()"
    if isinstance(element, ZeroOrMoreElement):
        return "zero_or_more()"
    if isinstance(element, ZeroOrMoreLazyElement):
        return "zero_or_more_lazy()"
    return f"at_least({element.times})"
