"""Build the edify wheel into ``docs/_static/`` for the in-browser playground."""

from __future__ import annotations

import subprocess
from pathlib import Path

_STATIC = Path(__file__).resolve().parent.parent.parent / "docs" / "_static"


def build_wheel_into_static() -> Path:
    """Build the current edify wheel into ``docs/_static/`` and return its path."""
    _STATIC.mkdir(parents=True, exist_ok=True)
    for stale in _STATIC.glob("edify-*.whl"):
        stale.unlink()
    subprocess.run(["uv", "build", "--wheel", "--out-dir", str(_STATIC)], check=True)
    wheels = sorted(_STATIC.glob("edify-*.whl"))
    if not wheels:
        raise RuntimeError("wheel build produced no edify-*.whl in docs/_static")
    return wheels[-1]


if __name__ == "__main__":
    print(build_wheel_into_static())
