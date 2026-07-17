"""Playground Sphinx extension.

Minimal registration now so the theme builds; the ``edify-playground`` directive,
the ``py-live`` fence, and the autocomplete-catalog hook land in Phase 3.
"""

from __future__ import annotations

from sphinx.application import Sphinx


def setup(app: Sphinx) -> dict[str, object]:
    return {"parallel_read_safe": True, "parallel_write_safe": True}
