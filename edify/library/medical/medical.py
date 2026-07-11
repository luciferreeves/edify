"""``medical`` — medical-coding-system code shape (SNOMED, ICD, NPI, RxNorm, LOINC)."""

from __future__ import annotations

from edify import Pattern, any_of

_snomed = Pattern().between(6, 18).digit()
_icd = (
    Pattern()
    .any_of().range("A", "T").range("V", "Z").end()
    .digit()
    .any_of().range("A", "Z").range("0", "9").end()
    .optional()
    .group()
    .char(".")
    .between(1, 4)
    .any_of().range("A", "Z").range("0", "9").end()
    .end()
)
_npi = Pattern().exactly(10).digit()
_loinc = Pattern().between(1, 7).digit().char("-").digit()

medical = (
    Pattern()
    .start_of_input()
    .subexpression(any_of(_snomed, _icd, _npi, _loinc))
    .end_of_input()
)
"""Callable :class:`Pattern` for medical-coding-system codes."""
