# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # time & space complexity -> O(1)

# Linked list class
class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

        # time & space complexity -> O(1)

    def append(self, data):
        new_node = Node(data)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node

        self.length += 1

        # time & space complexity -> O(n)

    def prepend(self, data):
        new_node = Node(data)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node

        self.length += 1

        # time & space complexity -> O(1)

    def __str__(self):
        if self.length == 0:
            return "Empty list"

        temp_node = self.head
        result = []

        while temp_node:
            result.append(str(temp_node.data))
            if temp_node.next is self.head:
                break

            temp_node = temp_node.next
            
        return " -> ".join(result) + " -> (back to head)"


# Usage
new_list = CSLinkedList()

new_list.append(10)
new_list.prepend(90)

print(new_list)