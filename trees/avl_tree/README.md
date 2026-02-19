# AVL Tree

An AVL Tree is a self-balancing Binary Search Tree (BST) where the difference between heights of left and right subtress cannot be more than one for all nodes. It ensures that the tree remains balanced, which helps with maintaining an efficient time complexity for operations like search, insert, and delete.

## Key Properties of an AVL Tree:
1. **Balanced Tree Condition:**
    - For every node in the tree, the difference between the heights of the left and right subtrees is at most 1. This difference is called the balance factor.
    - Balance Factor = height(left subtree) - height(right subtree)
    - A balance factor of:
        - -1, 0, or 1 means the node is balanced.
        - > 1 means the left subtree is taller than the right, which requires a right rotation.
        - < -1 means the right subtree is taller than the left, which requires a left rotation.

2. Balancing after Insertions and Deletions:
    - Inserting or deleting a node can disturb the balance of the tree, but an AVL Tree will perform rotations to restore balance.
    - The following rotations are used:
        - **Right Rotation (Single):** Used when the left subtree of a node is too tall.
        - **Left Rotation (Single):** Used when the right subtree of a node is too tall.
        - **Left-Right Rotation (Double):** Used when the left subtree is too tall, but the right child of the left subtree is too tall.
        - **Right-Left Rotation (Double):** Used when the right subtree is too tall, but the left child of the right subtree is too tall.

3. Time Complexity:
    Due to the balanced nature of the tree, operations like insertion, deletion, and searching all have a time complexity of O(log n), where n is the number of nodes in the tree.