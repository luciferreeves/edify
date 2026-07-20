"""Playground Sphinx extension.

Provides the homepage/section template overrides and the ``edify-playground``
directive, which renders a mount point the browser widget hydrates into a live
editor. Each directive may carry its own initial test strings via the ``:tests:``
option (pipe-separated), so every embedded playground demonstrates its own topic.
"""

from __future__ import annotations

import base64
import html
from typing import Any

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.application import Sphinx

_STANDALONE = {
    "playground": "wide.html",
    "api/index": "api.html",
    "library/index": "wide.html",
    "upgrading/index": "wide.html",
    "upgrading/0.3-to-1.0": "wide.html",
    "deprecation-policy": "wide.html",
    "changelog": "wide.html",
    "contributing": "wide.html",
}


def _encode(text: str) -> str:
    return base64.b64encode(text.encode("utf-8")).decode("ascii")


class EdifyPlayground(Directive):
    """``.. edify-playground::`` — a live builder/regex/test widget.

    The directive body is the starting chain. The optional ``:tests:`` option is a
    pipe-separated list of strings to seed the test panel. It renders as a mount
    point; the playground JS hydrates it into the interactive editor, falling back
    to the rendered source when scripting is unavailable.
    """

    has_content = True
    option_spec = {"tests": directives.unchanged}

    def run(self) -> list[nodes.Node]:
        source = "\n".join(self.content).strip()
        attributes = f'data-source="{_encode(source)}"'
        raw_tests = self.options.get("tests", "")
        test_lines = [item.strip() for item in raw_tests.split("|") if item.strip()]
        if test_lines:
            attributes += f' data-tests="{_encode(chr(10).join(test_lines))}"'
        markup = (
            f'<div class="edify-playground" {attributes}>'
            f'<pre class="pg-code pg-fallback">{html.escape(source)}</pre>'
            f"</div>"
        )
        return [nodes.raw("", markup, format="html")]


def _select_template(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: Any,
) -> str | None:
    if pagename == "index":
        return "home.html"
    if pagename.startswith("library/"):
        return "wide.html"
    return _STANDALONE.get(pagename)


def setup(app: Sphinx) -> dict[str, object]:
    app.add_directive("edify-playground", EdifyPlayground)
    app.connect("html-page-context", _select_template)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
