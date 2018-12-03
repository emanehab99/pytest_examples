import pytest

'''

'''

@pytest.fixture()
def resource():
    """
    Fixtures  instantiate a resource only when needed. if tests doesn't use a resource, setup and teardown won't be executed
    Default fixture scope is 'function'. setup and teardown script will run for every test
    :return:
    """

    print('setup resource')
    yield "resource"
    print('teardown resource')


@pytest.fixture(scope='class')
def resource2():
    """
    Fixture scope is 'class'. Setup and teardown script will run once within Class scope
    regardless of number of tests within class
    :return:
    """

    print('setup resource2')
    yield "resource2"
    print('teardown resource2')


class TestYield(object):

    def test_resource(self, resource):
        """
        this will setup and teardown resource every test
        :param resource:
        :return:
        """

        print("testing {}".format(resource))

    def test_resource2_first_method(self, resource2):
        """
        Instantiates resource2 for the first time in Class scope
        :param resource2:
        :return:
        """
        print("testing {}".format(resource2))

    def test(self, resource2):
        """
        This shouldn't instantiate resource2 again within class
        :param resource2:
        :return:
        """
        print("testing {}".format(resource2))