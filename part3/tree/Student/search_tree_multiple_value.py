def search_all(root,target):
#TODO

# Test Case 1: Multiple matching nodes
#       10
#      /  \
#     7    15
#    / \
#   7   10
tree1 = TreeNode(10, TreeNode(7, TreeNode(7), TreeNode(10)), TreeNode(15))
assert search_all(tree1, 7) == [7, 7]  # All nodes with value 7
assert search_all(tree1, 10) == [10, 10]  # All nodes with value 10
assert search_all(tree1, 15) == [15]  # Only one node with value 15

# Test Case 2: Single node tree
tree2 = TreeNode(8)
assert search_all(tree2, 8) == [8]  # Single matching node
assert search_all(tree2, 10) == []  # No matching nodes

# Test Case 3: Tree with no matching values
#       1
#      / \
#     2   3
tree3 = TreeNode(1, TreeNode(2), TreeNode(3))
assert search_all(tree3, 4) == []  # No matching nodes

# Test Case 4: Tree with a mix of values
#       5
#      / \
#     3   5
#    / \
#   2   5
tree4 = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(5)), TreeNode(5))
assert search_all(tree4, 5) == [5, 5, 5, 5]  # All nodes with value 5
assert search_all(tree4, 3) == [3]  # Only one node with value 3

