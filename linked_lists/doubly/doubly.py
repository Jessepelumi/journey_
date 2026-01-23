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

    def prepend(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1

        # time & space complexity -> O(1)

    def transversal(self):
        curr_node = self.head

        if not self.head:
            print("This is an empty list")
            return

        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

        # time complexity -> O(n)
        # space complexity -> O(1)

    def __str__(self):
        if not self.head:
            return "Empty list"

        temp_node = self.head
        result = []

        while temp_node:
            result.append(str(temp_node.data))
            temp_node = temp_node.next

        return " <-> ".join(result) + " -> (None)"
    

# Usage
new_list = DLinkedList()

new_list.append(10)
new_list.append(20)
new_list.append(30)

print(new_list)
