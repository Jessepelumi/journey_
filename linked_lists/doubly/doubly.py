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

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

        # time & space complexity -> O(1)
