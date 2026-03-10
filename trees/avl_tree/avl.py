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
    # time & space complexity -> O(1)

# Get the balance factor
def getBalance(node: AVLNode):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)
    # time & space complexity -> O(1)

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
    # time & space complexity -> O(1)

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
    # time & complexity -> O(1)

# Insert a node to an AVL Tree

# 1. Insert like a normal BST
# 2. Update heights
# 3. Compute balance factor
# 4. If unbalanced -> perform rotations

# balance factor > 1: left heavy
# balance factor < -1: right heavy

def insertNode(root: AVLNode, val):
    # Empty tree
    if not root:
        return AVLNode(val)
    
    if val < root.val:
        root.left = insertNode(root.left, val) # O(log n)
    else:
        root.right = insertNode(root.right, val) # O(log n)

    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    balance = getBalance(root)

    # Perform rotations based on balance factor
    # Left-Left condition
    if balance > 1 and val < root.left.val:
        return rightRotation(root)
    
    # Right-Right condition
    if balance < -1 and val > root.right.val:
        return leftRotation(root)
    
    # Left-Right condition
    if balance > 1 and val > root.left.val:
        root.left = leftRotation(root.left)
        return rightRotation(root)
    
    # Right-Left condition
    if balance < -1 and val < root.right.val:
        root.right = rightRotation(root.right)
        return leftRotation(root)

    return root

    # time & space complexity -> O(log n)

# find minimum value
def getMin(root: AVLNode):
    current = root

    while current.left:
        current = current.left
    return root 

def deleteNode(root: AVLNode, key):
    if not root:
        return None
    
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        
        temp = getMin(root)
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val)

    # update height of current node
    root.height = 1 + max(getHeight(root.left), getHeight(root.right))

    # balance factor
    balance = getBalance(root)

    # left-left condition -> right rotation
    if balance > 1 and getBalance(root.left) >= 0:
        return rightRotation(root)

    # right-right condition
    if balance < -1 and getBalance(root.right) <= 0:
        return leftRotation(root)

    # left-right condition
    if balance > 1 and getBalance(root.left) <= 0:
        root.left = leftRotation(root.left)
        return rightRotation(root)
    
    # right-left condition
    if balance < -1 and getBalance(root.right) >= 0:
        root.right = rightRotation(root.right)
        return leftRotation(root)
    
    return root


