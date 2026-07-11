"""``sku`` — Stock Keeping Unit (4-20 alphanumerics plus common separators)."""

from __future__ import annotations

from edify import Pattern

sku = (
    Pattern()
    .start_of_input()
    .between(4, 20)
    .any_of()
    .range("A", "Z")
    .range("a", "z")
    .range("0", "9")
    .any_of_chars("-_./")
    .end()
    .end_of_input()
)
"""Callable :class:`Pattern` for a permissive SKU shape: 4-20 characters
drawn from letters, digits, and common product-code separators
(``-``, ``_``, ``.``, ``/``).
"""
