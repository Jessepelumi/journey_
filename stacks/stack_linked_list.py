# Stack data structure using linked list

"""
In a stack implementation using linked list, the head is used as the top of the stack. This allows push and pop operations to be performed in O(1) time, as we can directly access the head without traversing the list.
Using the tail would require traversing the list, resulting in O(n) time complexity for these operations.
"""

# Node class
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        # time & space complexity -> O(1)

# Stack class
class StackLinkedList:
    def __init__(self):
        self.top = None
        self.length = 0

    # add a new element to the top of the stack
    def push(self, val):
        new_node = Node(val)

        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

        self.length += 1
        # time & space complexity -> O(1)

    # remove an element from the top of the stack
    def pop(self):
        if not self.top:
            return "Stack is empty"
        
        popped = self.top
        if not popped.next:
            self.top = None
        else:
            self.top = popped.next
            popped.next = None

        self.length -= 1
        return popped
        # time & space complexity -> O(1)

    # return the topmost element of the stack
    def peek(self):
        if not self.top:
            return "Stack is empty"
        
        return self.top
        # time & space complexity -> O(1)
    
    # check if stack is empty
    def isEmpty(self):
        return self.length == 0
        # time & space complexity -> O(1)
    
    # clear the stack
    def clear(self):
        if self.top:
            self.top = None

        self.length = 0
        # time & space complexity -> O(1)
