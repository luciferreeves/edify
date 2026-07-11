"""``tin`` — US Taxpayer Identification Number (SSN, EIN, or ITIN forms)."""

from __future__ import annotations

from edify import any_of
from edify.library.identifier.ein import ein
from edify.library.identifier.itin import itin
from edify.library.identifier.ssn import ssn

tin = any_of(ssn, ein, itin)
"""Callable :class:`Pattern` that accepts any US Taxpayer ID form: SSN
(``AAA-GG-SSSS``), EIN (``XX-XXXXXXX``), or ITIN (``9NN-YY-ZZZZ``).
"""
