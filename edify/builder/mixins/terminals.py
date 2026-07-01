"""The :class:`TerminalsMixin` — the ``to_regex_string`` and ``to_regex`` terminals.

Both methods require the builder to be fully specified: every opened frame
must have been closed with ``.end()`` so only the root frame remains. The
string terminal returns exactly the pattern you'd hand to ``re.compile``;
the compiled terminal performs that compilation with the current flag set
and returns the emitted string wrapped in an :class:`edify.result.Regex`.
"""

from __future__ import annotations

import re

from edify.builder.types.flags import Flags
from edify.builder.types.protocol import BuilderProtocol
from edify.compile.dispatch import render_element
from edify.elements.types.root import RootElement
from edify.errors.internal import FailedToCompileRegexError
from edify.errors.quantifier import DanglingQuantifierError
from edify.errors.structure import CannotCallSubexpressionError
from edify.result import Regex

_EMPTY_NON_CAPTURING_GROUP = "(?:)"
_ESCAPED_SPACE = "\\ "
_RAW_SPACE = " "


class TerminalsMixin(BuilderProtocol):
    """Provides the two pattern-emitting terminal methods on the builder."""

    def to_regex_string(self) -> str:
        """Return the bare regex string the builder describes.

        The output is exactly what would be handed to :func:`re.compile` —
        no surrounding ``/.../`` delimiters and no embedded flag suffix.
        """
        _ensure_fully_specified(self)
        _ensure_no_dangling_quantifier(self)
        root_element = RootElement(children=self._state.top_frame.children)
        rendered_pattern = render_element(root_element)
        unescaped_pattern = rendered_pattern.replace(_ESCAPED_SPACE, _RAW_SPACE)
        if unescaped_pattern == "":
            return _EMPTY_NON_CAPTURING_GROUP
        return unescaped_pattern

    def to_regex(self) -> Regex:
        """Return the pattern + flags compiled and wrapped in :class:`edify.result.Regex`.

        The wrapper exposes the pattern string as ``.source`` and the underlying
        :class:`re.Pattern` as ``.compiled``, plus the eight :mod:`re` query
        methods as direct delegates.
        """
        pattern_string = self.to_regex_string()
        flag_bitmask = _build_flag_bitmask(self._state.flags)
        try:
            compiled_pattern = re.compile(pattern_string, flags=flag_bitmask)
        except re.error as compile_error:
            raise FailedToCompileRegexError(str(compile_error)) from compile_error
        return Regex(source=pattern_string, compiled=compiled_pattern)


def _ensure_fully_specified(builder: BuilderProtocol) -> None:
    """Raise :class:`CannotCallSubexpressionError` when frames beyond the root remain open."""
    if len(builder._state.stack) == 1:
        return
    top_frame_type_name = type(builder._state.top_frame.type_node).__name__
    raise CannotCallSubexpressionError(top_frame_type_name)


def _ensure_no_dangling_quantifier(builder: BuilderProtocol) -> None:
    """Raise :class:`DanglingQuantifierError` when any frame carries an unconsumed quantifier."""
    for frame in builder._state.stack:
        if frame.quantifier is not None:
            raise DanglingQuantifierError()


def _build_flag_bitmask(flags: Flags) -> int:
    """Combine the True-valued fields of ``flags`` into a single :mod:`re` bitmask."""
    bitmask = 0
    if flags.ascii_only:
        bitmask = bitmask | re.A
    if flags.debug:
        bitmask = bitmask | re.DEBUG
    if flags.ignore_case:
        bitmask = bitmask | re.I
    if flags.multiline:
        bitmask = bitmask | re.M
    if flags.dotall:
        bitmask = bitmask | re.S
    if flags.verbose:
        bitmask = bitmask | re.X
    return bitmask
