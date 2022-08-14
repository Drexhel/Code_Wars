def fib(n):
    if n > 0 or n % 2 != 0:
        return fibn(abs(n))
    else:
        return -fibn(abs(n))
def fibn(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 0:
        n1 = fib(n/2)
        n2 = fib((n/2)-1)

        result = n1 ** 2 + (n1 * 2 * n2)
        return result
    else:
        n1 = fib((n+1) / 2)
        n2 = fib((n-1) / 2)

        result = n1 ** 2 + (n2 ** 2)
        return result
