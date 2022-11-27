from edify.library import ssn


def test_ssn():
    ssns = {
        "000-22-3333": False,
        "100-22-3333": True,
        "": False,
        123: False,
    }
    for s_s_n, expected in ssns.items():
        assert ssn(s_s_n) == expected
