# Binary Heap

A binary heap is a type of binary tree that satisfies specific structural and ordering properties.

### Properties of a Binary Heap

1. It is a **complete** binary tree
    A binary heap must be a complete binary tree.
        1. Every level of the tree is completely filled 
        2. Except possibly the last level
        3. The last level is filled from left to right.

2. It must follow the **Heap Property**
    A binary tree must satisfy one of the following heap properties.
        1. **Min Heap:** Every parent node is less than or equal to its children -> parent <= children
        2. **Max Heap:** Every parent node is greater than or equal to its children -> parent >= children

3. Stored in an array
    Binary heaps are usually implemented using an array rather than pointers.


### Applications of Binary Heap

Binary heap are commonly used to implement **Priority Queues**. 

Common applications include:
    1. CPU scheduling
    2. Task scheduling
    3. Dijkstra's algorithm
    4. A* pathfinding
    5. Event simulations.

### Array implementation of Binary Heap
When implementing a binary heap using a 0-based index array, the given formula is used:
Left child: 2 * i + 1
Right child: 2 * i + 2
Parent: (i - 1) // 2
    