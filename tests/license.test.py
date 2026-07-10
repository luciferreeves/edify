"""Acceptance tests pinning the license shape recorded in the installed edify metadata."""

from importlib.metadata import metadata


def test_installed_edify_metadata_declares_mit_license_expression():
    edify_metadata = metadata("edify")
    license_expression = edify_metadata.get("License-Expression")
    assert license_expression == "MIT"


def test_installed_edify_metadata_carries_no_apache_license_classifier():
    edify_metadata = metadata("edify")
    classifiers = edify_metadata.get_all("Classifier") or []
    apache_classifiers = [c for c in classifiers if "Apache" in c]
    assert apache_classifiers == []
