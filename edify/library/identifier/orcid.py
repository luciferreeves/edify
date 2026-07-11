"""``orcid`` — ORCID researcher identifier ``NNNN-NNNN-NNNN-NNNX``."""

from __future__ import annotations

from edify import Pattern

orcid = (
    Pattern()
    .start_of_input()
    .exactly(4).digit()
    .char("-")
    .exactly(4).digit()
    .char("-")
    .exactly(4).digit()
    .char("-")
    .exactly(3).digit()
    .any_of().digit().char("X").end()
    .end_of_input()
)
"""Callable :class:`Pattern` for the ORCID identifier shape:
four hyphen-separated groups of four digits, with the last position
allowing an ``X`` check character.
"""
