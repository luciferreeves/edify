from edify.library import url

urls = [
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
    for uri, expectation in zip(urls, expected):
        assert url(uri, match=match_list) == expectation


def test_proto_only():
    match_list = ["proto"]
    expected = [False] * 3 + [True] * 6 + [False]
    for uri, expectation in zip(urls, expected):
        print(uri, expectation)
        assert url(uri, match=match_list) == expectation


def test_no_proto_only():
    match_list = ["no_proto"]
    expected = [True] * 3 + [False] * 7
    for uri, expectation in zip(urls, expected):
        assert url(uri, match=match_list) == expectation


def test_invalid_protocol():
    match_list = ["invalid"]
    for uri in urls:
        try:
            url(uri, match=match_list)
        except ValueError:
            assert True


def test_invalid_match_type():
    match_list = "invalid"
    for uri in urls:
        try:
            url(uri, match=match_list)
        except TypeError:
            assert True


def test_empty_match_list():
    match_list = []
    for uri in urls:
        try:
            url(uri, match=match_list)
        except ValueError:
            assert True
