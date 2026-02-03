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

    # print out the queue
    def __str__(self):
        elements = [str(x) for x in self.items]
        return " ".join(elements)