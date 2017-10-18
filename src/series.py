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
    '''return the nth number in the lucas series, starting from 1:2.'''
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
    '''return the nth number in a series where the first two values are provided (default is fibonacci).'''
    if n <= 0: return 0
    if n == 1: return first

    total = second
    prev = first
    for i in range (n - 2):
        temp = total
        total = total + prev
        prev = temp

    return total

if __name__ == "__main__":
    print("This module implements functions that calculate mathematical series.")
    print("The module includes the Fibonacci sequence, the Lucas sequence, and custom sequences based on them.")
    print("")
    print("fibonacci(n): returns the nth value in the fibonacci series")
    print("")
    print("fibonacci(2)")
    print(fibonacci(2))
    print("fibonacci(3)")
    print(fibonacci(3))
    print("fibonacci(4)")
    print(fibonacci(4))
    print("fibonacci(5)")
    print(fibonacci(5))
    print("")
    print("lucas(n): returns the nth value in the fibonacci series")
    print("")
    print("lucas(1)")
    print(lucas(1))
    print("lucas(2)")
    print(lucas(2))
    print("lucas(3)")
    print(lucas(3))
    print("lucas(4)")
    print(lucas(4))
    print("lucas(5)")
    print(lucas(5))
    print("")
    print("sum_series(n, first, second): returns the nth value of a custom sequence.")
    print("similar to the Fibonacci sequence and starting with the values of 'first' and 'second'.")
    print("")
    print("sum_series(4, 2, 2)")
    print(sum_series(4, 2, 2))
    print("sum_series(4, 1, 6)")
    print(sum_series(4, 1, 6))
    print("sum_series(6, 10, 5)")
    print(sum_series(6, 10, 5))
