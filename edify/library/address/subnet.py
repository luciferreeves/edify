"""``subnet`` — dotted-decimal IPv4 subnet mask shape."""

from __future__ import annotations

from edify import Pattern, any_of


def _mask_octet() -> Pattern:
    return any_of(
        Pattern().string("255"),
        Pattern().string("254"),
        Pattern().string("252"),
        Pattern().string("248"),
        Pattern().string("240"),
        Pattern().string("224"),
        Pattern().string("192"),
        Pattern().string("128"),
        Pattern().char("0"),
    )


subnet = (
    Pattern()
    .start_of_input()
    .subexpression(_mask_octet())
    .char(".")
    .subexpression(_mask_octet())
    .char(".")
    .subexpression(_mask_octet())
    .char(".")
    .subexpression(_mask_octet())
    .end_of_input()
)
"""Callable :class:`Pattern` for a dotted-decimal IPv4 subnet mask
(each octet is one of ``255``, ``254``, ``252``, …, ``128``, ``0``).
"""
