# Binary Heap

A **Binary Heap** is a complete binary tree that satisfies the heap property. It is primarily used to implement **priority queues**.

## Why Complete Tree?

The complete tree structure ensures the heap can be stored efficiently in an array without wasted space, and enables **O(log n)** insert and delete operations by maintaining a balanced shape.

## Properties

1. **Complete Tree**: All levels filled except possibly the last, which fills left to right. This makes it suitable for array storage.

2. **Heap Property**:
   - **Min Heap**: parent ≤ children (smallest element at root)
   - **Max Heap**: parent ≥ children (largest element at root)

3. **Array Storage**: Typically implemented using an array for cache-friendly access.

## Array Index Formulas (0-based)

For a node at index `i`:

- Left child: `2 * i + 1`
- Right child: `2 * i + 2`
- Parent: `(i - 1) // 2`

## Key Operations

- **Insert**: Add to end, then "bubble up" to maintain heap property — **O(log n)**
- **Extract Min/Max**: Remove root, replace with last element, then "bubble down" — **O(log n)**
- **Peek**: View root element — **O(1)**

## Applications

- Priority queues
- CPU/task scheduling
- Dijkstra's algorithm (with min-heap)
- Heap sort
- Finding kth smallest/largest elements
