"""The composition root for :class:`Pattern` — a reusable regex fragment."""

from __future__ import annotations

import json

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
from edify.errors.serialize import NonObjectJSONPayloadError
from edify.serialize.dump import state_to_dict
from edify.serialize.load import dict_to_state
from edify.serialize.types import JSONValue


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
    TestingMixin,
):
    """A named, reusable regex fragment.

    Composes into a builder via ``.use()`` or emits its own regex via
    ``.to_regex_string()`` / ``.to_regex()``.
    """

    def __call__(self, value: str) -> bool:
        """Return True when ``value`` matches this pattern anywhere in it.

        Shortcut for :meth:`test` so a Pattern doubles as a validator callable
        (``email(value) -> bool``) without an intermediate ``.test`` step.
        """
        return self.test(value)

    def to_dict(self) -> dict[str, JSONValue]:
        """Return the canonical dict representation of this pattern."""
        return state_to_dict(self._state)

    def to_json(self) -> str:
        """Return the canonical JSON string for this pattern."""
        document = self.to_dict()
        return json.dumps(document, sort_keys=True, separators=(",", ":"))

    @classmethod
    def from_dict(cls, document: dict[str, JSONValue]) -> Pattern:
        """Return a Pattern reconstructed from a canonical dict."""
        reconstructed_state = dict_to_state(document)
        empty_pattern = cls()
        return empty_pattern._with_state(reconstructed_state)

    @classmethod
    def from_json(cls, blob: str) -> Pattern:
        """Return a Pattern reconstructed from a canonical JSON string."""
        parsed_document: JSONValue = json.loads(blob)
        if not isinstance(parsed_document, dict):
            raise NonObjectJSONPayloadError(type(parsed_document).__name__)
        return cls.from_dict(parsed_document)
