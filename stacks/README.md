# Stack

A **Stack** is a linear data structure that follows **LIFO** (Last In First Out) — the last element added is the first to be removed. Think of it as a stack of plates: you add to the top and remove from the top.

## Key Terminology

- **Top**: the most recently added element (where operations happen)
- **Bottom**: the base of the stack (first element added)
- **Push**: operation to add an element
- **Pop**: operation to remove an element
- **Overflow**: attempt to push when stack is full
- **Underflow**: attempt to pop when stack is empty

## Real-world Examples

- Browser history: the back button returns to the most recently visited page
- Undo/redo functionality in editors
- Function call stack in programming languages
- Stack of books on a desk
- Recursive function execution
- Expression evaluation (infix to postfix)

## Implementations

| Implementation | Description |
|----------------|-------------|
| **Python Lists** | Array-based stack (push/pop at end) |
| **Linked Lists** | Pointer-based stack (push/pop at head) |

## Common Operations

- `push` — add an element to the top
- `pop` — remove the top element
- `peek` — view the top element without removing it
- `is_empty` — check if the stack is empty
- `size` — return the number of elements
- `clear` — remove all elements

## Time Complexity

| Operation | Time Complexity |
|-----------|-----------------|
| Push | **O(1)** |
| Pop | **O(1)** |
| Peek | **O(1)** |
| is_empty | **O(1)** |

## Stack Applications

- Function call management (recursion)
- Expression evaluation and syntax parsing
- Undo/Redo mechanisms
- Backtracking algorithms
- Memory management
- Browser history navigation
- Tower of Hanoi problem
