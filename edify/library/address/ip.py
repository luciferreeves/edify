"""``ip`` — IPv4 or IPv6 address shape."""

from __future__ import annotations

from edify import Pattern, any_of
from edify.library._support.atoms import hex_any, octet


def _hex_group() -> Pattern:
    return Pattern().between(1, 4).subexpression(hex_any)


_ipv4 = Pattern().subexpression(octet).exactly(3).group().char(".").subexpression(octet).end()


def _b1() -> Pattern:
    return (
        Pattern()
        .exactly(7)
        .group()
        .subexpression(_hex_group())
        .char(":")
        .end()
        .subexpression(_hex_group())
    )


def _b2() -> Pattern:
    return Pattern().between(1, 7).group().subexpression(_hex_group()).char(":").end().char(":")


def _b3() -> Pattern:
    return (
        Pattern()
        .between(1, 6)
        .group()
        .subexpression(_hex_group())
        .char(":")
        .end()
        .char(":")
        .subexpression(_hex_group())
    )


def _b_mixed(prefix_count: int, suffix_count: int) -> Pattern:
    return (
        Pattern()
        .between(1, prefix_count)
        .group()
        .subexpression(_hex_group())
        .char(":")
        .end()
        .between(1, suffix_count)
        .group()
        .char(":")
        .subexpression(_hex_group())
        .end()
    )


def _b8() -> Pattern:
    return (
        Pattern()
        .subexpression(_hex_group())
        .char(":")
        .group()
        .between(1, 6)
        .group()
        .char(":")
        .subexpression(_hex_group())
        .end()
        .end()
    )


def _b9() -> Pattern:
    return (
        Pattern()
        .char(":")
        .group()
        .any_of()
        .subexpression(Pattern().between(1, 7).group().char(":").subexpression(_hex_group()).end())
        .char(":")
        .end()
        .end()
    )


def _b_link_local() -> Pattern:
    return (
        Pattern()
        .string("fe80:")
        .between(0, 4)
        .group()
        .char(":")
        .between(0, 4)
        .subexpression(hex_any)
        .end()
        .char("%")
        .one_or_more()
        .any_of()
        .range("0", "9")
        .range("a", "z")
        .range("A", "Z")
        .end()
    )


def _map_octet() -> Pattern:
    return any_of(
        Pattern().string("25").range("0", "5"),
        (
            Pattern()
            .optional()
            .group()
            .any_of()
            .subexpression(Pattern().char("2").range("0", "4"))
            .subexpression(Pattern().optional().char("1").digit())
            .end()
            .end()
            .digit()
        ),
    )


def _mapped_ipv4() -> Pattern:
    return (
        Pattern()
        .exactly(3)
        .group()
        .subexpression(_map_octet())
        .char(".")
        .end()
        .subexpression(_map_octet())
    )


def _b_ipv4_mapped() -> Pattern:
    return (
        Pattern()
        .string("::")
        .optional()
        .group()
        .string("ffff")
        .optional()
        .group()
        .char(":")
        .between(1, 4)
        .char("0")
        .end()
        .char(":")
        .end()
        .subexpression(_mapped_ipv4())
    )


def _b_hybrid() -> Pattern:
    return (
        Pattern()
        .between(1, 4)
        .group()
        .subexpression(_hex_group())
        .char(":")
        .end()
        .char(":")
        .subexpression(_mapped_ipv4())
    )


_ipv6 = any_of(
    _b1(),
    _b2(),
    _b3(),
    _b_mixed(5, 2),
    _b_mixed(4, 3),
    _b_mixed(3, 4),
    _b_mixed(2, 5),
    _b8(),
    _b9(),
    _b_link_local(),
    _b_ipv4_mapped(),
    _b_hybrid(),
)

ip = Pattern().start_of_input().subexpression(any_of(_ipv4, _ipv6)).end_of_input()
"""Callable :class:`Pattern` for IPv4 dotted-quad or any IPv6 form."""
