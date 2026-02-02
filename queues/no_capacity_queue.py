# Queue data structure using Python list

# Queue class
class Queue:
    def __init__(self):
        self.items = []

    # check if the queue is empty
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
        # time & space complexity - O(1)

    # add an element to the queue
    def enqueue(self, element):
        self.items.append(element)
        # time & space complexity -> O(1)

    # remove the first element of the queue
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.items.pop(0)
        # time complexity -> O(n)
        # space complexity -> O(1)

    # check the first element in the queue
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.items[0]
        # time & space complexity -> O(1)

    # clear the queue/delete all the elements of the queue
    def delete_all(self):
        self.items = None
        # time & space complexity -> O(1)

    # print out the queue
    def __str__(self):
        elements = [str(x) for x in self.items]
        return " ".join(elements)
    