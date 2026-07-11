from edify.library import ip

def test_valid_ipv4():
    assert ip("192.168.1.1")

def test_valid_ipv6():
    assert ip("2001:db8::1")

def test_bad_ip():
    assert not ip("999.999.999.999")
