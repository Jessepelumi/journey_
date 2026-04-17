# Binary Trees

A **Binary Tree** is a hierarchical structure where each node has at most two children (left and right). It serves as the foundation for many specialized data structures.

## Key Properties

- Each node has at most two children
- Used as the basis for BST, heaps, AVL trees, and more

## Specialized Types

| Type               | Description                                      |
| ------------------ | ------------------------------------------------ |
| **BST**            | Left child < parent < right child (ordered)      |
| **Heap**           | Satisfies heap property (min or max at root)     |
| **AVL Tree**       | Self-balancing BST with height constraint        |
| **Red-Black Tree** | Self-balancing BST with color properties         |
| **Syntax Tree**    | Represents program/expression syntax (compilers) |

## Common Operations

- **Create**: initialize an empty tree
- **Insert**: add a node at appropriate location
- **Delete**: remove a node and handle children
- **Search**: find a node with specific value
- **Traversal**: visit all nodes in specific order
- **Delete Tree**: remove all nodes

## Time Complexity

- Search, Insert, Delete: **O(n)** worst case, **O(log n)** balanced

## Traversals

### Depth First Search (DFS)

- **Preorder**: Root → Left → Right (useful for copying trees)
- **Inorder**: Left → Root → Right (gives sorted order for BST)
- **Postorder**: Left → Right → Root (useful for deleting trees)

### Breadth First Search (BFS)

- **Level Order**: visit nodes level by level (uses a queue)
