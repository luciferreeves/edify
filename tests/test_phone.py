from edify.library import phone_number


def test():
    phones = {
        "1234567890": True,
        "123 456 7890": True,
        "123-456-7890": True,
        "123.456.7890": True,
        "123 456 7890": True,
        "+1 (123) 456-7890": True,
        "+1 (123) 456 7890": True,
        "+1-(123)-456-7890": True,
        "+102 (123) 456-7890": True,
        "+91 (123) 456-7890": True,
        "90122121": True,
        "12345678901": True,
        "+1 (124) 232": True,
        "+1 (123) 45-890": True,
        "+1 (1) 456-7890": True,
        "9012": True,
        "911": True,
        "+1 (615) 243-": False
    }
    for phone, expectation in phones.items():
        assert phone_number(phone) == expectation
