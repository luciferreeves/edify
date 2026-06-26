"""The :class:`Flags` dataclass — the six pattern-global regex flags.

Each flag corresponds to one of Python's ``re`` flag constants. The builder
toggles them one at a time as the user calls ``.ignore_case()`` etc., and
the terminal step (``to_regex``) translates the True-valued fields into the
combined ``re`` flag bitmask at compile time.
"""

from __future__ import annotations

from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Flags:
    """Snapshot of the six pattern-global regex flags.

    Attributes:
        ascii_only: Maps to ``re.A`` — match ASCII-only character classes.
        debug: Maps to ``re.DEBUG`` — print debug information at compile time.
        ignore_case: Maps to ``re.I`` — case-insensitive matching.
        multiline: Maps to ``re.M`` — ``^``/``$`` match at line boundaries.
        dotall: Maps to ``re.S`` — ``.`` matches newlines too.
        verbose: Maps to ``re.X`` — allow whitespace and comments in patterns.
    """

    ascii_only: bool = False
    debug: bool = False
    ignore_case: bool = False
    multiline: bool = False
    dotall: bool = False
    verbose: bool = False

    def with_ascii_only(self) -> Flags:
        """Return a new :class:`Flags` with ``ascii_only`` enabled."""
        return replace(self, ascii_only=True)

    def with_debug(self) -> Flags:
        """Return a new :class:`Flags` with ``debug`` enabled."""
        return replace(self, debug=True)

    def with_ignore_case(self) -> Flags:
        """Return a new :class:`Flags` with ``ignore_case`` enabled."""
        return replace(self, ignore_case=True)

    def with_multiline(self) -> Flags:
        """Return a new :class:`Flags` with ``multiline`` enabled."""
        return replace(self, multiline=True)

    def with_dotall(self) -> Flags:
        """Return a new :class:`Flags` with ``dotall`` enabled."""
        return replace(self, dotall=True)

    def with_verbose(self) -> Flags:
        """Return a new :class:`Flags` with ``verbose`` enabled."""
        return replace(self, verbose=True)

    def with_merged(self, other: Flags) -> Flags:
        """Return a new :class:`Flags` whose every field is the logical-or of self and ``other``."""
        return Flags(
            ascii_only=self.ascii_only or other.ascii_only,
            debug=self.debug or other.debug,
            ignore_case=self.ignore_case or other.ignore_case,
            multiline=self.multiline or other.multiline,
            dotall=self.dotall or other.dotall,
            verbose=self.verbose or other.verbose,
        )
