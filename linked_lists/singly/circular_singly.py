# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked list class
class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0