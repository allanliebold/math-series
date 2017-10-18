"""Functions that return the value of a specified number in a sequence."""


def fibonacci(n):
    """Fibonacci sequence function."""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


def lucas(n):
    """Similar to fibonacci but begins with 2 and 1."""
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n + 1)


def sum_series(n, first=0, second=1):
    """In addition to n user may specify first two numbers in sequence."""
    if first == 0 and second == 1:
        return fibonacci(n)
    elif first == 2 and second == 1:
        return lucas(n)
    else:
        for i in range(1, n):
            first, second = second, first + second
        return first


"""Main method"""

if __name__ == "__main__":
    main()