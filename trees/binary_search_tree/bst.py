# LeetCode style definition
# class LTreeNode:
#     def __init__(self, val, left = None, right = None):
#         self.val = val
#         self.left = left
#         self.right = right

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

