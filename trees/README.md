# Tree Data Structure

A **Tree** is a hierarchical (non-linear) data structure with no cycles. It represents parent-child relationships in a branching structure. Unlike linear structures, trees organize data vertically.

## Why Trees?

- Represent hierarchical data naturally
- Efficient search operations (when balanced)
- Model decision-making processes
- Support fast insertion and deletion

## Real-world Examples

- Family tree
- Organizational chart
- File system (folders and files)
- XML/HTML document structure
- Company hierarchy
- Biological classification

## Key Terminology

- **Root**: top node with no parent
- **Edge**: connection between parent and child
- **Leaf**: node with no children (terminal node)
- **Siblings**: nodes sharing the same parent
- **Ancestor**: any predecessor of a node (parent, grandparent, etc.)
- **Descendant**: any node below a given node (child, grandchild, etc.)
- **Subtree**: a node and all its descendants
- **Path**: sequence of edges from one node to another
- **Depth**: number of edges from root to a node
- **Height**: maximum edges from root to any leaf
- **Degree**: number of children a node has
- **Level**: nodes at the same depth (root is level 0)
- **Forest**: a collection of separate trees

## Tree Properties

| Property | Description |
|----------|-------------|
| **Nodes** | Total number of elements |
| **Edges** | Total number of connections (n-1 for connected tree) |
| **Height** | Maximum depth from root to leaf |
| **Degree** | Maximum number of children any node has |

## Types of Trees

| Type | Description |
|------|-------------|
| **Binary Tree** | Each node has at most 2 children |
| **Binary Search Tree** | Ordered binary tree (left < parent < right) |
| **AVL Tree** | Self-balancing BST |
| **B-Tree** | Self-balancing for databases |
| **Trie** | Prefix tree for strings |
| **Heap** | Complete tree with heap property |

## Common Operations

- **Create**: initialize an empty tree
- **Insert**: add a node
- **Delete**: remove a node
- **Search**: find a node
- **Traverse**: visit all nodes
- **Get Height**: calculate tree height
- **Get Size**: count total nodes

## Time Complexity (Balanced Tree)

| Operation | Time Complexity |
|-----------|-----------------|
| Search | O(log n) |
| Insert | O(log n) |
| Delete | O(log n) |
| Traversal | O(n) |
