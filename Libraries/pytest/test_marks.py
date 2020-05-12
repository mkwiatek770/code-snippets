import pytest


@pytest.mark.integration
def test_1():
    print("This is integration test")


def test_2():
    print("This is normal one")