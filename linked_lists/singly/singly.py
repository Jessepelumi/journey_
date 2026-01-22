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

    def search(self, data):
        curr_node = self.head
        curr_index = 0

        while curr_node:
            if curr_node.data == data:
                print(f"{data} was found in the list at index {curr_index}")
                return
            curr_node = curr_node.next
            curr_index += 1

        print(f"{data} was not found in the list")

        # time complexity -> O(n)
        # space complexity -> O(1)

    def get(self, index):
        # empty list check
        if self.length == 0:
            print("This is an empty list")
            return
        
        if index == -1:
            print(f"The tail node's data is {self.tail.data}")
            return self.tail
        
        # invalid index check
        if index < -1 or index >= self.length:
            print("Invalid index")
            return
        
        curr_node = self.head
        for _ in range(index):
            curr_node = curr_node.next

        print(f"The data at index {index} is {curr_node.data}")
        return curr_node
    
        # time complexity -> O(n)
        # space complexity -> O(1)

    # def set_value(self, index, data):
    #     # empty list
    #     if self.length == 0:
    #         print("This list is empty")
    #         return
        
    #     if index == -1:
    #         self.tail.data = data
    #         print(f"tail updated to {self.tail.data}")
    #         return
        
    #     # invalid index
    #     if index < -1 or index >= self.length:
    #         print("Invalid index")
    #         return

    #     curr_node = self.head
    #     for _ in range(index):
    #         curr_node = curr_node.next

    #     curr_node.data = data
    #     print(f"updated to {curr_node.data}")

    #     # time complexity -> O(n)
    #     # space complexity -> O(1)

    # set_value method using get method
    def set_value(self, index, data):
        target_node = self.get(index)

        if target_node:
            target_node.data = data
            print(f"The data at index {index} has been updated to {target_node.data}")
            return

        print("Target node was not found")

        # time complexity -> O(n)
        # space complexity -> O(1)

    def pop_first(self):
        if self.length == 0:
            print("No node popped. This is an empty list")
            return
        
        popped_node = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = popped_node.next
            popped_node = None

        self.length -= 1

        print(popped_node, popped_node.data)

        # time & space complexity -> O(1)

    def pop(self):
        if self.length == 0:
            print("No node popped. This is an empty list")
            return

        popped_node = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            curr_node = self.head

            while curr_node.next is not self.tail:
                curr_node = curr_node.next

            self.tail = curr_node
            curr_node.next = None

        self.length -= 1

        print(popped_node, popped_node.data)

        # time complexity -> O(n)
        # space complexity -> O(1)

    def remove(self, index):
        # if self.length == 0:
        #     print("No node removed. This is an empty list")
        #     return
        
        # # invalid index 
        # if index < 0 or index >= self.length:
        #     print("Invalid index")
        #     return
        
        prev_node = self.get(index - 1)
        if not prev_node:
            return
        
        popped_node = prev_node.next

        if self.length == 1:
            self.head = self.tail = None
        elif popped_node is self.tail:
            self.tail = prev_node
            prev_node.next = None
        else:
            prev_node.next = popped_node.next
            popped_node.next = None

        self.length -= 1

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
# new_list.append(10)
new_list.prepend(20)
# new_list.append(20)
new_list.insert(30, 1)

print(new_list)

# new_list.search(10)

#new_list.set_value(3, 100)

# print(new_list.head.data)
# print(new_list.tail.data)
# print(new_list.length)
#print(new_list)

new_list.remove(0)
#print(new_list.head.data)
print(new_list)
# new_list.transverse()

#new_list.get(-1)