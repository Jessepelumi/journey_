# AVL Tree

An **AVL Tree** is a self-balancing Binary Search Tree that maintains O(log n) worst-case time for all operations by ensuring the height difference between left and right subtrees is at most 1 for every node.

## Balance Factor

`balance_factor = height(left) - height(right)`

- **Valid values**: -1, 0, 1 (balanced)
- **> 1**: left-heavy → right rotation needed
- **< -1**: right-heavy → left rotation needed

## When Rotations Are Needed

### Single Rotations

- **Right Rotation**: Left-left imbalance (left child is heavy)
- **Left Rotation**: Right-right imbalance (right child is heavy)

### Double Rotations

- **Left-Right (LR)**: Left-right imbalance (left child's right subtree is heavy)
- **Right-Left (RL)**: Right-left imbalance (right child's left subtree is heavy)

## Time Complexity

All operations: **O(log n)** — guaranteed due to self-balancing

## vs Regular BST

Unlike regular BST which can degrade to O(n) with sorted input, AVL trees guarantee balanced height, ensuring consistent performance.
