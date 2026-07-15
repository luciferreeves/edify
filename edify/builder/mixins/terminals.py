"""The :class:`TerminalsMixin` — the ``to_regex_string`` and ``to_regex`` terminals.

Both methods require the builder to be fully specified: every opened frame
must have been closed with ``.end()`` so only the root frame remains. The
string terminal returns exactly the pattern you'd hand to ``re.compile``;
the compiled terminal performs that compilation with the current flag set
via the selected engine backend, returning the emitted string wrapped in
an :class:`edify.result.Regex`.
"""

from __future__ import annotations

from edify.builder.types.engine import Engine
from edify.builder.types.flags import Flags
from edify.builder.types.protocol import BuilderProtocol
from edify.compile.backend import compile_pattern
from edify.compile.dispatch import render_element
from edify.elements.types.root import RootElement
from edify.errors.quantifier import DanglingQuantifierError
from edify.errors.structure import CannotCallSubexpressionError
from edify.result import Regex

_EMPTY_NON_CAPTURING_GROUP = "(?:)"
_ESCAPED_SPACE = "\\ "
_RAW_SPACE = " "


class TerminalsMixin(BuilderProtocol):
    """Provides the two pattern-emitting terminal methods on the builder."""

    _cached_regex: Regex | None

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

    def to_regex(
        self,
        *,
        ascii_only: bool = False,
        debug: bool = False,
        ignore_case: bool = False,
        multiline: bool = False,
        dotall: bool = False,
        verbose: bool = False,
        engine: Engine = "re",
    ) -> Regex:
        """Return the pattern + flags compiled and wrapped in :class:`edify.result.Regex`.

        The wrapper exposes the pattern string as ``.source`` and the underlying
        compiled pattern as ``.compiled``, plus the eight :mod:`re` query methods
        as direct delegates against the selected engine backend.

        Keyword arguments are OR-merged into the flag snapshot the builder
        already carries — passing ``ignore_case=True`` here is equivalent to
        having called ``.ignore_case()`` in the chain. Flags never turn off,
        only on.

        The ``engine`` kwarg selects the compilation backend. ``"re"`` (default)
        uses the stdlib :mod:`re` module. ``"regex"`` uses the third-party
        ``regex`` module, which unlocks constructs the stdlib does not accept
        (variable-width lookbehind, per-call timeouts). ``"regex"`` requires
        ``pip install edify[regex]``; a clean :class:`MissingRegexBackendError`
        surfaces when the extra is not installed.

        Default (no-kwargs) calls hit a per-instance lazy cache: the second and
        subsequent no-kwargs calls return the same :class:`Regex` the first call
        produced. Passing any kwarg bypasses the cache and always compiles fresh.
        """
        kwarg_flags = Flags(
            ascii_only=ascii_only,
            debug=debug,
            ignore_case=ignore_case,
            multiline=multiline,
            dotall=dotall,
            verbose=verbose,
        )
        can_cache = engine == "re" and kwarg_flags == Flags()
        if can_cache and self._cached_regex is not None:
            return self._cached_regex
        pattern_string = self.to_regex_string()
        effective_flags = self._state.flags.with_merged(kwarg_flags)
        compiled_pattern = compile_pattern(pattern_string, engine, effective_flags)
        wrapped = Regex(
            source=pattern_string,
            compiled=compiled_pattern,
            elements=tuple(self._state.top_frame.children),
            engine=engine,
        )
        if can_cache:
            self._cached_regex = wrapped
        return wrapped


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
