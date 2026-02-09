# Creating a basic tree

# TreeNode class
class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    def add_child(self, TreeNode):
        self.children.append(TreeNode)

    def __str__(self, level = 0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
# Usage
tree = TreeNode("Drinks", [])
cold = TreeNode("Cold", [])
hot = TreeNode("Hot", [])

tree.add_child(cold)
tree.add_child(hot)

tea = TreeNode("Tea", [])
coffee = TreeNode("Coffee", [])

hot.add_child(tea)
hot.add_child(coffee)

cola = TreeNode("Cola", [])
pepsi = TreeNode("Pepsi", [])

cold.add_child(cola)
cold.add_child(pepsi)

print(tree)
