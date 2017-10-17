def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

def lucas(n):
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n+1)


def sum_series(n, first=0, second=1):
    return n
