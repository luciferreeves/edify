"""Resolve ``Self`` in documented signatures to the class the method belongs to.

``typing.Self`` is precise in source but opaque in a reference: a reader sees
``-> Self`` and still has to work out what that is, and the word links nowhere.
Substituting the owning class name gives the same guarantee in a term the reader
already knows, and the Python domain turns it into a cross-reference for free.

Return annotations are rewritten for every documented method; parameter
annotations carrying ``Self`` are rewritten the same way.
"""

from __future__ import annotations

import re
from typing import Any

from sphinx.application import Sphinx

_SELF = re.compile(r"(?:[\w.]+\.)?\bSelf\b")
_SHORTEN_MARKER = re.compile(r"~(?=[\w.]+)")


def _owning_class(name: str) -> str | None:
    """Return the dotted path of the class a member belongs to, or None for a plain function."""
    parts = name.split(".")
    if len(parts) < 2:
        return None
    owner = parts[-2]
    if not owner[:1].isupper():
        return None
    return ".".join(parts[:-1])


def _clean(text: str | None, owner: str | None) -> str | None:
    """Resolve ``Self`` to ``owner`` and drop the ``~`` display marker autodoc leaks."""
    if not text:
        return text
    if owner is not None:
        text = _SELF.sub(owner, text)
    return _SHORTEN_MARKER.sub("", text)


def _rewrite_annotations(
    app: Sphinx,
    what: str,
    name: str,
    obj: Any,
    options: Any,
    signature: str | None,
    return_annotation: str | None,
) -> tuple[str | None, str | None]:
    owner = _owning_class(name)
    return _clean(signature, owner), _clean(return_annotation, owner)


def setup(app: Sphinx) -> dict[str, object]:
    app.connect("autodoc-process-signature", _rewrite_annotations)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
