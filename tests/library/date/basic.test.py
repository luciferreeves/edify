from edify.library import date

_TEST_CASES = {
    "1/1/2020": True,
    "01/01/2020": True,
    "1/01/2020": True,
    "01/1/2020": True,
    "1/1/20": False,
    "01/01/20": False,
    "1/1/202": False,
    "01/01/202": False,
    "12/12/2022": True,
    "12/12/2": False,
    "2021-11-04T22:32:47.142354-10:00": False,
    "2021-11-04T22:32:47.142354Z": False,
    "2021-11-04T22:32:47.142354": False,
    "2021-11-04T22:32:47": False,
    "2021-11-04T22:32": False,
    "2021-11-04T22": False,
    "2021-11-04": False,
    "2021-11": False,
    "2021": False,
    "1-1-2020": False,
}


def test_date():
    for candidate, expectation in _TEST_CASES.items():
        assert date(candidate) is expectation
