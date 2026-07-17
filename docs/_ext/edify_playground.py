"""Playground Sphinx extension.

Registers the homepage template override now; the ``edify-playground`` directive,
the autocomplete-catalog hook, and the generated Library reference land in later phases.
"""

from __future__ import annotations

from typing import Any

from sphinx.application import Sphinx


def _use_home_template(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: Any,
) -> str | None:
    if pagename == "index":
        return "home.html"
    return None


def setup(app: Sphinx) -> dict[str, object]:
    app.connect("html-page-context", _use_home_template)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
