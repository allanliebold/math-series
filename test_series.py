"""Test for Math Series functions."""
import pytest
from series import fibonacci, lucas, sum_series

fib_data = [
    """Arguments and expected results for Fibonacci tests."""
    (0, 0),
    (1, 0),
    (2, 1),
    (4, 2),
    (10, 34)
]

lucas_data = [
    """Arguments and expected results for Lucas tests."""
    (0, 0),
    (1, 2),
    (2, 1),
    (4, 4),
    (8, 29)
]

sum_data = [
    """Arguments and expected results for Sum Series tests."""
    (0, 9, 6, 0),
    (1, 0, 1, 0),
    (8, 2, 1, 29),
    (5, 3, 5, 21),
    (7, 4, 0, 20)
]


@pytest.mark.parametrize("arg,expected", fib_data)
def test_fibonacci(arg, expected):
    """Test Fibonacci function using above parameters."""
    assert fibonacci(arg) == expected


def test_fibonacci_type_error():
    """Test n = string, should raise a TypeError."""
    with pytest.raises(TypeError):
        fibonacci('string')


@pytest.mark.parametrize("arg,expected", lucas_data)
def test_lucas(arg, expected):
    """Test Lucas function with above parameters."""
    assert lucas(arg) == expected


@pytest.mark.parametrize("arg,first,second,expected", sum_data)
def test_sum_series(arg, first, second, expected):
    """Test Sum Series function with above parameters."""
    assert sum_series(arg, first, second) == expected
