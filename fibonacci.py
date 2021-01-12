def fib(n):
    ''' return the nth number in the fibonacci sequence'''
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(8))
help(fib)