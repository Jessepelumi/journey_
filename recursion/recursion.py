"""
Recursion is a way of solving a problem where a function calls itself, typically with smaller inputs, until it reaches a base case to terminate the process.
A good example is the Russian doll.
"""

# Russian doll example
def russianDoll(doll):
    print(f"Opening doll {doll}")

    if doll == 1:
        print("All dolls have been opened")
    else:
        return russianDoll(doll - 1)
    
# russianDoll(5)

"""
Recursive thinking helps break down big problems into smaller, manageable tasks.
The following things should be considered when choosing recursion: 
- Can the problem be divided into smaller subproblems that are similar to the original problem?
- Does the problem have a clear base case to stop recursion (e.g., `doll == 1`)?
- Can you express the solution in terms of itself (i.e., the function calling itself with smaller inputs)?

Example of recursion problems:
- Design an algorithm to compute nth... 
- Write code to list the n... 
- Implement a method to compute all
"""

# Factorial
# Factorial formula -> n! = n * (n-1) * (n-2) * ... * 2 * 1
# Simplified factorial formula -> n! = n * (n-1)!
def factorial(n):
    assert n >= 0 and int(n) == n, "Positive integers only!"

    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1) # n! = n * (n-1)!
    
print(factorial(-5))
