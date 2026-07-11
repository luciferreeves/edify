"""``email`` — email address shape (basic or RFC 5322)."""

from __future__ import annotations

from edify import Pattern, any_of


def _local_char_class() -> Pattern:
    return (
        Pattern()
        .any_of()
        .range("a", "z")
        .range("0", "9")
        .char("!")
        .char("#")
        .char("$")
        .char("%")
        .char("&")
        .char("'")
        .char("*")
        .char("+")
        .char("/")
        .char("=")
        .char("?")
        .char("^")
        .char("_")
        .char("`")
        .char("{")
        .char("|")
        .char("}")
        .char("~")
        .char("-")
        .end()
    )


def _domain_label() -> Pattern:
    return (
        Pattern()
        .any_of()
        .range("a", "z")
        .range("0", "9")
        .end()
        .optional()
        .group()
        .zero_or_more()
        .any_of()
        .range("a", "z")
        .range("0", "9")
        .char("-")
        .end()
        .any_of()
        .range("a", "z")
        .range("0", "9")
        .end()
        .end()
    )


_basic_local = (
    Pattern()
    .one_or_more()
    .subexpression(_local_char_class())
    .zero_or_more()
    .group()
    .char(".")
    .one_or_more()
    .subexpression(_local_char_class())
    .end()
)

_basic_domain = (
    Pattern()
    .one_or_more()
    .group()
    .subexpression(_domain_label())
    .char(".")
    .end()
    .subexpression(_domain_label())
)

_basic = Pattern().subexpression(_basic_local).char("@").subexpression(_basic_domain)


def _quoted_text() -> Pattern:
    return (
        Pattern()
        .any_of()
        .range("\x01", "\x08")
        .char("\x0b")
        .char("\x0c")
        .range("\x0e", "\x1f")
        .char("\x21")
        .range("\x23", "\x5b")
        .range("\x5d", "\x7f")
        .end()
    )


def _quoted_escape() -> Pattern:
    return (
        Pattern()
        .char("\\")
        .any_of()
        .range("\x01", "\x09")
        .char("\x0b")
        .char("\x0c")
        .range("\x0e", "\x7f")
        .end()
    )


_quoted_local = (
    Pattern()
    .char('"')
    .zero_or_more()
    .subexpression(any_of(_quoted_text(), _quoted_escape()))
    .char('"')
)


def _octet() -> Pattern:
    return any_of(
        Pattern().string("25").range("0", "5"),
        Pattern().char("2").range("0", "4").digit(),
        Pattern().optional().any_of_chars("01").digit().optional().digit(),
    )


def _bracket_text() -> Pattern:
    return (
        Pattern()
        .any_of()
        .range("\x01", "\x08")
        .char("\x0b")
        .char("\x0c")
        .range("\x0e", "\x1f")
        .range("\x21", "\x5a")
        .range("\x53", "\x7f")
        .end()
    )


def _bracket_escape() -> Pattern:
    return (
        Pattern()
        .char("\\")
        .any_of()
        .range("\x01", "\x09")
        .char("\x0b")
        .char("\x0c")
        .range("\x0e", "\x7f")
        .end()
    )


_ip_literal_tail = any_of(
    _octet(),
    (
        Pattern()
        .zero_or_more()
        .any_of()
        .range("a", "z")
        .range("0", "9")
        .char("-")
        .end()
        .any_of()
        .range("a", "z")
        .range("0", "9")
        .end()
        .char(":")
        .one_or_more()
        .subexpression(any_of(_bracket_text(), _bracket_escape()))
    ),
)

_ip_literal = (
    Pattern()
    .char("[")
    .exactly(3)
    .group()
    .subexpression(_octet())
    .char(".")
    .end()
    .subexpression(_ip_literal_tail)
    .char("]")
)

_rfc_local = any_of(_basic_local, _quoted_local)
_rfc_domain = any_of(_basic_domain, _ip_literal)
_rfc = Pattern().subexpression(_rfc_local).char("@").subexpression(_rfc_domain)

email = Pattern().start_of_input().subexpression(any_of(_basic, _rfc)).end_of_input()
"""Callable :class:`Pattern` that accepts either the common permissive email
shape or the full RFC 5322 mailbox shape.
"""
