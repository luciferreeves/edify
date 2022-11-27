from edify.library import password


def test_password():
    assert password("password") is False
    assert password("Password123!") is True
    assert password("Password123!", max_length=8) is False
    assert password("Password123!", min_upper=2) is False
    assert password("password", min_upper=0, min_digit=0, min_special=0) is True
    assert password("pass@#1", min_special=1, special_chars="!", min_digit=0, min_upper=0, min_length=4) is False
