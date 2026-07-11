from edify.library import postal


def test_valid_postal():
    assert postal("12345")


def test_bad_postal():
    assert not postal("nope-!!!")
