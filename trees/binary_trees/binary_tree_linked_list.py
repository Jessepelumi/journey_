# Binary tree implementation using linked lists.

# Tree node class
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None
        # time & space complexity -> O(1)


# Usage
new_tree = TreeNode("Drinks")
hot = TreeNode("Hot")
cold = TreeNode("Cold")
new_tree.left_child = hot
new_tree.right_child = cold

coffee = TreeNode("Coffee")
tea = TreeNode("Tea")
hot.left_child = coffee
hot.right_child = tea

cola = TreeNode("Cola")
pepsi = TreeNode("Pepsi")
cold.left_child = cola
cold.right_child = pepsi

# Pre-order traversal
def preorder_traversal(root_node: TreeNode):
    if not root_node:
        return
    
    print(root_node.val)
    preorder_traversal(root_node.left_child)
    preorder_traversal(root_node.right_child)

    # time complexity - O(n)
    # space complexity -> O(n) -> recursion uses function call stack 

preorder_traversal(new_tree)

# In-order traversal
def inorder_traversal(root_node: TreeNode):
    if not root_node:
        return
    
    inorder_traversal(root_node.left_child)
    print(root_node.val)
    inorder_traversal(root_node.right_child)

    # time complexity -> O(n)
    # space complexity -> O(n) -> recursion uses function call stack

inorder_traversal(new_tree)

# Post-order traversal
def postorder_traversal(root_node: TreeNode):
    if not root_node:
        return
    
    postorder_traversal(root_node.left_child)
    postorder_traversal(root_node.right_child)
    print(root_node.val)

    # time complexity -> O(n)
    # space complexity -> O(n)

postorder_traversal(new_tree)
