# Node class
class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

"""
Note: AVL Tree is basically a BST, so all the operations performed on a BST can be performed on an AVL Tree. 
"""

def getHeight(node: AVLNode):
    if not node:
        return 0
    return node.height

# Get the balance factor
def getBalance(node: AVLNode):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

# Perform a right rotation

# 1. Create a variable 'new_root' and assign it to the left child of the disbalanced node
# 2. Create another variable 'temp' and assign it to the right child of the left child of the disbalanced node.
# 3. Set the disbalanced node as the right child of the new node.
# 4. Set temp as the left child of the disbalanced node.
# 5. Adjust heights of rotated node and new root
# 6. Return a.

def rightRotation(n: AVLNode):
    new_node = n.left
    temp = new_node.right

    new_node.right = n
    n.left = temp

    # compute heights
    n.height = 1 + max(getHeight(n.left), getHeight(n.right))
    new_node.height = 1 + max(getHeight(new_node.left), getHeight(new_node.right))

    return new_node

# Perform a left notation

# 1. Create a variable 'new_root' and assign it to the right child of the disbalanced node
# 2. Create another variable 'temp' and assign it to the left child of the right child of the disbalanced node
# 3. Set the disbalanced node as the left child of the new node.
# 4. Set temp as the right child of the disbalanced node
# 5. Adjust heights of disbalanced  node and new root
# 6. Return a

def leftRotation(n: AVLNode):
    new_node = n.right
    temp = new_node.left

    new_node.left = n
    n.right = temp

    # compute height
    n.height = 1 + max(getHeight(n.left), getHeight(n.right))
    new_node.height = 1 + max(getHeight(new_node.left), getHeight(new_node.right))

    return new_node

# Insert a node to an AVL Tree

# 1. Insert like a normal BST
# 2. Update heights
# 3. Compute balance factor
# 4. If unbalanced -> perform rotations

# balance factor > 1: left heavy
# balance factor < -1: right heavy

