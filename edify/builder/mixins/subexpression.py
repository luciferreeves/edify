"""The :class:`SubexpressionMixin` — merge another builder as a quantifiable atom.

Provides both :meth:`SubexpressionMixin.subexpression` (the primitive with
full option surface) and :meth:`SubexpressionMixin.use` (the ergonomic
alias that composes a :class:`edify.pattern.Pattern` or another builder
with the common-case defaults).

Both entry points validate the incoming expression, transform its elements
through the namespace / capture-offset / anchor logic in
:mod:`edify.builder.merge`, wrap the merged children in a
:class:`SubexpressionElement`, and append that to the current frame
(applying any pending quantifier).
"""

from __future__ import annotations

from typing import Self

from edify.builder.diagnose import describe_open_frames
from edify.builder.merge import MergeContext, merge_element
from edify.builder.types.protocol import BuilderProtocol
from edify.elements.types.base import BaseElement
from edify.elements.types.groups import SubexpressionElement
from edify.errors.structure import CannotCallSubexpressionError


class SubexpressionMixin(BuilderProtocol):
    """Provides the ``.subexpression`` and ``.use`` chain methods."""

    def use(self, pattern: BuilderProtocol) -> Self:
        """Return a new builder with ``pattern`` embedded via subexpression semantics.

        Ergonomic alias for ``self.subexpression(pattern)`` using the
        common-case defaults (``ignore_flags=True``, ``ignore_start_and_end=True``,
        no namespace). Use :meth:`subexpression` directly when you need to
        override any of those.

        Args:
            pattern: A :class:`edify.pattern.Pattern` — or any fully-specified
                fluent surface conforming to :class:`BuilderProtocol` — to
                embed at the current position.
        """
        return self.subexpression(pattern)

    def subexpression(
        self,
        expression: BuilderProtocol,
        namespace: str = "",
        ignore_flags: bool = True,
        ignore_start_and_end: bool = True,
    ) -> Self:
        """Return a new builder with ``expression`` merged in as a quantifiable atom.

        Args:
            expression: A fully-specified builder produced elsewhere (only the
                root frame open, no in-progress nested constructs).
            namespace: Prefix prepended to every named-capture and named-back-
                reference name from ``expression``.
            ignore_flags: When True (default), the expression's flag snapshot
                is dropped. When False, the parent's flags become the logical
                OR of both.
            ignore_start_and_end: When True (default), ``start_of_input`` and
                ``end_of_input`` markers inside ``expression`` collapse to
                no-ops; when False, they merge into the parent (and raise if
                the parent already declared the same anchor).
        """
        _ensure_fully_specified(expression)
        merged_root_children, captures_added = _merge_expression_children(
            expression, self, namespace, ignore_start_and_end
        )
        subexpression_element = SubexpressionElement(children=merged_root_children)
        state_with_element = self.state.with_element_added_to_top(subexpression_element)
        state_with_counts = state_with_element.with_capture_groups_added(captures_added)
        if ignore_flags:
            return self.with_state(state_with_counts)
        merged_flags = self.state.flags.with_merged(expression.state.flags)
        state_with_flags = state_with_counts.with_flags(merged_flags)
        return self.with_state(state_with_flags)


def _ensure_fully_specified(expression: BuilderProtocol) -> None:
    """Raise when ``expression`` still has nested frames open beyond the root."""
    if len(expression.state.stack) == 1:
        return
    open_frames = describe_open_frames(expression.state)
    raise CannotCallSubexpressionError(open_frames)


def _merge_expression_children(
    expression: BuilderProtocol,
    parent: BuilderProtocol,
    namespace: str,
    ignore_start_and_end: bool,
) -> tuple[tuple[BaseElement, ...], int]:
    """Run every root child of ``expression`` through the merge transform."""
    context = MergeContext(
        capture_index_offset=parent.state.total_capture_groups,
        namespace=namespace,
        ignore_start_and_end=ignore_start_and_end,
        parent_has_start=parent.state.has_defined_start,
        parent_has_end=parent.state.has_defined_end,
    )
    expression_root_children = expression.state.top_frame.children
    merged_list: list[BaseElement] = []
    total_added = 0
    for child in expression_root_children:
        result = merge_element(child, context)
        merged_list.append(result.element)
        total_added += result.captures_added
    return tuple(merged_list), total_added
