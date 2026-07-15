"""The :class:`TestingMixin` — first-class ``assert_matches`` / ``assert_rejects`` helpers.

Both methods accept an iterable of strings and raise if any input fails the
declared expectation. The raised assertion class inherits :class:`AssertionError`
so pytest introspects it exactly like a bare ``assert``.
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import Self

from edify.builder.types.protocol import BuilderProtocol
from edify.errors.testing import (
    PatternDidNotMatchInputsError,
    PatternMatchedRejectedInputsError,
)


class TestingMixin(BuilderProtocol):
    """Provides ``assert_matches`` and ``assert_rejects`` on any fluent surface."""

    def assert_matches(self, inputs: Iterable[str]) -> Self:
        """Assert every string in ``inputs`` matches this pattern; return ``self``."""
        compiled = self._lazy_regex()
        input_tuple = tuple(inputs)
        missing = tuple(item for item in input_tuple if compiled.search(item) is None)
        if missing:
            raise PatternDidNotMatchInputsError(compiled.source, missing)
        return self

    def assert_rejects(self, inputs: Iterable[str]) -> Self:
        """Assert every string in ``inputs`` is rejected by this pattern; return ``self``."""
        compiled = self._lazy_regex()
        input_tuple = tuple(inputs)
        matched = tuple(item for item in input_tuple if compiled.search(item) is not None)
        if matched:
            raise PatternMatchedRejectedInputsError(compiled.source, matched)
        return self
