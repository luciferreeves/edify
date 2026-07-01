"""The composition root for :class:`Pattern` — a reusable regex fragment.

:class:`Pattern` shares every chain-method mixin with :class:`RegexBuilder`
except the terminals: a pattern is not intended to compile itself, it is
intended to compose *into* a builder (or into another pattern) via
``.use()`` or ``.subexpression()``. To emit a regex from a pattern, embed it
in a builder: ``RegexBuilder().use(my_pattern).to_regex()``.

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
from edify.builder.mixins.quantifiers import QuantifiersMixin
from edify.builder.mixins.subexpression import SubexpressionMixin


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
    QuantifiersMixin,
    SubexpressionMixin,
):
    """A named, reusable regex fragment. Composes into a builder via ``.use()``."""
