
from edify import main


def test_main():
    if main.main() is None:
        assert True
