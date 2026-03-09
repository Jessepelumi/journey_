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

# 1. Create a variable 'a' and assign it to the left child of the node to be rotated
# 2. Create another variable 'b' and assign it to the right child of the left child of the node to be rotated.
# 3. Set the rotated node as the right child of a.
# 4. Set b as the left child of the rotated node.
# 5. Adjust heights of rotated node and new root
# 6. Return a.

def rightRotation(n: AVLNode):
    a = n.left
    b = a.right

    a.right = n
    n.left = b

    n.height = 1 + max(getHeight(n.left), getHeight(n.right))
    a.height = 1 + max(getHeight(a.left), getHeight(a.right))

    return a

# Perform a left notation

# 1. Create a variable 'a' and assign it to the right child of the node to be rotated
# 2. Create another variable 'b' and assign it to the left child of the right child of the node to be rotated
# 3. Set the rotated node as the left child of a.
# 4. Set b as the right child of the rotated node
# 5. Adjust heights of rotated node and new root
# 6. Return a

def leftRotation(n: AVLNode):
    a = n.right
    b = a.left

    a.left = n
    n.right = b

    n.height = 1 + max(getHeight(n.left), getHeight(n.right))
    a.height = 1 + max(getHeight(a.left), getHeight(a.right))

    return a

# Insert a node to an AVL Tree

# 1. Insert like a normal BST
# 2. Update heights
# 3. Compute balance factor
# 4. If unbalanced -> perform rotations

# balance factor > 1: left heavy
# balance factor < -1: right heavy

