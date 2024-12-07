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


def get_total(root):
#TODO

# Test Case 1: Standard tree
#       10
#      /  \
#     5    15
#    / \
#   2   7
tree1 = TreeNode(10, TreeNode(5, TreeNode(2), TreeNode(7)), TreeNode(15))
assert get_total(tree1) == 39, "Test Case 1 Failed"# Sum: 10 + 5 + 15 + 2 + 7 = 39
print("Test Case 1 Passed")

# Test Case 2: Tree with large values
#       100
#      /   \
#    50    200
tree2 = TreeNode(100, TreeNode(50), TreeNode(200))
assert get_total(tree2) == 350, "Test Case 2 Failed"  # Sum: 100 + 50 + 200 = 350
print("Test Case 2 Passed")

# Test Case 3: Tree with mixed positive and negative values
#       -10
#      /   \
#     5    -15
#    /
#   20
tree3 = TreeNode(-10, TreeNode(5, TreeNode(20)), TreeNode(-15))
assert get_total(tree3) == 0, "Test Case 3 Failed"  # Sum: -10 + 5 + 20 - 15 = 0
print("Test Case 3 Passed")

# Test Case 4: Single node tree
tree4 = TreeNode(8)
assert get_total(tree4) == 8, "Test Case 4 Failed"  # Sum is 8, as there is only one node
print("Test Case 4 Passed")