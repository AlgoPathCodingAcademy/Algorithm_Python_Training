def is_value_in_range_bst(root,low,high,target):
#TODO

# BST structure:
#       15
#      /  \
#     10   20
#    / \
#   5  12

root = TreeNode(15, TreeNode(10, TreeNode(5), TreeNode(12)), TreeNode(20))

is_value_in_range_bst(root, 5, 15, 12)  # Output: True
is_value_in_range_bst(root, 10, 20, 5)  # Output: False

