from edify.library import guid


def test_valid_guids():
    guids = {
        "6ba7b810-9dad-11d1-80b4-00c04fd430c8": True,
        '{51d52cf1-83c9-4f02-b117-703ecb728b74}': True,
        '{51d52cf1-83c9-4f02-b117-703ecb728-b74}': False,
    }
    for guid_string, expectation in guids.items():
        assert guid(guid_string) == expectation
