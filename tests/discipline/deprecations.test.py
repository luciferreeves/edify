"""Deprecation-stub contract harness.

Every deprecated public symbol must fire exactly one :class:`DeprecationWarning`
whose message matches the policy format::

    <name> is deprecated since <version>; use <replacement>. See <docs-url>

with ``stacklevel=2`` so the warning points at the caller. Edify 1.0 ships
stub-free, so the registry below is empty; this harness parametrizes over it, so
the moment a stub lands its row here pins the category, message shape, single-fire
behavior, and documentation URL.
"""

import importlib
import re
import warnings

import pytest

_MESSAGE_PATTERN = re.compile(
    r"^(?P<name>\S+) is deprecated since (?P<version>\S+); "
    r"use (?P<replacement>.+)\. See (?P<url>https://\S+#\S+)$"
)

# One row per deprecated stub: (import_path, symbol_name, call_args).
# Empty in 1.0 (stub-free). Each future deprecation adds its row here.
_DEPRECATED_STUBS: list[tuple[str, str, tuple[object, ...]]] = []


@pytest.mark.parametrize(
    ("import_path", "symbol_name", "call_args"),
    _DEPRECATED_STUBS,
    ids=[f"{path}.{name}" for path, name, _ in _DEPRECATED_STUBS],
)
def test_deprecated_stub_fires_one_well_formed_warning(import_path, symbol_name, call_args):
    module = importlib.import_module(import_path)
    stub = getattr(module, symbol_name)
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        stub(*call_args)
    deprecation_warnings = [w for w in caught if issubclass(w.category, DeprecationWarning)]
    assert len(deprecation_warnings) == 1
    message_text = str(deprecation_warnings[0].message)
    assert _MESSAGE_PATTERN.match(message_text), (
        f"{import_path}.{symbol_name} warning does not match the policy format: {message_text!r}"
    )


def test_message_pattern_accepts_a_policy_conformant_message():
    conformant = (
        "old_name is deprecated since 1.1; use new_name. "
        "See https://edify.readthedocs.io/en/latest/upgrading/1.0-to-1.1.html#new-name"
    )
    assert _MESSAGE_PATTERN.match(conformant)


def test_message_pattern_rejects_a_message_missing_the_docs_url():
    non_conformant = "old_name is deprecated since 1.1; use new_name."
    assert _MESSAGE_PATTERN.match(non_conformant) is None


def test_message_pattern_rejects_a_url_without_an_anchor():
    non_conformant = (
        "old_name is deprecated since 1.1; use new_name. "
        "See https://edify.readthedocs.io/en/latest/upgrading/1.0-to-1.1.html"
    )
    assert _MESSAGE_PATTERN.match(non_conformant) is None


def test_registry_is_empty_or_every_row_has_three_fields():
    for row in _DEPRECATED_STUBS:
        assert len(row) == 3
