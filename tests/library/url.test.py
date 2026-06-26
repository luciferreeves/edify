import pytest

from edify.library import url

_URLS = [
    "example.com",
    "www.example.com",
    "www.example.com/path/to/file",
    "http://www.example.com",
    "http://example.com",
    "http://www.example.com/path/to/page",
    "https://example.com",
    "https://www.example.com/",
    "https://www.example.com/path/to/page",
    "//example.com",
]


def test_all_protocols():
    match_list = ["proto", "no_proto"]
    expected = [True] * 9 + [False]
    for uri, expectation in zip(_URLS, expected, strict=True):
        assert url(uri, match=match_list) is expectation


def test_proto_only():
    match_list = ["proto"]
    expected = [False] * 3 + [True] * 6 + [False]
    for uri, expectation in zip(_URLS, expected, strict=True):
        assert url(uri, match=match_list) is expectation


def test_no_proto_only():
    match_list = ["no_proto"]
    expected = [True] * 3 + [False] * 7
    for uri, expectation in zip(_URLS, expected, strict=True):
        assert url(uri, match=match_list) is expectation


def test_invalid_protocol():
    for uri in _URLS:
        with pytest.raises(ValueError, match="Invalid protocol"):
            url(uri, match=["invalid"])


def test_invalid_match_type():
    for uri in _URLS:
        with pytest.raises(TypeError, match="must be a list"):
            url(uri, match="invalid")


def test_empty_match_list():
    for uri in _URLS:
        with pytest.raises(ValueError, match="must not be empty"):
            url(uri, match=[])
