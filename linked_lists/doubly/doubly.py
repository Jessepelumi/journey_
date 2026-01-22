# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    # time & space complexity -> O(1)

# Linked list class
class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
