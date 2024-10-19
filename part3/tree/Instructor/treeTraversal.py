import sys
import os

# Get the parent directory of the current script
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to the Python path
sys.path.append(parent_dir)

# Now import the treeNode module
from treeNode import TreeNode, create_tree_from_list

'''
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
'''

# Example usage
lst = [1, 2, 3, None, 5, None, 7]
root = create_tree_from_list(lst)

# Function to traverse and print in-order
def inorder_traversal(node):
    if not node:
        return
    inorder_traversal(node.left)
    print(node.value, end=' ')
    inorder_traversal(node.right)

# Print the tree using in-order traversal
print("In-order traversal:")
inorder_traversal(root)
print()

def preorder_traversal(node):
    if not node:
        return
    # Process the root node (print or store the value)
    print(node.value, end=' ')

    # Recursively visit the left subtree
    preorder_traversal(node.left)

    # Recursively visit the right subtree
    preorder_traversal(node.right)

# Pre-order traversal
print("Pre-order traversal:")
preorder_traversal(root)
print()

def postorder_traversal(node):
    if not node:
        return

    # Recursively visit the left subtree
    postorder_traversal(node.left)

    # Recursively visit the right subtree
    postorder_traversal(node.right)

    # Process the root node (print or store the value)
    print(node.value, end=' ')

# Post-order traversal
print("Post-order traversal:")
postorder_traversal(root)
print()
