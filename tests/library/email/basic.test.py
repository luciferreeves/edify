from edify.library import email

_TEST_CASES = [
    ("email@example.com", True),
    ("email@192.168.0.1", True),
    ("firstname.lastname@example.com", True),
    ("email@subdomain.example.com", True),
    ("firstname+lastname@example.com", True),
    ("1234567890@example.com", True),
    ("email@example-one.com", True),
    ("_______@example.com", True),
    ("email@example.museum", True),
    ("firstname-lastname@example.com", True),
    ("email@example.com.", False),
    ("plainaddress", False),
    ("#@%^%#$@#$@#.com", False),
    ("@example.com", False),
    ("Joe Smith <email@example.com>", False),
    ("email.example.com", False),
    ("email@example@example.com", False),
    (".email@example.com", False),
    ("email.@example.com", False),
    ("email..email@example.com", False),
    ("あいうえお@example.com", False),
    ("email@-example.com", False),
    ("Abc..123@example.com", False),
]


def test_email():
    for candidate, expectation in _TEST_CASES:
        assert email(candidate) is expectation
