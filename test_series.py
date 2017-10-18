"""Test for Fibonacci Sequence."""
import pytest


def test_fibonacci_base_case():
    """Test fibonacci function base case. We're starting from n(1) = 0."""
    from series import fibonacci
    assert fibonacci(1) == 0


def test_fibonacci_first_index():
    """Test fibonacci function for n = 2."""
    from series import fibonacci
    assert fibonacci(2) == 1


def test_fibonacci_n_4():
    """Test fibonacci function for n = 4. The fourth fibonacci number is 2."""
    from series import fibonacci
    assert fibonacci(4) == 2


def test_fibonacci_n_10():
    """Test n = 10. Tenth number is 34."""
    from series import fibonacci
    assert fibonacci(10) == 34


def test_fibonacci_type_error():
    """Test n = string."""
    from series import fibonacci
    with pytest.raises(TypeError):
        fibonacci('string')

"""Test for Lucas."""


def test_lucas_base_case():
    """Test Lucas base case, beginning with n 1 == 2."""
    from series import lucas
    assert lucas(1) == 2


def test_lucas_first_index():
    """Test Lucas function for n = 2."""
    from series import lucas
    assert lucas(2) == 1


def test_lucas_n_4():
    """Test Lucas n 4. Fourth number in Lucas sequence is 4."""
    from series import lucas
    assert lucas(4) == 4


def test_lucas_n_8():
    """Test lucas function for n = 8. Result should be 29."""
    from series import lucas
    assert lucas(8) == 29

"""Test for Sum Series."""


def test_sum_series_base_case():
    """Test for no first and second arguments passed. Default to fibonacci."""
    from series import sum_series
    assert sum_series(1) == 0


def test_sum_series_lucas():
    """Test if Lucas numbers are selected."""
    from series import sum_series
    assert sum_series(8, 2, 1) == 29


def test_sum_series_other():
    """Test for iterative alternate series."""
    from series import sum_series
    assert sum_series(5, 3, 5) == 21


def test_sum_series_other740():
    """Test for n 7 with first 4 and second 9."""
    from series import sum_series
    assert sum_series(7, 4, 0) == 20


def test_sum_series_0():
    """Test for n 0. Should return 0."""
    from series import sum_series
    assert sum_series(0) == 0
