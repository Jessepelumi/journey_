"""
Recursion is a way of solving a problem by having a function call itself.
A good example is the Russian doll.
"""

# Russina doll example
def russianDoll(doll):
    print(doll)

    if doll == 1:
        print("All dolls have been opened")
    else:
        return russianDoll(doll - 1)
    
russianDoll(5)
