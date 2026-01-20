# Node class
# The node contains 'data' stored and 'pointer/reference' to the next node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # time & space complexity -> O(1)

# List class
# The two major components are the head and tail
class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)

        # first check if the list is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
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
            self.head = new_node

        self.length += 1

        # time & space complexity -> O(1)

    def insert(self, data, index):
        new_node = Node(data)

        # invalid index
        if index < 0 or index > self.length:
            print("Invalid index!")
            return

        # assign new node to head and tail if list is empty
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # insert at the beginning of the list if index is 0
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr_node = self.head
            for _ in range(index - 1):
                curr_node = curr_node.next

            new_node.next = curr_node.next
            curr_node.next = new_node

            # check if new node is the new tail
            if not new_node.next:
                self.tail = new_node

        self.length += 1

        # time complexity -> O(n)
        # space complexity -> O(1)

    def transverse(self):
        curr_node = self.head
        if not self.head:
            print("This list is empty")
            return

        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

        # for loop method
        # for _ in range(self.length):
        #     print(curr_node.data)
        #     curr_node = curr_node.next

        # time complexity -> O(n)
        # space complexity -> O(1)

    def __str__(self):
        temp_node = self.head
        result = ''

        while temp_node:
            result += str(temp_node.data)
            if temp_node.next:
                result += ' -> '

            temp_node = temp_node.next

        return result


# Usage
new_list = SLinkedList()
new_list.append(10)
new_list.append(10)
new_list.append(10)
new_list.prepend(20)
new_list.append(20)
new_list.insert(10, 5)

print(new_list.head.data)
print(new_list.tail.data)
print(new_list.length)
print(new_list)
new_list.transverse()