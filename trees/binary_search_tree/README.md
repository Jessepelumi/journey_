# Binary Search Tree

A Binary Search Tree (BST) is a binary tree with additional properties such as:

For ant given node N:

- **Left Subtree:** Every node in the left subtree must have a value less than (or equal) to the value of node N.
- **Right Subtree:** Every node in the right subtree must have a value greater than (or equal to) the value of node N.

## A Note on Duplicates:

Standard BST definitions often vary on how they handle equal values:

- **Strict BST:** No duplicates allowed (Left < Parent < Right).
- **Left-leaning Duplicates:** Duplicates go to the left (Left <= Parent < Right). 
- **Right-leaning Duplicates:** Duplicates go to the right (Left < Parent <= Right).