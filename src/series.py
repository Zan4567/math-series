def fibonacci(n):
    '''return the nth number in the fibonacci series, starting from 1:1.'''
    if n <= 0: return 0
    if n == 1: return 1

    total = 1
    prev = 0
    for i in range (n - 1):
        temp = total
        total = total + prev
        prev = temp

    return total

def lucas(n):
    '''return the nth number in the lucas series, starting from 1:1.'''
    if n <= 0: return 0
    if n == 1: return 2

    total = 1
    prev = 2
    for i in range (n - 2):
        temp = total
        total = total + prev
        prev = temp

    return total

def sum_series(n, first = 1, second = 1):
    '''return the nth number in the lucas series, starting from 1:1.'''
    if n <= 0: return 0
    if n == 1: return first

    total = second
    prev = first
    for i in range (n - 2):
        temp = total
        total = total + prev
        prev = temp

    return total
