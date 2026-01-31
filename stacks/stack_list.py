# Stack data structure using Python list

"""
In a stack implementation using Python list, the end of the list is used as the top of the stack. This allows push and pop operations to be performed in O(1) time, as append and pop operations on the end of the list are O(1) operations.
Using the beginning of the list would require traversing the entire list, resulting in O(n) time complexity for these operations.
"""

# Stack class
class Stack:
    def __init__(self):
        self.items = []

    # add an element to the top of the stack
    def push(self, element):
        self.items.append(element)
        # time complexity -> O(1)
        # space complexity -> O(1)

    # remove the topmost element from the stack
    def pop(self):
        if len(self.items) == 0:
            return "Stack is empty"
        return self.items.pop() 
    
    # time complexity -> O(1)
    # space complexity -> O(1)
    
    # return the last inserted element without removing it
    def peek(self):
        if len(self.items) == 0:
            return "Stack is empty"
        return self.items[len(self.items) - 1]
        # return self.items[-1]
        # time complexity -> O(1)
        # space complexity -> O(1)

    # returns the length of the stack
    def size(self):
        return len(self.items)
    
        # time complexity -> O(1)
        # space complexity -> O(1)

    
    # clear the stack
    def clear(self):
        self.items = []

        # time complexity -> O(1)
        # space complexity -> O(1)
    
    # print out the stack in a readable format
    def __str__(self):
        if len(self.items) == 0:
            return "Stack is empty"
        
        elements = [str(x) for x in reversed(self.items)]
        return "\n".join(elements)
    
    # time complexity -> O(n)
    # space complexity -> O(n)


# Usage
new_stack = Stack()

new_stack.push(10)
new_stack.push(20)
new_stack.push(30)

new_stack.clear()

print(new_stack)