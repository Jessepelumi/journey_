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

    def __str__(self):
        temp_node = self.head
        result = ''

        while temp_node is not None:
            result += str(temp_node.data)
            if temp_node.next:
                result += ' -> '

            temp_node = temp_node.next

        return result


# Usage
new_list = SLinkedList()
new_list.append(10)
new_list.append(20)
new_list.append(30)

print(new_list.head.data)
print(new_list.tail.data)
print(new_list.length)
print(new_list)