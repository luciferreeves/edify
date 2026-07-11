"""Private composable atoms shared by the library validators.

Every atom is a :class:`Pattern` fragment that renders exactly what the
comment beside it says; nothing here is exported publicly, but every entry
is imported freely by the exported validators to keep their fluent chains
readable.
"""

from __future__ import annotations

from edify import Pattern, any_of

hex_lower = Pattern().any_of().range("0", "9").range("a", "f").end()
"""A single lowercase hex nibble: ``[0-9a-f]``."""

hex_upper = Pattern().any_of().range("0", "9").range("A", "F").end()
"""A single uppercase hex nibble: ``[0-9A-F]``."""

hex_any = Pattern().any_of().range("0", "9").range("a", "f").range("A", "F").end()
"""A single mixed-case hex nibble: ``[0-9a-fA-F]``."""

digit_atom = Pattern().digit()
"""A single decimal digit: ``\\d``."""

octet = any_of(
    Pattern().string("25").range("0", "5"),
    Pattern().char("2").range("0", "4").digit(),
    Pattern().char("1").digit().digit(),
    Pattern().range("1", "9").digit(),
    Pattern().digit(),
)
"""An IPv4 octet in ``0``-``255``."""
