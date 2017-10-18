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
