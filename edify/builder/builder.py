"""The composition root for :class:`RegexBuilder` — the fluent regex-builder class."""

from __future__ import annotations

import edify.builder.reverse as reverse_module
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
from edify.builder.mixins.testing import TestingMixin


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
    TestingMixin,
):
    """A fluent, immutable, strongly-typed regex builder.

    Immutability is a hard contract: every chain method returns a *new* builder
    and leaves the receiver untouched. A base builder held in a constant, closure,
    or attribute can be extended along multiple independent paths without any of
    them observing another's state. Repeat no-kwargs ``.to_regex()`` calls on the
    same builder return the same cached :class:`Regex`; a chain step or ``fork()``
    yields a fresh builder with its own empty cache.
    """

    @classmethod
    def from_regex(cls, pattern_text: str) -> RegexBuilder:
        """Return a builder chain whose emitted pattern is equivalent to ``pattern_text``.

        Args:
            pattern_text: Raw regex source, exactly what would be handed to :func:`re.compile`.

        Raises:
            edify.builder.reverse.UnsupportedReverseParseError: when the source uses a
                construct the reverse parser cannot translate yet.
        """
        return reverse_module.build_from_regex(pattern_text)
