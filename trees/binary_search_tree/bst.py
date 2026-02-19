# LeetCode style definition
# class LTreeNode:
#     def __init__(self, val, left = None, right = None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

# BST node
class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# insert a node to the tree
def insert_node(root: BSTNode, val):
    # if the tree is empty
    if root is None:
        return BSTNode(val)
    
    if val < root.val:
        root.left = insert_node(root.left, val)
    else:
        root.right = insert_node(root.right, val)
    
    return root
    # time and space complexity -> O(log n) (halfed input)

# traversing a BST
# DFS traversal
def preorder(root: BSTNode):
    if root is None:
        return
    
    print(root.val)
    preorder(root.left)
    preorder(root.right)
    # time & space complexity -> O(n)

def inorder(root: BSTNode):
    if root is None:
        return
    
    inorder(root.left)
    print(root.val)
    inorder(root.right)
    # time & space complexity -> O(n)

def postorder(root: BSTNode):
    if root is None:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.val)
    # time & space complexity -> O(n)

# BFS traversal
def levelorder(root: BSTNode):
    if root is None:
        return
    
    # custom queue
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        print(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    # time & space complixity -> O(n)

# search for a node 
def search(root: BSTNode, target: BSTNode):
    current = root

    while current:
        if target.val == current.val:
            return current
        
        if target.val < current.val:
            current = target.left # ignore right and traverse through left subtree
        else:
            current = target.right # ignore left and traverse through right subtree

    return None # when not found
    # time & space complexity -> O(log n)

# delete a node
# Note: check README for detailed explanation.

# find min value
# to find min val, traverse through the left part of the tree 
def find_min(root: BSTNode):
    current = root

    while current.left:
        current = current.left
    return root

def delete(root: BSTNode, key):
    if not root:
        return None
    
    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        # leaf node
        if not root.left and not root.right:
            return None
        
        # node has one child
        elif not root.left:
            return root.right
        elif not root.right:
            return root.left
        
        # node has two children
        else:
            temp = find_min(root)
            root.val = temp.val
            root.right = delete(root.right, temp.val)

    return root
    # time & space complexity -> O(n)

