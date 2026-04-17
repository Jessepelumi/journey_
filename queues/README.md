# Queue

A **Queue** is a linear data structure that follows the **FIFO** (First In First Out) principle — the first element added is the first to be removed.

## Key Terminology

- **Front**: the position where elements are removed
- **Rear**: the position where elements are added

## Real-world Examples

- Printer queue: the first document submitted is the first to print
- Customer service call routing
- Task scheduling in operating systems

## Implementations

- **Python Lists**: Queue without capacity and circular queue (with capacity)
- **Linked Lists**: Dynamic queue implementation

## Common Operations

- `enqueue` (or push) — add an element to the rear
- `dequeue` (or pop) — remove the front element
- `peek` — view the front element without removing it
- `is_empty` — check if the queue is empty
- `is_full` — check if the queue has reached capacity (for bounded queues)

## Time Complexity

- All operations: **O(1)**
