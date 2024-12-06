def search_tree(root,target)
#TODO

# Test Case 1: Value exists in the tree
#       10
#      /  \
#     7   15
#    / \
#   2   7
tree1 = TreeNode(10, TreeNode(7, TreeNode(2), TreeNode(7)), TreeNode(15))
assert search_tree(tree1, 7) == True  # 7 is present
assert search_tree(tree1, 20) == False  # 20 is not present

# Test Case 2: Single node tree
tree2 = TreeNode(8)
assert search_tree(tree2, 8) == True  # Target matches the node value
assert search_tree(tree2, 10) == False  # Target is not present

# Test Case 3: Tree with values greater than target
#       1
#      / \
#     2   3
tree3 = TreeNode(1, TreeNode(2), TreeNode(3))
assert search_tree(tree3, 4) == False  # 4 is not present
assert search_tree(tree3, 2) == True  # 2 is present

# Test Case 4: Tree with negative and positive values
#       5
#      / \
#    -3   7
#   /  \
# -4   -2
tree4 = TreeNode(5, TreeNode(-3, TreeNode(-4), TreeNode(-2)), TreeNode(7))
assert search_tree(tree4, -3) == True  # -3 is present
assert search_tree(tree4, 0) == False  # 0 is not present
