from edify.library import mac


def test_mac():
    macs = {
        "00:00:5e:00:53:af": True,
        "00:00:5e:00:53:af:": False,
        123: False,
    }

    for m_a_c, expected in macs.items():
        assert mac(m_a_c) == expected
