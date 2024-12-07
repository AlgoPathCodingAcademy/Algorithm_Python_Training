class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
def is_value_in_bst_range(node, low, high):
#TODO

# Create the BST
root = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6)), 
                TreeNode(10, None, TreeNode(14)))
#        8
#       / \
#      3   10
#     / \    \
#    1   6    14

# Check if there exists any value in the range
assert is_value_in_bst_range(root, 5, 9) == True, "Test Case 1 Failed" # Output: True (value 6 is in range)
print("Test Case 1 Passed")
assert is_value_in_bst_range(root, 15, 20) == False, "Test Case 2 Failed"  # Output: False (no value in range)
print("Test Case 2 Passed")
