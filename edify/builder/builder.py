"""The composition root for :class:`RegexBuilder` — the fluent regex-builder class.

The class itself defines no chain methods; every method comes from one of
the mixins under :mod:`edify.builder.mixins`. The composition order does
not matter for behavior because the mixins do not override each other's
methods, but they are listed alphabetically by mixin name for predictability.

The two attributes required by :class:`BuilderProtocol` —
``_state: BuilderState`` and ``_with_state``  — live here. Every chain
method reads ``self._state`` and returns ``self._with_state(new_state)``.
"""

from __future__ import annotations

from typing import Self

from edify.builder.mixins.anchors import AnchorsMixin
from edify.builder.mixins.assertions import AssertionsMixin
from edify.builder.mixins.captures import CapturesMixin
from edify.builder.mixins.chain import ChainMixin
from edify.builder.mixins.chars import CharsMixin
from edify.builder.mixins.classes import ClassesMixin
from edify.builder.mixins.flags import FlagsMixin
from edify.builder.mixins.groups import GroupsMixin
from edify.builder.mixins.quantifiers import QuantifiersMixin
from edify.builder.mixins.subexpression import SubexpressionMixin
from edify.builder.mixins.terminals import TerminalsMixin
from edify.builder.types.state import BuilderState


class RegexBuilder(
    AnchorsMixin,
    AssertionsMixin,
    CapturesMixin,
    ChainMixin,
    CharsMixin,
    ClassesMixin,
    FlagsMixin,
    GroupsMixin,
    QuantifiersMixin,
    SubexpressionMixin,
    TerminalsMixin,
):
    """A fluent, immutable, strongly-typed regex builder."""

    _state: BuilderState

    def __init__(self) -> None:
        self._state = BuilderState()

    def _with_state(self, new_state: BuilderState) -> Self:
        """Return a fresh builder of the same concrete type carrying ``new_state``."""
        builder_class = type(self)
        new_instance = builder_class.__new__(builder_class)
        new_instance._state = new_state
        return new_instance
