"""``number`` — number in any base or form (integer, decimal, hex, binary, octal, scientific, complex)."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

number = RegexBackedPattern(
    r"^(?:"
    r"[+-]?\d+"
    r"|[+-]?\d+\.\d+"
    r"|[+-]?\.\d+"
    r"|[+-]?\d+\.\d*[eE][+-]?\d+"
    r"|[+-]?\d+[eE][+-]?\d+"
    r"|0[xX][0-9a-fA-F]+"
    r"|0[oO][0-7]+"
    r"|0[bB][01]+"
    r"|[+-]?\d+(?:\.\d+)?[+-]\d+(?:\.\d+)?[jJi]"
    r")$"
)
"""Callable :class:`Pattern` that accepts numbers in any base or form:
signed integers, decimals, floats, scientific, hex (``0x``), octal (``0o``),
binary (``0b``), or complex (``a+bj``).
"""
