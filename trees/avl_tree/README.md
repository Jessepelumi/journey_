# AVL Tree

An **AVL Tree** is a self-balancing Binary Search Tree that maintains O(log n) worst-case time for all operations by ensuring the height difference between left and right subtrees is at most 1 for every node. Named after inventors Adelson-Velsky and Landis.

## Why AVL Trees?

- Guarantees O(log n) for all operations
- Prevents worst-case O(n) degradation of regular BST
- Automatic balancing through rotations
- Efficient for frequent searches and updates

## Key Terminology

- **Balance Factor**: height(left) - height(right)
- **Left-Heavy**: balance factor > 1
- **Right-Heavy**: balance factor < -1
- **Rotation**: operation to restore balance
- **Rebalancing**: process of restoring AVL property

## Real-world Examples

- Database indexing with frequent updates
- Memory management systems
- Symbol table management in compilers
- Associative arrays with high update frequency

## Balance Factor

`balance_factor = height(left) - height(right)`

- **Valid values**: -1, 0, 1 (balanced)
- **> 1**: left-heavy → right rotation needed
- **< -1**: right-heavy → left rotation needed

## When Rotations Are Needed

### Single Rotations

| Rotation | Trigger | Description |
|----------|---------|-------------|
| **Right Rotation** | Left-left imbalance | Left child is heavy |
| **Left Rotation** | Right-right imbalance | Right child is heavy |

### Double Rotations

| Rotation | Trigger | Description |
|----------|---------|-------------|
| **Left-Right (LR)** | Left-right imbalance | Left child's right subtree is heavy |
| **Right-Left (RL)** | Right-left imbalance | Right child's left subtree is heavy |

## Time Complexity

| Operation | Time Complexity |
|-----------|-----------------|
| Search | O(log n) |
| Insert | O(log n) |
| Delete | O(log n) |
| Get Height | O(1) |

## vs Regular BST

| Aspect | Regular BST | AVL Tree |
|--------|-------------|----------|
| Worst Case | O(n) | O(log n) |
| Average Case | O(log n) | O(log n) |
| Memory | Lower | Higher (height tracking) |
| Insert/Delete | Faster | Slightly slower (rotations) |

## Insertion Process

1. Perform standard BST insertion
2. Update heights along the path
3. Check balance factor at each ancestor
4. Perform rotations if needed (bottom-up)

## Deletion Process

1. Perform standard BST deletion
2. Update heights along the path
3. Check balance factor at each ancestor
4. Perform rotations if needed (may propagate up)

## Advantages

- Guaranteed O(log n) performance
- Self-balancing
- Efficient for large datasets
- Predictable performance

## Limitations

- More overhead than regular BST
- Slightly more memory per node
- Rotations add complexity
