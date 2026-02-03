# Queue implementation using Python list with size limit

# Queue class
class Queue:
    def __init__(self, max_size):
        self.items = max_size * [None]
        self.max_size = max_size
        self.start = -1
        self.top = -1
        # time complexity -> O(1)
        # space complexity -> O(n)

    # check if the list is at max capacity
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top == self.max_size - 1:
            return True
        else:
            return False
        # time & space complexity -> O(1)

    # check if the queue is empty
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        # time & space complexity -> O(1)
        
    # add an element to the queue
    def enqueue(self, element):
        if self.isFull():
            return "Queue is at max capacity"
        else:
            if self.top + 1 == self.max_size:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = element
        # time & space complexity -> O(1)

    # remove an element from the queue
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            first_element = self.items[self.start]
            start = self.start

            # if there is only one element in the queue
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.max_size:
                self.start = 0
            else:
                self.start += 1

            self.items[start] = None
            return first_element
        # time & space complexity -> O(1)

    # return the first element without returning it
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.items[self.start]
        # time & space complexity -> O(1)

    # delete the queue
    def delete(self):
        self.items = self.max_size * [None]
        self.start = -1
        self.top = -1
        # time & space complexity -> O(1)

    # print out the queue
    def __str__(self):
        elements = [str(x) for x in self.items]
        return " ".join(elements)
    