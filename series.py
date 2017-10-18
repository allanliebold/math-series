"""Fibonacci Sequence"""


def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

"""Lucas Sequence"""


def lucas(n):
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n+1)


"""Modified Sequence which accounts for optional arguments"""


def sum_series(n, first=0, second=1):

    if first ==0 and second == 1:
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
