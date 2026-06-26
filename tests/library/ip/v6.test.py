from edify.library import ipv6

_TEST_CASES = {
    "2001:0db8:85a3:0000:0000:8a2e:0370:7334": True,
    "2001:db8:85a3:0:0:8a2e:370:7334": True,
    "2001:db8:85a3::8a2e:370:7334": True,
    "2001:db8:85a3:0:0:8A2E:370:7334": True,
    "2001:db8:85a3:0:0:8a2e:370:7334:": False,
    "2001:db8:85a3:0:0:8a2e:370:7334:7334": False,
    "2001:db8:85a3:0:0:8a2e:370:7334:7334:7334": False,
    "2001:db8:85a3:0:0:8a2e:370:7334:7334:7334:7334": False,
}


def test_ipv6():
    for candidate, expectation in _TEST_CASES.items():
        assert ipv6(candidate) is expectation
