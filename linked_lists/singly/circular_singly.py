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

    def insert(self, data, index):
        # empty list
        # invalid index
        # insertion into the first position
        # insertion into the last position

        new_node = Node(data)

        if index < 0 or index > self.length:
            print("Invalid index")
            return
        
        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        else:
            curr_node = self.head
            for _ in range(index - 1):
                curr_node = curr_node.next

            new_node.next = curr_node.next
            curr_node.next = new_node

            if new_node.next is self.head:
                self.tail = new_node

        self.length += 1

        # time complexity -> O(n)
        # space complexity -> O(1)

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

new_list.insert(30, 0)

print(new_list)
print(new_list.head.data)