import pytest
import maths_func


"""
Testing add_func with different parameters
 1) using multiple calls with different parameters
 2) using parameterised decorator
"""


def test_add_func_add_integers():
    """
    Testing add_func for integers
    :return:
    """
    assert maths_func.add_func(5, 7) == 12


def test_add_func_add_strings():
    """
        Testing add_func for strings
        :return:
        """
    assert maths_func.add_func("Hello", " World") == "Hello World"


def test_add_func_add_floats():
    """
    Testing add_func for floats
    :return:
    """
    assert maths_func.add_func(20.5, 10.25) == 30.75


@pytest.mark.parametrize('arg1, arg2, result',
                         [(5, 7, 12),
                          ("Hello", " World", "Hello World"),
                          (20.5, 10.25, 30.75)])
def test_add_func(arg1, arg2, result):
    """
    This is testing add_func using one call with different parameters
    :param arg1:
    :param arg2:
    :param result:
    :return:
    """
    assert maths_func.add_func(arg1, arg2) == result
