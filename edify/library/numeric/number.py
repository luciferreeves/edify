"""``number`` — number in any base or common form."""

from __future__ import annotations

from edify import Pattern, any_of


def _sign() -> Pattern:
    return Pattern().optional().any_of_chars("+-")


_int = Pattern().subexpression(_sign()).one_or_more().digit()
_dec = (
    Pattern()
    .subexpression(_sign())
    .one_or_more()
    .digit()
    .char(".")
    .one_or_more()
    .digit()
)
_ldec = Pattern().subexpression(_sign()).char(".").one_or_more().digit()
_sci_dec = (
    Pattern()
    .subexpression(_sign())
    .one_or_more()
    .digit()
    .char(".")
    .zero_or_more()
    .digit()
    .any_of_chars("eE")
    .optional()
    .any_of_chars("+-")
    .one_or_more()
    .digit()
)
_sci_int = (
    Pattern()
    .subexpression(_sign())
    .one_or_more()
    .digit()
    .any_of_chars("eE")
    .optional()
    .any_of_chars("+-")
    .one_or_more()
    .digit()
)
_hex = (
    Pattern()
    .char("0")
    .any_of_chars("xX")
    .one_or_more()
    .any_of()
    .range("0", "9")
    .range("a", "f")
    .range("A", "F")
    .end()
)
_oct = Pattern().char("0").any_of_chars("oO").one_or_more().range("0", "7")
_bin = Pattern().char("0").any_of_chars("bB").one_or_more().any_of_chars("01")
_complex = (
    Pattern()
    .subexpression(_sign())
    .one_or_more()
    .digit()
    .optional()
    .group()
    .char(".")
    .one_or_more()
    .digit()
    .end()
    .any_of_chars("+-")
    .one_or_more()
    .digit()
    .optional()
    .group()
    .char(".")
    .one_or_more()
    .digit()
    .end()
    .any_of_chars("jJi")
)

number = (
    Pattern()
    .start_of_input()
    .subexpression(any_of(_int, _dec, _ldec, _sci_dec, _sci_int, _hex, _oct, _bin, _complex))
    .end_of_input()
)
"""Callable :class:`Pattern` that accepts numbers in any base or form:
signed integers, decimals, floats, scientific, hex (``0x``), octal (``0o``),
binary (``0b``), or complex (``a+bj``).
"""
