

import pytest


@pytest.fixture()
def before():
    print("\nbefore each test")


@pytest.fixture()
def before_2():
    print("\nbefore each test 2")


def test_first_1(before):
    """
    This one will always fail
    :param before:
    :return:
    """
    print("test_1()")
    assert 3 == 5


@pytest.mark.eman
def test_second_2(before):
    """
    test this with pytest -m eman test_fixtures.py
    :param before:
    :return:
    """
    print("test_2()")


@pytest.mark.usefixtures("before_2")
class TestTryMark(object):

    """
    This is one way to group tests with will use same resources
    All tests within these class will use 'before_2' fixture
    No need to add it before each test
    """

    def test_third_3(self):
        print("test_3()")

    def test_fourth_4(self):
        print('test_4()')

    def test_fifth_5(self):
        print('test_5()')


@pytest.mark.eman
def test_sixth_6(before):
    """
    test this with pytest -m eman test_fixtures.py
    :param before: 
    :return: 
    """

    print("test_6()")