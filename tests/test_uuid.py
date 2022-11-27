from edify.library import uuid

uuids = {
    "123e4567-e89b-12d3-a456-426614174000": True,
    "123e456-789b-12d3-426614174000": False,
    "123e456-789b-12d3-a456-426614174000-12ad3r": False,
    "123e456": False,
}


def test_valid_uuids():
    for uuid_string, expectation in uuids.items():
        assert uuid(uuid_string) == expectation
