# Binary Search Tree (BST)

A **BST** is a binary tree where each node follows the ordering property, enabling efficient search.

## Ordering Property

For any node with value `N`:

- **Left subtree**: all values ≤ N
- **Right subtree**: all values ≥ N

This allows O(log n) average-case search by eliminating half the remaining tree at each step.

## Duplicates

Different implementations handle duplicates differently:

- **Strict BST**: no duplicates allowed (Left < Parent < Right)
- **Left-leaning**: duplicates go left (Left ≤ Parent < Right)
- **Right-leaning**: duplicates go right (Left < Parent ≤ Right)

## Common Operations

- **Search**: find a value — O(log n) average, O(n) worst
- **Insert**: add a value while maintaining order — O(log n) average
- **Delete**: remove a node — O(log n) average

## Deletion Cases

1. **Leaf node**: simply remove it
2. **One child**: bypass the node (link parent directly to child)
3. **Two children**:
   - Find **successor** (smallest in right subtree) or **predecessor** (largest in left subtree)
   - Replace node's value with successor/predecessor
   - Delete the successor/predecessor (which will be case 1 or 2)

## Worst Case

If the tree becomes unbalanced (e.g., sorted insertion), operations degrade to **O(n)**. Use self-balancing trees (AVL, Red-Black) to maintain O(log n).
