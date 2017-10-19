"""Test for Math Series functions."""
import pytest
from series import fibonacci, lucas, sum_series

fib_data = [(0, "Invalid Input"), (1, 0), (2, 1), (3, 1), (4, 2), (5, 3),
            (6, 5), (7, 8), (8, 13), (9, 21), (10, 34)]

lucas_data = [(0, "Invalid Input"), (1, 2), (2, 1), (3, 3), (4, 4), (5, 7),
              (6, 11), (7, 18), (8, 29), (9, 47), (10, 76)]

sum_data = [(0, 9, 6, "Invalid Input"), (1, 0, 1, 0), (8, 2, 1, 29),
            (5, 3, 5, 21), (7, 4, 0, 20), (10, 5, 2, 173)]


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
    """Test Sum Series function with above."""
    assert sum_series(arg, first, second) == expected
