"""The composition root for :class:`RegexBuilder` — the fluent regex-builder class.

The class itself defines no chain methods; every method comes from one of
the mixins under :mod:`edify.builder.mixins`. The composition order does
not matter for behavior because the mixins do not override each other's
methods, but they are listed alphabetically by mixin name for predictability.

The immutable-state plumbing (``_state`` attribute + ``_with_state`` helper)
lives on :class:`edify.builder.core.BuilderCore`, which every fluent surface
in the package inherits from.
"""

from __future__ import annotations

from edify.builder.core import BuilderCore
from edify.builder.mixins.anchors import AnchorsMixin
from edify.builder.mixins.assertions import AssertionsMixin
from edify.builder.mixins.captures import CapturesMixin
from edify.builder.mixins.chain import ChainMixin
from edify.builder.mixins.chars import CharsMixin
from edify.builder.mixins.classes import ClassesMixin
from edify.builder.mixins.flags import FlagsMixin
from edify.builder.mixins.groups import GroupsMixin
from edify.builder.mixins.matcher import MatcherMixin
from edify.builder.mixins.operators import OperatorsMixin
from edify.builder.mixins.quantifiers import QuantifiersMixin
from edify.builder.mixins.subexpression import SubexpressionMixin
from edify.builder.mixins.terminals import TerminalsMixin


class RegexBuilder(
    BuilderCore,
    AnchorsMixin,
    AssertionsMixin,
    CapturesMixin,
    ChainMixin,
    CharsMixin,
    ClassesMixin,
    FlagsMixin,
    GroupsMixin,
    MatcherMixin,
    OperatorsMixin,
    QuantifiersMixin,
    SubexpressionMixin,
    TerminalsMixin,
):
    """A fluent, immutable, strongly-typed regex builder."""
