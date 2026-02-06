"""
Factorial formula:
n! = n * (n-1) * (n-2) * ... * 2 * 1
n! = n * (n-1)!
"""

def factorial(n):
    assert n >= 0 and int(n) == n, "Must be a positive integer"
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))