## Binary Trees

A binary tree is a hierarchical data structure in which each node has at most two children, typically referred to as the left and right children. It serves as the foundation for several specialized types of trees, including:

- **Binary Search Tree (BST):** A binary tree where the left child of a node contains values smaller than the node, and the right child contains values larger than the node.
- **Heap Tree:** A binary tree used to implement heaps, where the tree satisfies the heap property (either min-heap or max-heap).
- **AVL Tree:** A self-balancing binary search tree where the difference in heights between left and right subtrees is at most one.
- **Red-Black Tree**: A self-balancing binary search tree with additional properties for balancing the tree during insertions and deletions.
- **Syntax Tree:** A tree used in the representation of language syntax, especially in compilers, where nodes represent components of an expression or program.

Binary trees form the basis for various other advanced data structures due to their simplicity and efficiency in organizing data.

Some binary tree operations are:
- **Creation:** Set up an empty tree or initialize it with a root.
- **Insertion:** Add a node at an appropriate location.
- **Deletion:** Remove a node and handle its children accordingly.
- **Search:** Find a node with a specific value.
- **Traversal:** Visit all nodes in a specific order (pre-order, in-order, post-order, or level-order).
- **Deletion of Tree:** Completely remove all nodes from the tree.

Traversing a binary tree:
#### Depth First Search (DFS)
- Preorder: Root Node -> Left Subtree -> Right Subtree
- In-order: Left Subtree -> Root Node -> Right Subtree
- Post-order traversal: Left Subtree -> Right Subtree -> Root Node

#### Breadth First Search (BFS): Level order traversal.
