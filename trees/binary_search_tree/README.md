# Binary Search Tree (BST)

A **BST** is a binary tree where each node follows the ordering property, enabling efficient search. It combines the hierarchical structure of a binary tree with ordered data.

## Why BST?

- Efficient search: O(log n) average case
- Ordered data: inorder traversal gives sorted sequence
- Dynamic size: grows and shrinks as needed
- Supports range queries

## Key Terminology

- **Ordering Property**: left subtree values ≤ node value ≤ right subtree values
- **Successor**: smallest node in right subtree (next larger)
- **Predecessor**: largest node in left subtree (next smaller)
- **Balanced**: height difference between subtrees is minimal
- **Unbalanced**: tree degenerates to linked list (worst case)

## Real-world Examples

- Database indexing
- Symbol tables in compilers
- Dictionary implementations
- File system organization
- Priority queue alternatives

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

| Operation | Description | Average | Worst |
|-----------|-------------|---------|-------|
| **Search** | Find a value | O(log n) | O(n) |
| **Insert** | Add a value | O(log n) | O(n) |
| **Delete** | Remove a node | O(log n) | O(n) |
| **Traversal** | Visit all nodes | O(n) | O(n) |
| **Min** | Find minimum | O(log n) | O(n) |
| **Max** | Find maximum | O(log n) | O(n) |

## Deletion Cases

1. **Leaf node**: simply remove it
2. **One child**: bypass the node (link parent directly to child)
3. **Two children**:
   - Find **successor** (smallest in right subtree) or **predecessor** (largest in left subtree)
   - Replace node's value with successor/predecessor
   - Delete the successor/predecessor (which will be case 1 or 2)

## Worst Case

If the tree becomes unbalanced (e.g., sorted insertion), operations degrade to **O(n)**. Use self-balancing trees (AVL, Red-Black) to maintain O(log n).

## Balanced vs Unbalanced

| Scenario | Tree Shape | Time Complexity |
|----------|------------|-----------------|
| Random insertion | Balanced | O(log n) |
| Sorted insertion | Degenerates to line | O(n) |
| Random deletion | Balanced | O(log n) |

## Advantages

- Fast search (compared to arrays for dynamic data)
- Ordered traversal
- Supports min/max operations
- Flexible size
