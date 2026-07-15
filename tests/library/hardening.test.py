"""Real-world corpus hardening tests for every hand-picked library validator.

Each corpus file under ``tests/library/corpora/<name>.toml`` lists ``accepts``
and ``rejects`` — strings the named validator must accept or reject exactly.
Adding a new validator only means dropping a new TOML file next to the others;
the parametrization discovers it at collection time.
"""

from __future__ import annotations

import tomllib
from pathlib import Path

import pytest

import edify.library as library_module
from edify import Pattern

_CORPUS_ROOT = Path(__file__).parent / "corpora"


def _corpus_cases():
    for corpus_path in sorted(_CORPUS_ROOT.glob("*.toml")):
        validator_name = corpus_path.stem
        validator = getattr(library_module, validator_name)
        if not isinstance(validator, Pattern):
            continue
        parsed = tomllib.loads(corpus_path.read_text())
        for accept_input in parsed.get("accepts", []):
            yield validator_name, validator, "accept", accept_input
        for reject_input in parsed.get("rejects", []):
            yield validator_name, validator, "reject", reject_input


_CASES = list(_corpus_cases())


@pytest.mark.parametrize(
    ("validator_name", "validator", "expected_verdict", "input_string"),
    _CASES,
    ids=[
        f"{name}-{verdict}-{index}"
        for index, (name, _validator, verdict, _input_string) in enumerate(_CASES)
    ],
)
def test_library_validator_matches_the_committed_corpus(
    validator_name, validator, expected_verdict, input_string
):
    observed = validator(input_string)
    if expected_verdict == "accept":
        assert observed is True, (
            f"validator {validator_name!r} rejected {input_string!r} but corpus expects accept"
        )
    else:
        assert observed is False, (
            f"validator {validator_name!r} accepted {input_string!r} but corpus expects reject"
        )
