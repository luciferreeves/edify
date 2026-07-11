"""``script`` — text in a specific Unicode script."""

from __future__ import annotations

from edify import Pattern, any_of

_latin = (
    Pattern()
    .one_or_more()
    .any_of()
    .range("A", "Z")
    .range("a", "z")
    .range("À", "ɏ")
    .end()
)
_cyrillic = Pattern().one_or_more().range("Ѐ", "ӿ")
_greek = Pattern().one_or_more().range("Ͱ", "Ͽ")
_cjk = (
    Pattern()
    .one_or_more()
    .any_of()
    .range("一", "鿿")
    .range("぀", "ゟ")
    .range("゠", "ヿ")  # noqa: RUF001
    .range("가", "힯")
    .end()
)
_arabic = Pattern().one_or_more().range("؀", "ۿ")
_hebrew = Pattern().one_or_more().range("֐", "׿")
_devanagari = Pattern().one_or_more().range("ऀ", "ॿ")

script = (
    Pattern()
    .start_of_input()
    .subexpression(any_of(_latin, _cyrillic, _greek, _cjk, _arabic, _hebrew, _devanagari))
    .end_of_input()
)
"""Callable :class:`Pattern` for text in a single common Unicode script:
Latin (with extensions), Cyrillic, Greek, CJK (Chinese/Japanese/Korean),
Arabic, Hebrew, or Devanagari.
"""
