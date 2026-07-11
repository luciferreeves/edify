"""``ptr`` — reverse-DNS PTR record shape (``d.c.b.a.in-addr.arpa`` or IPv6 nibble form)."""

from __future__ import annotations

from edify import Pattern, any_of
from edify.library._support.atoms import hex_any

_ipv4_ptr = (
    Pattern()
    .exactly(4)
    .group()
    .between(1, 3)
    .digit()
    .char(".")
    .end()
    .string("in-addr")
    .char(".")
    .string("arpa")
    .optional()
    .char(".")
)
_ipv6_ptr = (
    Pattern()
    .exactly(32)
    .group()
    .subexpression(hex_any)
    .char(".")
    .end()
    .string("ip6")
    .char(".")
    .string("arpa")
    .optional()
    .char(".")
)

ptr = (
    Pattern()
    .start_of_input()
    .subexpression(any_of(_ipv4_ptr, _ipv6_ptr))
    .end_of_input()
)
"""Callable :class:`Pattern` for the reverse-DNS PTR shape: IPv4
``d.c.b.a.in-addr.arpa`` or IPv6 32-nibble ``…ip6.arpa`` form.
"""
