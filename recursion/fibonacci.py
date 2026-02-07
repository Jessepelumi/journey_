"""
Fibonacci sequence
The implementation of the Fibonacci sequence using recursion calculates the Fibonacci number at a given position, starting from position 0.
The number at the given position is the sum of the numbers at the previous two positions.
"""

def fibonacci(n): # n is the given position
    if not isinstance(n, int) or n < 0:
        raise ValueError("Positive integers only!")

    # base case for termination
    if n in [0, 1]:
        return n
    # recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci("g"))
