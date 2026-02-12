# Binary tree implementation using linked lists.

# Queue linked list to implement level order traversal
import helper_queue as hq

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

# preorder_traversal(new_tree)

# In-order traversal
def inorder_traversal(root_node: TreeNode):
    if not root_node:
        return
    
    inorder_traversal(root_node.left_child)
    print(root_node.val)
    inorder_traversal(root_node.right_child)

    # time complexity -> O(n)
    # space complexity -> O(n) -> recursion uses function call stack

# inorder_traversal(new_tree)

# Post-order traversal
def postorder_traversal(root_node: TreeNode):
    if not root_node:
        return
    
    postorder_traversal(root_node.left_child)
    postorder_traversal(root_node.right_child)
    print(root_node.val)

    # time complexity -> O(n)
    # space complexity -> O(n)

# postorder_traversal(new_tree)

# Level-order traversal
def levelOrderTraversal(root_node: TreeNode):
    if not root_node:
        return
    else:
        custom_queue = hq.HelperQueue()
        custom_queue.enqueue(root_node)

        while not(custom_queue.isEmpty()):
            # return root
            root = custom_queue.dequeue()
            print(root.val.val)

            # check left child
            if root.val.left_child:
                custom_queue.enqueue(root.val.left_child)

            # check right child
            if root.val.right_child:
                custom_queue.enqueue(root.val.right_child)

    # time complexity -> O(n)
    # space complexity -> O(n) -> because of the custom queue

# levelOrderTraversal(new_tree)

# search for a value
def searchBt(root_node: TreeNode, node_val):
    if not root_node:
        return
    else:
        custom_queue = hq.HelperQueue()
        custom_queue.enqueue(root_node)

        while not(custom_queue.isEmpty()):
            root = custom_queue.dequeue()
            if root.val.val == node_val:
                return "Success! -> " + root.val.val
            
            if root.val.left_child:
                custom_queue.enqueue(root.val.left_child)
            if root.val.right_child:
                custom_queue.enqueue(root.val.right_child)

        return node_val + " not found"
    
    # time & space complexity -> O(n)
        
# print(searchBt(new_tree, "Col"))

# insert a new node
# this function inserts the new node into the first available child node, not a specific or targetted node
def insertNodeBT(root_node, new_node):
    if not root_node:
        root_node = new_node
    else:
        custom_queue = hq.HelperQueue()
        custom_queue.enqueue(root_node)
        while not(custom_queue.isEmpty()):
            root = custom_queue.dequeue()
            if root.val.left_child:
                custom_queue.enqueue(root.val.left_child)
            else:
                root.val.left_child = new_node
                return "Inserted successfully"

            if root.val.right_child:
                custom_queue.enqueue(root.val.right_child)
            else:
                root.val.right_child = new_node
                return "Inserted successfully"
            
        # time & space complexity -> O(n)

new_node = TreeNode("Fanta")
# insertNodeBT(new_tree, new_node)
# preorder_traversal(new_tree)

# this inserts a new node to a specific or targeted node
def insert_target_node(root_node: TreeNode, new_node: TreeNode, target_node):
    if not root_node:
        root_node = new_node
    else:
        custom_queue = hq.HelperQueue()
        custom_queue.enqueue(root_node)

        while not custom_queue.isEmpty():
            root = custom_queue.dequeue()

            # check if target node was found
            if root.val == target_node:
                if not root.val.left_child:
                    root.val.left_child = new_node
                elif not root.val.right_child:
                    root.val.right_child = new_node
                else:
                    return "Node already balanced"
                return "Inserted successfully"

            # continue with traversal
            if root.val.left_child:
                custom_queue.enqueue(root.val.left_child)

            if root.val.right_child:
                custom_queue.enqueue(root.val.right_child)

        return "Target node not found"
    # time & space complexity -> O(n)
    
# print(insert_target_node(new_tree, new_node, pepsi))
# preorder_traversal(new_tree)
    
# delete a node
"""
Ordinary Binary Tree Deletion (Summary):
For an ordinary binary tree, the order of nodes does not matter, so deletion does not need to preserve parent-child identity. Instead, we focus on preserving the shape of the tree, particularly its level-order balance.

To delete a node:
- Find the deepest node in the tree.
- Replace the value of the target node with the value of the deepest node.
- Remove the deepest node from the tree.

This ensures the tree remains compact and connected, while sacrificing the original parental links of the target node.
"""
# get deepest node (level order traversal)
def getDeepestNode(root_node: TreeNode):
    if not root_node:
        return
    
    custom_queue = hq.HelperQueue()
    custom_queue.enqueue(root_node)

    while not custom_queue.isEmpty():
        root = custom_queue.dequeue()
        
        if root.val.left_child:
            custom_queue.enqueue(root.val.left_child)

        if root.val.right_child:
            custom_queue.enqueue(root.val.right_child)
        
    deepest_node = root.val
    return deepest_node

# delete deepest node
def deleteDeepestNode(root_node: TreeNode, deepest_node: TreeNode):
    if not root_node:
        return
    
    custom_queue = hq.HelperQueue()
    custom_queue.enqueue(root_node)

    while not custom_queue.isEmpty():
        root = custom_queue.dequeue()

        if root.val == deepest_node:
            root.val.left_child = None
            root.val.right_child = None

        # continue traversal
        if root.val.left_child:
            custom_queue.enqueue(root.val.left_child)
        if root.val.right_child:
            custom_queue.enqueue(root.val.right_child)

# print(getDeepestNode(new_tree))

def delete_node(new_node: TreeNode, target_node: TreeNode):
    pass

# print(insert_target_node(new_tree, new_node, cola))
# levelOrderTraversal(new_tree)

print(insert_target_node(new_tree, new_node, cola))
levelOrderTraversal(new_tree)

deleteDeepestNode(new_tree, getDeepestNode(new_tree))
levelOrderTraversal(new_tree)
