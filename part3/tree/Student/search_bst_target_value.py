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

search_bst(root, 7)  # Output: True
search_bst(root, 2)  # Output: False

