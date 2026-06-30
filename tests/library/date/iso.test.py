from edify.library import iso_date

_TEST_CASES = {
    "1/1/2020": False,
    "01/01/2020": False,
    "1/01/2020": False,
    "01/1/2020": False,
    "1/1/20": False,
    "01/01/20": False,
    "1/1/202": False,
    "01/01/202": False,
    "12/12/2022": False,
    "12/12/2": False,
    "2021-11-04T22:32:47.142354-10:00": True,
    "2021-11-04T22:32:47.142354Z": True,
    "2021-11-04T22:32:47.142354": True,
    "2021-11-04T22:32:47": True,
    "2021-11-04T22:32": False,
    "2021-11-04T22": False,
    "2021-11-04": False,
    "2021-11": False,
    "2021": False,
}


def test_iso_date():
    for candidate, expectation in _TEST_CASES.items():
        assert iso_date(candidate) is expectation
