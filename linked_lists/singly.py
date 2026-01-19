# Node class
# The node contains 'data' stored and 'pointer/reference' to the next node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# List class
# The two major components are the head and tail
class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)

        # first check if the list is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1