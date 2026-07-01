"""The :class:`OperatorsMixin` — ``+`` concatenation and ``|`` alternation.

Both operators produce a new instance of the same concrete fluent surface
(a :class:`edify.builder.builder.RegexBuilder` or a
:class:`edify.pattern.composition.Pattern`), leaving both operands untouched
per the immutable-builder contract.

Semantically:

* ``a + b`` embeds ``b`` at the end of ``a`` — the algebra equivalent of
  ``a.subexpression(b)``.
* ``a | b`` produces a fresh instance whose sole element is an
  ``AnyOfElement`` containing ``a`` and ``b`` — the algebra equivalent of
  ``fresh.any_of().subexpression(a).subexpression(b).end()``.
"""

from __future__ import annotations

from typing import Self

from edify.builder.types.protocol import BuilderProtocol


class OperatorsMixin(BuilderProtocol):
    """Provides the ``+`` and ``|`` operator overloads on any fluent surface."""

    def __add__(self, other: BuilderProtocol) -> Self:
        """Return a new instance with ``other`` embedded at the end of ``self``.

        Anchors and flags from either operand are preserved so
        ``START + Pattern().digit() + END`` renders as ``^\\d$``.
        """
        return self.subexpression(other, ignore_flags=False, ignore_start_and_end=False)

    def __or__(self, other: BuilderProtocol) -> Self:
        """Return a new instance whose sole element is an alternation of ``self`` and ``other``.

        Anchors and flags from either operand are preserved so alternation
        arms carrying anchors keep them in the emitted regex.
        """
        concrete_class = type(self)
        fresh_instance = concrete_class()
        with_self = fresh_instance.any_of().subexpression(
            self, ignore_flags=False, ignore_start_and_end=False
        )
        with_other = with_self.subexpression(other, ignore_flags=False, ignore_start_and_end=False)
        return with_other.end()
