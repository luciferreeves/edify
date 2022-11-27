from edify.library import password

def test_password():
    assert password("password") == False
    assert password("Password123!") == True
    assert password("Password123!", max_length=8) == False
    assert password("Password123!", min_upper=2) == False
    assert password("password", min_upper=0, min_digit=0, min_special=0) == True
    assert password("pass@#1", min_special=1, special_chars="!", min_digit=0, min_upper=0, min_length=4) == False
