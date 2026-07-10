"""Grouping element classes — non-capturing groups, alternation, lookarounds, subexpressions.

These elements collect ordered child elements and emit a parenthesised
construct that does not introduce a numbered capture:

* :class:`GroupElement` — ``(?:...)`` non-capturing group.
* :class:`AnyOfElement` — ``(?:a|b|c)`` (or ``[abc]`` when all members fuse) alternation.
* :class:`SubexpressionElement` — a merged-in pattern fragment treated as a single
  unit for quantification purposes.
* :class:`AssertAheadElement` — ``(?=...)`` positive lookahead.
* :class:`AssertNotAheadElement` — ``(?!...)`` negative lookahead.
* :class:`AssertBehindElement` — ``(?<=...)`` positive lookbehind.
* :class:`AssertNotBehindElement` — ``(?<!...)`` negative lookbehind.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from edify.elements.types.base import BaseElement


@dataclass(frozen=True)
class GroupElement(BaseElement):
    """A non-capturing ``(?:...)`` group.

    Attributes:
        children: The elements rendered inside the parentheses, in order.
    """

    children: tuple[BaseElement, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class AnyOfElement(BaseElement):
    """An alternation rendered as ``(?:a|b|c)`` (or ``[abc]`` when fully fusable).

    Attributes:
        children: The alternative elements, in order.
    """

    children: tuple[BaseElement, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class SubexpressionElement(BaseElement):
    """A merged-in pattern fragment treated as a quantifiable atom.

    Attributes:
        children: The elements from the merged pattern, after namespace and
            anchor adjustments have been applied.
    """

    children: tuple[BaseElement, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class AssertAheadElement(BaseElement):
    """A positive lookahead ``(?=...)``.

    Attributes:
        children: The elements that must match immediately after the current position.
    """

    children: tuple[BaseElement, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class AssertNotAheadElement(BaseElement):
    """A negative lookahead ``(?!...)``.

    Attributes:
        children: The elements that must NOT match immediately after the current position.
    """

    children: tuple[BaseElement, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class AssertBehindElement(BaseElement):
    """A positive lookbehind ``(?<=...)``.

    Attributes:
        children: The elements that must have matched immediately before the current position.
    """

    children: tuple[BaseElement, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class AssertNotBehindElement(BaseElement):
    """A negative lookbehind ``(?<!...)``.

    Attributes:
        children: The elements that must NOT have matched immediately before the current position.
    """

    children: tuple[BaseElement, ...] = field(default_factory=tuple)
