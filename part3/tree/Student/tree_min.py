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


def find_min(root):
#TODO

# Test Case 1: Standard tree
#       10
#      /  \
#     5    15
#    / \
#   2   7
tree1 = TreeNode(10, TreeNode(5, TreeNode(2), TreeNode(7)), TreeNode(15))
assert find_min(tree1) == 2, "Test Case 1 Failed"# Smallest value is 2
print("Test Case 1 Passed")

# Test Case 2: Tree with varying depths
#        15
#       /  \
#      10   20
#     / \
#    5   12
tree2 = TreeNode(15, TreeNode(10, TreeNode(5), TreeNode(12)), TreeNode(20))
assert find_min(tree2) == 5, "Test Case 2 Failed" # Smallest value is 5
print("Test Case 2 Passed")

# Test Case 3: Tree with all positive values
#       100
#      /   \
#    50    200
tree3 = TreeNode(100, TreeNode(50), TreeNode(200))
assert find_min(tree3) == 50, "Test Case 3 Failed"  # Smallest value is 50
print("Test Case 3 Passed")

# Test Case 4: Tree with negative and positive values
#       -5
#      /   \
#    -10    0
#    /
#   -15
tree4 = TreeNode(-5, TreeNode(-10, TreeNode(-15)), TreeNode(0))
assert find_min(tree4) == -15, "Test Case 4 Failed"  # Smallest value is -15
print("Test Case 4 Passed")

