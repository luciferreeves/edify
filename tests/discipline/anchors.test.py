"""Deprecation-URL anchor contract.

A deprecation warning points users at ``docs/upgrading/...#anchor``. Shape-checking
the URL alone passes even when the anchor 404s. This test extracts every anchor
referenced by a deprecation stub, parses the upgrade guides for their actual
``.. _label:`` targets, and asserts each referenced anchor exists.

Edify 1.0 ships stub-free, so the deprecation-URL registry is empty today; the
test still verifies that every anchor the upgrade guides *declare* is well-formed
and unique, so the contract is enforced the moment the first stub lands.
"""

import re
from pathlib import Path

_REPO_ROOT = Path(__file__).parent.parent.parent
_UPGRADING_DIR = _REPO_ROOT / "docs" / "upgrading"
_ANCHOR_PATTERN = re.compile(r"^\.\.\s+_([a-zA-Z0-9][a-zA-Z0-9\-]*):\s*$")

# Anchors referenced by deprecation-warning URLs. Each entry is (guide-stem, anchor).
# Empty in 1.0 (stub-free); every future deprecation stub adds its (guide, anchor) row.
_DEPRECATION_URL_ANCHORS: frozenset[tuple[str, str]] = frozenset()


def _declared_anchors(rst_path: Path) -> list[str]:
    anchors: list[str] = []
    for line in rst_path.read_text().splitlines():
        matched = _ANCHOR_PATTERN.match(line)
        if matched is not None:
            anchors.append(matched.group(1))
    return anchors


def _anchors_by_guide() -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for rst_path in sorted(_UPGRADING_DIR.glob("*.rst")):
        result[rst_path.stem] = _declared_anchors(rst_path)
    return result


def test_upgrade_guide_anchors_are_unique_within_each_guide():
    for guide_stem, anchors in _anchors_by_guide().items():
        assert len(anchors) == len(set(anchors)), (
            f"duplicate anchor(s) in docs/upgrading/{guide_stem}.rst: "
            f"{sorted({a for a in anchors if anchors.count(a) > 1})}"
        )


def test_every_deprecation_url_anchor_exists_in_its_guide():
    anchors_by_guide = _anchors_by_guide()
    for guide_stem, anchor in _DEPRECATION_URL_ANCHORS:
        declared = anchors_by_guide.get(guide_stem, [])
        assert anchor in declared, (
            f"deprecation URL references #{anchor} in docs/upgrading/{guide_stem}.rst, "
            f"but no `.. _{anchor}:` target exists there."
        )


def test_the_0_3_to_1_0_guide_declares_the_license_anchor():
    anchors = _anchors_by_guide()["0.3-to-1.0"]
    assert "license-mit" in anchors


def test_the_0_3_to_1_0_guide_declares_the_python_floor_anchor():
    anchors = _anchors_by_guide()["0.3-to-1.0"]
    assert "python-floor" in anchors
