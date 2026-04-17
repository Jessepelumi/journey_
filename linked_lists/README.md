# Linked List

A **Linked List** is a linear data structure made up of **nodes** connected in a chain. Each node contains:

- **Data**: the value stored
- **Pointer/Reference**: a reference to the next node

Linked lists excel at dynamic memory allocation and efficient insertion/deletion (O(1) when position is known).

## Key Terminology

- **Head**: the first node in the list
- **Tail**: the last node, which points to null (or back to head for circular)

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

The last node points back to the first, forming a circle.

## Common Operations

- `append` — add node to the end
- `prepend` — add node to the beginning
- `insert` — add node after a given value
- `delete` — remove node by value
- `search` — find if a value exists
- `print` — display all elements

## Time Complexity

- Search: **O(n)**
- Insert/Delete at head: **O(1)**
- Insert/Delete at tail: **O(1)** (with tail pointer)
