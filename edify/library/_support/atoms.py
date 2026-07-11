"""Private composable atoms shared by the library validators.

Every atom is a :class:`Pattern` fragment that renders exactly what the
comment beside it says; nothing here is exported publicly, but every entry
is imported freely by the exported validators to keep their fluent chains
readable.
"""

from __future__ import annotations

from edify import RegexBuilder, any_of, char, range_of
from edify.library._support.coerce import as_pattern


def _hex_lower_atom() -> object:
    return as_pattern(RegexBuilder().any_of().range("0", "9").range("a", "f").end())


def _hex_upper_atom() -> object:
    return as_pattern(RegexBuilder().any_of().range("0", "9").range("A", "F").end())


def _hex_any_atom() -> object:
    chain = (
        RegexBuilder().any_of().range("0", "9").range("a", "f").range("A", "F").end()
    )
    return as_pattern(chain)


def _digit_atom() -> object:
    return as_pattern(RegexBuilder().digit())


def _octet_atom() -> object:
    branch_250_255 = RegexBuilder().string("25").range("0", "5")
    branch_200_249 = RegexBuilder().char("2").range("0", "4").digit()
    branch_100_199 = RegexBuilder().char("1").digit().digit()
    branch_10_99 = RegexBuilder().range("1", "9").digit()
    branch_0_9 = RegexBuilder().digit()
    return any_of(
        as_pattern(branch_250_255),
        as_pattern(branch_200_249),
        as_pattern(branch_100_199),
        as_pattern(branch_10_99),
        as_pattern(branch_0_9),
    )


hex_lower = _hex_lower_atom()
"""A single lowercase hex nibble: ``[0-9a-f]``."""

hex_upper = _hex_upper_atom()
"""A single uppercase hex nibble: ``[0-9A-F]``."""

hex_any = _hex_any_atom()
"""A single mixed-case hex nibble: ``[0-9a-fA-F]``."""

digit_atom = _digit_atom()
"""A single decimal digit: ``\\d``."""

octet = _octet_atom()
"""An IPv4 octet in ``0``-``255``."""