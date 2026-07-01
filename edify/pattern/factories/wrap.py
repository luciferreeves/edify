"""Internal helpers shared by every functional factory.

The factories in :mod:`edify.pattern.factories` all take one or more
:class:`Pattern` operands, extract their AST elements, wrap them into a
new element (a quantifier, a group, an assertion, an alternation, etc.),
and drop that wrapped element into a fresh :class:`Pattern`.

These helpers centralize:

* :func:`target_element` — turn an operand into a single element ready to
  wrap. Single-element operands unwrap to that element directly (so
  ``exactly(3, DIGIT)`` renders as ``\\d{3}`` not ``(?:\\d){3}``); multi-
  element operands bundle into a :class:`SubexpressionElement`.
* :func:`pattern_containing` — build a fresh :class:`Pattern` whose root
  frame carries the supplied element.
"""

from __future__ import annotations

from edify.builder.types.protocol import BuilderProtocol
from edify.elements.types.base import BaseElement
from edify.elements.types.groups import SubexpressionElement
from edify.pattern.composition import Pattern


def target_element(operand: BuilderProtocol) -> BaseElement:
    """Return the element to wrap: the sole child when there is one, else a bundle."""
    children = operand._state.top_frame.children
    if len(children) == 1:
        return children[0]
    return SubexpressionElement(children=children)


def pattern_containing(element: BaseElement) -> Pattern:
    """Return a fresh :class:`Pattern` whose root frame holds ``element``."""
    fresh_pattern = Pattern()
    new_state = fresh_pattern._state.with_element_added_to_top(element)
    return fresh_pattern._with_state(new_state)
