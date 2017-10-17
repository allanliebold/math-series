"""Test fibonacci and lucas functions."""
import pytest
"""" python -m pytest test_series.py"""
''''Tests for Fibonacci Sequence'''

def test_fibonacci_base_case():
    """Test fibonacci function base case. We're starting from n(1) = 0."""
    from series import fibonacci
    assert fibonacci(1) == 0


def test_fibonacci_first_index():
    """Test fibonacci function for n = 2."""
    from series import fibonacci
    assert fibonacci(2) == 1


def test_fibonacci_n_4():
    """Test fibonacci function for n = 5. The fifth fibonacci number is 3."""
    from series import fibonacci
    assert fibonacci(4) == 2


def test_fibonacci_n_10():
    """Test n = 10. Tenth number is 55."""
    from series import fibonacci
    assert fibonacci(10) == 34


def test_fibonacci_type_error():
    """Test n = string."""
    from series import fibonacci
    with pytest.raises(TypeError):
        fibonacci('string')

'''Tests for Lucas'''

def test_lucas_base_case():
    from series import lucas
    assert lucas(1) == 2

def test_lucas_first_index():
    from series import lucas
    assert lucas(2) == 1 

def test_lucas_n_4():
    from series import lucas
    assert lucas(4) == 4

def test_lucas_n_8():
    from series import lucas
    assert lucas(8) == 29

"""Tests for Sum Series"""

def test_sum_series_base_case():
    from series import sum_series
    assert sum_series(1) == 0

def test_sum_series_lucas():
    from series import sum_series
    assert sum_series(8, 2, 1) == 29
