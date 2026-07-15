"""``password`` — configurable password-strength validator (callable :class:`Pattern` subclass)."""

from __future__ import annotations

import re

from edify.pattern.composition import Pattern

_DEFAULT_SPECIAL_CHARS = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
_UPPERCASE_RE = re.compile("[A-Z]")
_LOWERCASE_RE = re.compile("[a-z]")
_DIGIT_RE = re.compile("[0-9]")


class _PasswordPattern(Pattern):
    """Callable :class:`Pattern` that checks configurable password thresholds.

    Attributes:
        min_length: Minimum length inclusive.
        max_length: Maximum length inclusive.
        min_upper: Minimum required uppercase letters.
        min_lower: Minimum required lowercase letters.
        min_digit: Minimum required decimal digits.
        min_special: Minimum required special characters.
        special_chars: The set of characters counted toward ``min_special``.
    """

    def __init__(
        self,
        min_length: int = 8,
        max_length: int = 64,
        min_upper: int = 1,
        min_lower: int = 1,
        min_digit: int = 1,
        min_special: int = 1,
        special_chars: str = _DEFAULT_SPECIAL_CHARS,
    ) -> None:
        super().__init__()
        self.min_length = min_length
        self.max_length = max_length
        self.min_upper = min_upper
        self.min_lower = min_lower
        self.min_digit = min_digit
        self.min_special = min_special
        self.special_chars = special_chars

    def __call__(
        self,
        value: str,
        min_length: int | None = None,
        max_length: int | None = None,
        min_upper: int | None = None,
        min_lower: int | None = None,
        min_digit: int | None = None,
        min_special: int | None = None,
        special_chars: str | None = None,
    ) -> bool:
        """Return True when ``value`` meets every configured threshold."""
        if not isinstance(value, str):
            return False
        effective_min_length = self.min_length if min_length is None else min_length
        effective_max_length = self.max_length if max_length is None else max_length
        effective_min_upper = self.min_upper if min_upper is None else min_upper
        effective_min_lower = self.min_lower if min_lower is None else min_lower
        effective_min_digit = self.min_digit if min_digit is None else min_digit
        effective_min_special = self.min_special if min_special is None else min_special
        effective_special = self.special_chars if special_chars is None else special_chars
        length_ok = effective_min_length <= len(value) <= effective_max_length
        upper_ok = len(_UPPERCASE_RE.findall(value)) >= effective_min_upper
        lower_ok = len(_LOWERCASE_RE.findall(value)) >= effective_min_lower
        digit_ok = len(_DIGIT_RE.findall(value)) >= effective_min_digit
        special_flags = [1 for character in value if character in effective_special]
        special_count = sum(special_flags)
        special_ok = special_count >= effective_min_special
        return length_ok and upper_ok and lower_ok and digit_ok and special_ok


password = _PasswordPattern()
"""Callable :class:`Pattern` (subclass) that enforces configurable password-strength thresholds.

Call as ``password(value)`` for the defaults or ``password(value, min_length=12, min_special=2)``
to tighten specific thresholds.

Default policy:
    * Length between 8 and 64 characters inclusive.
    * At least one uppercase letter, one lowercase letter, one decimal digit, and
      one special character from the default set (``!@#$%^&*()_+-=[]{}|;':",./<>?``).

Guarantees:
    * Every threshold is checked exactly as configured — no silent lower/upper bound.
    * The special-character set is overridable per call via ``special_chars=``.

Does not guarantee:
    * Passphrase strength beyond the counted-class thresholds — e.g. does not
      reject dictionary words, common patterns, keyboard walks, or breached-password
      corpora.
    * Non-ASCII character-class handling — the class regex targets ASCII letters
      and digits.
"""
