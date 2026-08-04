"""The :class:`MatcherMixin` — the closed set of five match verbs on any fluent surface.

Compiles ``self`` on first use via :meth:`edify.builder.core.BuilderCore.lazy_regex`
and reuses the cached :class:`edify.result.regex.Regex` on every subsequent call,
so ``pattern.test("a")`` followed by ``pattern.match("b")`` compiles the underlying
regex exactly once.

The surface is intentionally limited to ``test``, ``match``, ``search``, ``findall``,
``sub`` — the small verb set that keeps chain autocomplete uncluttered. Reach through
:meth:`to_regex` and use :class:`edify.result.regex.Regex` for ``fullmatch``,
``finditer``, ``subn``, or ``split``. Every match method also accepts a per-call
``timeout=`` kwarg that only applies under ``engine="regex"``.
"""

from __future__ import annotations

import sys
from collections.abc import Callable

from edify.builder.types.protocol import BuilderProtocol
from edify.result.match import Match


class MatcherMixin(BuilderProtocol):
    """Provides the five-verb match surface (``test``/``match``/``search``/``findall``/``sub``)."""

    def test(self, string: str, pos: int = 0, endpos: int = sys.maxsize) -> bool:
        """Return ``True`` when the pattern matches anywhere in ``string``, else ``False``.

        Uses search semantics: a match anywhere in ``string`` is enough. Anchor the
        pattern when the whole string must match.

        Args:
            string: The text to test.
            pos: Index to start searching from.
            endpos: Index to stop searching at.
        """
        return self.lazy_regex().search(string, pos, endpos) is not None

    def match(
        self,
        string: str,
        pos: int = 0,
        endpos: int = sys.maxsize,
        *,
        timeout: float | None = None,
    ) -> Match | None:
        """Delegate to :meth:`re.Pattern.match`, returning an edify :class:`Match`.

        The match must begin at ``pos`` but need not reach the end of ``string``.

        Args:
            string: The text to match against.
            pos: Index the match must start at.
            endpos: Index to stop matching at.
            timeout: Seconds to allow before abandoning the match; ``None`` waits
                indefinitely.

        Returns:
            A :class:`~edify.result.Match`, or ``None`` when the pattern does not match
            at ``pos``.
        """
        return self.lazy_regex().match(string, pos, endpos, timeout=timeout)

    def search(
        self,
        string: str,
        pos: int = 0,
        endpos: int = sys.maxsize,
        *,
        timeout: float | None = None,
    ) -> Match | None:
        """Delegate to :meth:`re.Pattern.search`, returning an edify :class:`Match`.

        Scans forward from ``pos`` until the pattern matches somewhere.

        Args:
            string: The text to search.
            pos: Index to start searching from.
            endpos: Index to stop searching at.
            timeout: Seconds to allow before abandoning the search; ``None`` waits
                indefinitely.

        Returns:
            The first :class:`~edify.result.Match`, or ``None`` when there is none.
        """
        return self.lazy_regex().search(string, pos, endpos, timeout=timeout)

    def findall(
        self,
        string: str,
        pos: int = 0,
        endpos: int = sys.maxsize,
        *,
        timeout: float | None = None,
    ) -> list[str] | list[tuple[str, ...]]:
        """Delegate to :meth:`re.Pattern.findall`.

        Args:
            string: The text to scan.
            pos: Index to start scanning from.
            endpos: Index to stop scanning at.
            timeout: Seconds to allow before abandoning the scan; ``None`` waits
                indefinitely.

        Returns:
            Every non-overlapping match. Each item is the matched text, or a tuple of
            the capture groups when the pattern has more than one.
        """
        return self.lazy_regex().findall(string, pos, endpos, timeout=timeout)

    def sub(
        self,
        replacement: str | Callable[[Match], str],
        string: str,
        count: int = 0,
        *,
        timeout: float | None = None,
    ) -> str:
        """Delegate to :meth:`re.Pattern.sub`; callables receive an edify :class:`Match`.

        Args:
            replacement: The text to substitute, which may reference captures as
                ``\\g<name>``; or a callable receiving each
                :class:`~edify.result.Match` and returning its replacement.
            string: The text to perform substitutions in.
            count: How many matches to replace; ``0`` replaces every one.
            timeout: Seconds to allow before abandoning the substitution; ``None`` waits
                indefinitely.

        Returns:
            ``string`` with each replaced match substituted.
        """
        return self.lazy_regex().sub(replacement, string, count=count, timeout=timeout)
