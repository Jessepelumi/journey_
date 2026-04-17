# Queue

A **Queue** is a linear data structure that follows the **FIFO** (First In First Out) principle — the first element added is the first to be removed. It is an abstract data type that models a line of waiting elements.

## Key Terminology

- **Front**: the position where elements are removed (also called "head")
- **Rear**: the position where elements are added (also called "tail")
- **Enqueue**: operation to add an element
- **Dequeue**: operation to remove an element

## Real-world Examples

- Printer queue: the first document submitted is the first to print
- Customer service call routing
- Task scheduling in operating systems
- Breadth-first search (BFS) in graphs
- Message queues in distributed systems
- Airport security checkpoint line

## Implementations

| Implementation     | Description                                    |
| ------------------ | ---------------------------------------------- |
| **Python Lists**   | Queue without capacity (unbounded)             |
| **Circular Queue** | Queue with fixed capacity (wraps around)       |
| **Linked Lists**   | Dynamic queue implementation                   |
| **Deque**          | Double-ended queue (add/remove from both ends) |

## Common Operations

- `enqueue` (or push) — add an element to the rear
- `dequeue` (or pop) — remove the front element
- `peek` — view the front element without removing it
- `is_empty` — check if the queue is empty
- `is_full` — check if the queue has reached capacity (for bounded queues)
- `size` — return the number of elements

## Time Complexity

| Operation | Time Complexity |
| --------- | --------------- |
| Enqueue   | **O(1)**        |
| Dequeue   | **O(1)**        |
| Peek      | **O(1)**        |
| is_empty  | **O(1)**        |

## Types of Queues

| Type               | Description                                       |
| ------------------ | ------------------------------------------------- |
| **Simple Queue**   | Basic FIFO order                                  |
| **Circular Queue** | Last position connects to first (wraps around)    |
| **Priority Queue** | Elements removed based on priority (not FIFO)     |
| **Deque**          | Double-ended, can add/remove from both ends       |
| **Blocking Queue** | Operations block when empty/full (multithreading) |
