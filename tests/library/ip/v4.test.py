from edify.library import ipv4

_TEST_CASES = {
    "192.168.0.1": True,
    "244.232.123.233": True,
    "363.232.123.233": False,
    "234.234234.234.234": False,
    "12.12.12.12.12": False,
    "0.0.0.0": True,
    "987.987.987.987": False,
}


def test_ipv4():
    for candidate, expectation in _TEST_CASES.items():
        assert ipv4(candidate) is expectation
