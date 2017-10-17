"""Test fibonacci and lucas functions."""
"""" python -m pytest test_series.py"""

def test_fibonacci():
    """Test fibonacci function."""
    from series import fibonacci
    assert fibonacci(1) == 0
