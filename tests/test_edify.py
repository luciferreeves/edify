
from edify import __main__


def test_main():
    if __main__.main() is None:
        assert True
