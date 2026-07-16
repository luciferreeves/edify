"""Compute Edify's public API surface as a stable, diffable text snapshot.

Walks ``edify`` and its documented public submodules, and emits one line per
public symbol: its dotted path plus, for callables, a normalized signature. The
output is deterministic (sorted) so a diff against the committed
``.public-surface`` file shows exactly what a PR added, removed, or changed.
"""

from __future__ import annotations

import importlib
import inspect
import pkgutil
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
_SURFACE_PATH = _REPO_ROOT / ".public-surface"
_ROOT_PACKAGE = "edify"


def compute_surface() -> str:
    """Return the full public-surface snapshot text for the ``edify`` package."""
    module_names = _public_module_names()
    entries: list[str] = []
    for module_name in module_names:
        module = importlib.import_module(module_name)
        entries.extend(_module_entries(module_name, module))
    unique_sorted = sorted(set(entries))
    return "\n".join(unique_sorted) + "\n"


def _public_module_names() -> list[str]:
    root_module = importlib.import_module(_ROOT_PACKAGE)
    root_path = root_module.__path__
    names = [_ROOT_PACKAGE]
    for module_info in pkgutil.walk_packages(root_path, prefix=f"{_ROOT_PACKAGE}."):
        if _is_private_path(module_info.name):
            continue
        names.append(module_info.name)
    return names


def _is_private_path(dotted_name: str) -> bool:
    parts = dotted_name.split(".")
    return any(part.startswith("_") for part in parts)


def _module_entries(module_name: str, module: object) -> list[str]:
    exported_names = getattr(module, "__all__", None)
    if exported_names is None:
        return []
    entries: list[str] = []
    for symbol_name in exported_names:
        if symbol_name.startswith("_"):
            continue
        value = getattr(module, symbol_name, None)
        entries.append(_render_symbol(module_name, symbol_name, value))
    return entries


def _render_symbol(module_name: str, symbol_name: str, value: object) -> str:
    dotted = f"{module_name}.{symbol_name}"
    signature = _signature_or_empty(value)
    if signature:
        return f"{dotted}{signature}"
    return dotted


def _signature_or_empty(value: object) -> str:
    if not callable(value):
        return ""
    try:
        return str(inspect.signature(value))
    except (ValueError, TypeError):
        return ""


def main(argv: list[str]) -> int:
    """Print the surface; with ``--write`` overwrite the committed snapshot file."""
    surface = compute_surface()
    if "--write" in argv:
        _SURFACE_PATH.write_text(surface, encoding="utf-8")
        return 0
    if "--check" in argv:
        committed = _SURFACE_PATH.read_text(encoding="utf-8")
        if committed != surface:
            sys.stderr.write(
                "public surface drift: run `python tools/surface.py --write` and commit "
                ".public-surface, adding a changes/ fragment for the change.\n"
            )
            return 1
        return 0
    sys.stdout.write(surface)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
