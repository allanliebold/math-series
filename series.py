"""Functions that return the value of a specified number in a sequence."""
"""Fibonacci Sequence"""


def fibonacci(n):
    """Fibonacci sequence function."""
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


"""Lucas Sequence"""


def lucas(n):
    """Similar to fibonacci but begins with 2 and 1."""
    if n == 0:
        return 0
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n + 1)


"""Modified Sequence which accounts for optional arguments"""


def sum_series(n, first=0, second=1):
    """In addition to n user may specify first two numbers in sequence."""
    if n == 0:
        return 0
    else:
        for i in range(1, n):
            first, second = second, first + second
        return first


"""Main method"""

if __name__ == "__main__":
    msg_fib = """
    This module defines functions that implement mathematical series.
    ...
    fibonacci(n):
        Returns the nth value in the Fibonacci series.
    >>> fibonacci(2)
    {}
    """.format(fibonacci(2))
    print(msg_fib)
    msg_lucas = """
    lucas(n):
        Returns the nth value in the Lucas series.
    >>> lucas(8)
    {}
    """.format(lucas(8))
    print(msg_lucas)
    msg_sum = """
    sum_series(n, first=0, second=1):
        Returns the nth value in a series with user specified first and second
        values. If not provided these default to 0 and 1, respectively.
    >>> sum_series(5, 4, 6)
    {}
    """.format(sum_series(5, 4, 6))
    print(msg_sum)
