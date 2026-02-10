# Helper queue

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class HelperQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        if not self.head:
            return True
        else:
            return False
        
    def enqueue(self, val):
        new_node = Node(val)

        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            node = self.head
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next

        self.length -= 1
        return node
    