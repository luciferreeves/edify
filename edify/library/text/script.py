"""``script`` — text in a specific Unicode script."""

from __future__ import annotations

from edify.library._support.regex import RegexBackedPattern

script = RegexBackedPattern(
    r"^(?:"
    r"[A-Za-zÀ-ɏ]+"
    r"|[Ѐ-ӿ]+"
    r"|[Ͱ-Ͽ]+"
    r"|[一-鿿぀-ゟ゠-ヿ가-힯]+"  # noqa: RUF001
    r"|[؀-ۿ]+"
    r"|[֐-׿]+"
    r"|[ऀ-ॿ]+"
    r")$"
)
"""Callable :class:`Pattern` for text in a single common Unicode script:
Latin (with extensions), Cyrillic, Greek, CJK (Chinese/Japanese/Korean),
Arabic, Hebrew, or Devanagari.
"""
