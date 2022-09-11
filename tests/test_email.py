from edify.library import email
from edify.library import email_rfc_5322

emails = [
        "email@example.com",
        "email@192.168.0.1",
        "firstname.lastname@example.com",
        "email@subdomain.example.com",
        "firstname+lastname@example.com",
        "1234567890@example.com",
        "email@example-one.com",
        "_______@example.com",
        "email@example.museum",
        "firstname-lastname@example.com",
        "email@example.com.",
        "plainaddress",
        "#@%^%#$@#$@#.com",
        "@example.com",
        "Joe Smith <email@example.com>",
        "email.example.com",
        "email@example@example.com",
        ".email@example.com",
        "email.@example.com",
        "email..email@example.com",
        "あいうえお@example.com",
        "email@-example.com",
        "Abc..123@example.com"
]


def test_email():

    expectations = [
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False
    ]
    for i in range(len(emails)):
        assert email(emails[i]) == expectations[i]


def test_email_rfc_5322():
    expectations = [
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False
    ]
    for i in range(len(emails)):
        assert email_rfc_5322(emails[i]) == expectations[i]
