"""Test fibonacci and lucas functions."""
"""" python -m pytest test_series.py"""


def test_fibonacci_base_case():
    """Test fibonacci function base case."""
    from series import fibonacci
    assert fibonacci(1) == 0


def test_fibonacci_first_index():
    """Test fibonacci function for n = 2."""
    from series import fibonacci
    assert fibonacci(2) == 1


def test_fibonacci_n_5():
    """Test fibonacci function for n = 5. The fifth fibonacci number is 3."""
    from series import fibonacci
    assert fibonacci(4) == 2
