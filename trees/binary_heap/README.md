# Binary Heap

A binary heap is a type of binary tree that satisfies specific structural and ordering properties.

### Properties of a Binary Heap

1. It is a **complete** binary tree
    A binary heap must be a complete binary tree.
        - Every level of the tree is completely filled 
        - Except possibly the last level
        - The last level is filled from left to right.

2. It must follow the **Heap Property**
    A binary tree must satisfy one of the following heap properties.
        - **Min Heap:** Every parent node is less than or equal to its children -> parent <= children
        - **Max Heap:** Every parent node is greater than or equal to its children -> parent >= children

3. Stored in an array
    Binary heaps are usually implemented using an array rather than pointers.


### Applications of Binary Heap

Binary heap are commonly used to implement **Priority Queues**. 

Common applications include:
    - CPU scheduling
    - Task scheduling
    - Dijkstra's algorithm
    - A* pathfinding
    - Event simulations.
    