# Binary Heap implementation using 0-based index array

# Heap class
class Heap:
    def __init__(self, size):
        self.heap_list = size * [None]
        self.heap_size = 0
        self.max_size = size
        # time complexity -> O(1)
        # space complexity -> O(n)

    def peek(self):
        if self.heap_size <= 0:
            return "Heap is empty"
        return self.heap_list[0]

