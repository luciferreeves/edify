"""The composition root for :class:`Pattern` — a reusable regex fragment.

:class:`Pattern` shares every chain-method mixin with :class:`RegexBuilder`,
including the terminals so a pattern can emit its own regex directly via
``pattern.to_regex_string()`` or ``pattern.to_regex()``. A pattern still
composes *into* a builder (or into another pattern) via ``.use()`` or
``.subexpression()`` when the caller wants control over how anchors, flags
and namespaces merge into the outer surface.

The immutable-state plumbing (``_state`` attribute + ``_with_state`` helper)
comes from :class:`edify.builder.core.BuilderCore`, the same base
:class:`edify.builder.builder.RegexBuilder` inherits from.
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


class Pattern(
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
    """A named, reusable regex fragment.

    Composes into a builder via ``.use()`` or emits its own regex via
    ``.to_regex_string()`` / ``.to_regex()``.
    """
