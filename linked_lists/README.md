# Linked List

A **Linked List** is a linear data structure made up of **nodes** connected in a chain. Each node contains data and a reference (pointer) to the next node. Unlike arrays, elements are not stored in contiguous memory locations.

## Why Linked Lists?

- Dynamic size: no need to declare fixed size
- Efficient insertion/deletion: O(1) when position is known
- No memory waste: no pre-allocation needed
- Flexible memory allocation

## Key Terminology

- **Head**: the first node in the list
- **Tail**: the last node, which points to null (or back to head for circular)
- **Node**: a container holding data and a reference
- **Pointer/Reference**: the link to the next (or previous) node
- **Null**: indicates end of list (or None in Python)

## Real-world Examples

- Music playlist (next/previous buttons)
- Browser history (back/forward navigation)
- Image viewer (next/previous image)
- Task scheduling linked list in OS

## Types

### Singly Linked List

Nodes point forward only. Each node has:

- **Data**: the value stored
- **Next**: reference to the next node

### Doubly Linked List

Nodes point both forward and backward. Each node has:

- **Data**: the value stored
- **Next**: reference to the next node
- **Prev**: reference to the previous node

### Circular Linked List

The last node points back to the first, forming a circle. Can be singly or doubly.

## Common Operations

- `append` — add node to the end
- `prepend` — add node to the beginning
- `insert` — add node after a given value
- `delete` — remove node by value
- `search` — find if a value exists
- `print` — display all elements
- `reverse` — reverse the list order
- `get_length` — count number of nodes

## Time Complexity

| Operation | Singly | Doubly |
|-----------|--------|--------|
| Search | O(n) | O(n) |
| Insert at Head | O(1) | O(1) |
| Insert at Tail | O(1)* | O(1)* |
| Delete at Head | O(1) | O(1) |
| Delete at Tail | O(n) | O(1) |

*With tail pointer

## Advantages vs Arrays

| Aspect | Linked List | Array |
|--------|-------------|-------|
| Insertion/Deletion | O(1) | O(n) |
| Random Access | O(n) | O(1) |
| Memory | Dynamic | Fixed |
| Cache Friendly | No | Yes |
