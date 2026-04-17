# Binary Heap

A **Binary Heap** is a complete binary tree that satisfies the heap property. It is primarily used to implement **priority queues** and is the foundation for heap sort.

## Why Complete Tree?

The complete tree structure ensures:
- Efficient array storage (no wasted space)
- **O(log n)** insert and delete operations
- Balanced shape for consistent performance
- Cache-friendly memory access

## Key Terminology

- **Complete Tree**: All levels filled except possibly the last, filled left to right
- **Heap Property**: Parent is either greater than or less than children
- **Min Heap**: Smallest element at root (parent ≤ children)
- **Max Heap**: Largest element at root (parent ≥ children)
- **Bubble Up**: Process of restoring heap property after insertion
- **Bubble Down**: Process of restoring heap property after removal (heapify)

## Real-world Examples

- Priority queue implementations
- CPU task scheduling
- Dijkstra's algorithm (with min-heap)
- Finding top-k elements
- Median of data streams

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

## Array Index Formulas (1-based)

For a node at index `i`:

- Left child: `2 * i`
- Right child: `2 * i + 1`
- Parent: `i // 2`

## Key Operations

| Operation | Description | Time Complexity |
|-----------|-------------|-----------------|
| **Insert** | Add to end, then bubble up | O(log n) |
| **Extract Min/Max** | Remove root, replace with last, bubble down | O(log n) |
| **Peek** | View root element | O(1) |
| **Build Heap** | Create heap from array | O(n) |

## Time Complexity

| Operation | Time Complexity |
|-----------|-----------------|
| Insert | O(log n) |
| Extract Min/Max | O(log n) |
| Peek | O(1) |
| Build Heap | O(n) |

## Applications

- Priority queues
- CPU/task scheduling
- Dijkstra's algorithm (with min-heap)
- Heap sort
- Finding kth smallest/largest elements
- Median maintenance
- Top-k streaming elements
