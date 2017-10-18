"""Functions that return the value of a specified number in a sequence."""
"""Fibonacci Sequence"""


def fibonacci(n):
    """Fibonacci sequence function."""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


"""Lucas Sequence"""


def lucas(n):
    """Similar to fibonacci but begins with 2 and 1."""
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n + 1)


"""Modified Sequence which accounts for optional arguments"""


def sum_series(n, first=0, second=1):
    """In addition to n user may specify first two numbers in sequence."""
    for i in range(1, n):
        first, second = second, first + second
    return first


"""Main method"""

if __name__ == "__main__":
    main()
