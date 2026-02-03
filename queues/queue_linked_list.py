# Queue data structure implementation using linked list

# Node class
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        # time & space complexity -> O(1)

# Queue class
class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        # time & space complexity -> O(1)

    # check if the queue is empty
    def is_empty(self):
        if not self.head:
            return True
        else:
            return False
        # time & space complexity -> O(1)

    # add an element to the queue
    def enqueue(self, val):
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        # time & space complexity -> O(1)

    # remove an element from the queue
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            first_element = self.head
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        
        self.length -= 1
        return first_element
        # time & space complexity -> O(1)

    # return the top element of the queue without deleting it
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.head
        # time & space complexity -> O(1)
