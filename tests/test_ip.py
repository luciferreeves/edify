from edify.library import ipv4
from edify.library import ipv6

# Generate ipv4 dictionary
ipv4_dict = {
    "192.168.0.1": True,
    "244.232.123.233": True,
    "363.232.123.233": False,
    "234.234234.234.234": False,
    "12.12.12.12.12": False,
    "0.0.0.0": True,
    "987.987.987.987": False,
}

# Generate ipv6 dictionary
ipv6_dict = {
    "2001:0db8:85a3:0000:0000:8a2e:0370:7334": True,
    "2001:db8:85a3:0:0:8a2e:370:7334": True,
    "2001:db8:85a3::8a2e:370:7334": True,
    "2001:db8:85a3:0:0:8A2E:370:7334": True,
    "2001:db8:85a3:0:0:8a2e:370:7334:": False,
    "2001:db8:85a3:0:0:8a2e:370:7334:7334": False,
    "2001:db8:85a3:0:0:8a2e:370:7334:7334:7334": False,
    "2001:db8:85a3:0:0:8a2e:370:7334:7334:7334:7334": False,
}


def test_ipv4():
    for ip, expectation in ipv4_dict.items():
        assert ipv4(ip) == expectation


def test_ipv6():
    for ip, expectation in ipv6_dict.items():
        assert ipv6(ip) == expectation
