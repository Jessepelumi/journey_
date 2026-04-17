# Binary Trees

A **Binary Tree** is a hierarchical structure where each node has at most two children (left and right). It serves as the foundation for many specialized data structures and algorithms.

## Why Binary Trees?

- Simple structure with powerful applications
- Foundation for search trees and heaps
- Efficient for hierarchical data representation
- Supports various traversal strategies

## Key Terminology

- **Root**: topmost node of the tree
- **Left Child**: the left descendant of a node
- **Right Child**: the right descendant of a node
- **Subtree**: a node and all its descendants
- **Full Binary Tree**: every node has 0 or 2 children
- **Complete Binary Tree**: all levels filled except possibly last
- **Perfect Binary Tree**: all internal nodes have 2 children, all leaves at same level

## Real-world Examples

- Decision trees in machine learning
- Expression trees in compilers
- Huffman coding trees
- Binary space partitioning
- Family tree diagrams

## Key Properties

- Each node has at most two children
- Used as the basis for BST, heaps, AVL trees, and more
- Height can range from O(log n) to O(n)

## Specialized Types

| Type                | Description                                      |
| ------------------- | ------------------------------------------------ |
| **BST**             | Left child < parent < right child (ordered)      |
| **Heap**            | Satisfies heap property (min or max at root)     |
| **AVL Tree**        | Self-balancing BST with height constraint        |
| **Red-Black Tree**  | Self-balancing BST with color properties         |
| **Syntax Tree**     | Represents program/expression syntax (compilers) |
| **Expression Tree** | Represents mathematical expressions              |
| **Trie**            | Prefix tree for string operations                |

## Common Operations

| Operation       | Description                        |
| --------------- | ---------------------------------- |
| **Create**      | Initialize an empty tree           |
| **Insert**      | Add a node at appropriate location |
| **Delete**      | Remove a node and handle children  |
| **Search**      | Find a node with specific value    |
| **Traversal**   | Visit all nodes in specific order  |
| **Get Height**  | Calculate tree height              |
| **Get Size**    | Count total nodes                  |
| **Delete Tree** | Remove all nodes                   |

## Time Complexity

| Operation | Worst Case | Balanced Case |
| --------- | ---------- | ------------- |
| Search    | O(n)       | O(log n)      |
| Insert    | O(n)       | O(log n)      |
| Delete    | O(n)       | O(log n)      |
| Traversal | O(n)       | O(n)          |

## Traversals

### Depth First Search (DFS)

| Type          | Order               | Use Case                            |
| ------------- | ------------------- | ----------------------------------- |
| **Preorder**  | Root → Left → Right | Copying trees, prefix expressions   |
| **Inorder**   | Left → Root → Right | BST sorted output                   |
| **Postorder** | Left → Right → Root | Deleting trees, postfix expressions |

### Breadth First Search (BFS)

- **Level Order**: visit nodes level by level (uses a queue)
- Useful for finding shortest path in unweighted trees

## Special Binary Trees

| Type                | Definition                                                |
| ------------------- | --------------------------------------------------------- |
| **Full Tree**       | Every node has 0 or 2 children                            |
| **Complete Tree**   | All levels filled except possibly last                    |
| **Perfect Tree**    | All internal nodes have 2 children, all leaves same level |
| **Degenerate Tree** | Each node has only 1 child (like linked list)             |
