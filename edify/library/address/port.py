"""``port`` — TCP/UDP port number 0-65535."""

from __future__ import annotations

from edify import Pattern, any_of

port = any_of(
    Pattern().start_of_input().string("6553").range("0", "5").end_of_input(),
    Pattern().start_of_input().string("655").range("0", "2").digit().end_of_input(),
    Pattern().start_of_input().string("65").range("0", "4").exactly(2).digit().end_of_input(),
    Pattern().start_of_input().string("6").range("0", "4").exactly(3).digit().end_of_input(),
    Pattern().start_of_input().range("1", "5").exactly(4).digit().end_of_input(),
    Pattern().start_of_input().range("1", "9").between(0, 3).digit().end_of_input(),
    Pattern().start_of_input().char("0").end_of_input(),
)
"""Callable :class:`Pattern` for a TCP/UDP port number 0-65535."""
