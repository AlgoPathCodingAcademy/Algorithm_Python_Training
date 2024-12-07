class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        """
        Initialize a TreeNode.
        :param value: The value of the node.
        :param left: Reference to the left child node (default is None).
        :param right: Reference to the right child node (default is None).
        """
        self.value = value
        self.left = left
        self.right = right

def search_bst(root,target):
#TODO

# BST structure:
#       8
#      / \
#     3   10
#    / \    \
#   1   6    14
#      / \   /
#     4   7 13

root = TreeNode(8)
root.left = TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7)))
root.right = TreeNode(10, None, TreeNode(14, TreeNode(13)))

assert search_bst(root, 7) == True, "Test Case 1 Failed"   # Output: True
print("Test Case 1 Passed")
assert search_bst(root, 2) == False, "Test Case 2 Failed"  # Output: False
print("Test Case 2 Passed")
