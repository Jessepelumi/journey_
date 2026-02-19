# Binary Search Tree

A Binary Search Tree (BST) is a binary tree with additional properties such as:

For any given node N:

- **Left Subtree:** Every node in the left subtree must have a value less than (or equal) to the value of node N.
- **Right Subtree:** Every node in the right subtree must have a value greater than (or equal to) the value of node N.

## A Note on Duplicates:

Standard BST definitions often vary on how they handle equal values:

- **Strict BST:** No duplicates allowed (Left < Parent < Right).
- **Left-leaning Duplicates:** Duplicates go to the left (Left <= Parent < Right). 
- **Right-leaning Duplicates:** Duplicates go to the right (Left < Parent <= Right).

## Deleting a Node in a BST:

1. **Leaf Node:** If the node to be deleted has no children, simply remove it from the tree.
2. **Node with One Child:** If the node to be deleted has only one child, bypass the node by linking its parent directly to the child.
3. **Node with Two Children:** If the node to be deleted has two children:
    - Find the successor (the smallest node in the right subtree) or predecessor (the largest node in the left subtree).
    - Replace the node with the successor/predecessor.
    - Delete the successor/predecessor node, which will now be in one of the first two cases (leaf or one child).