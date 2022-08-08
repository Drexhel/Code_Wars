import itertools
def fib(n, j=0, t=1):
    if n == 0:
        return 0
    for i in itertools.repeat(None,abs(n)-1):
        t, j = t + j, t
    if n > 0 or n % 2 != 0:
        return t
    else:
        return -t