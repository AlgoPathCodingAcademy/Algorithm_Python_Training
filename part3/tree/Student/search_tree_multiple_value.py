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

def search_all(root,target):
#TODO

# Test Case 1: Multiple matching nodes
#       10
#      /  \
#     7    15
#    / \
#   7   10
tree1 = TreeNode(10, TreeNode(7, TreeNode(7), TreeNode(10)), TreeNode(15))
assert search_all(tree1, 7) == [7, 7],"Test Case 1 Failed"  # All nodes with value 7
print("Test Case 1 Passed")
assert search_all(tree1, 10) == [10, 10], "Test Case 2 Failed"  # All nodes with value 10
print("Test Case 2 Passed")
assert search_all(tree1, 15) == [15], "Test Case 3 Failed"  # Only one node with value 15
print("Test Case 3 Passed")

# Test Case 2: Single node tree
tree2 = TreeNode(8)
assert search_all(tree2, 8) == [8], "Test Case 4 Failed"  # Single matching node
print("Test Case 4 Passed")
assert search_all(tree2, 10) == [], "Test Case 5 Failed"  # No matching nodes
print("Test Case 5 Passed")
# Test Case 3: Tree with no matching values
#       1
#      / \
#     2   3
tree3 = TreeNode(1, TreeNode(2), TreeNode(3))
assert search_all(tree3, 4) == [], "Test Case 6 Failed"  # No matching nodes
print("Test Case 6 Passed")
# Test Case 4: Tree with a mix of values
#       5
#      / \
#     3   5
#    / \
#   2   5
tree4 = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(5)), TreeNode(5))
assert search_all(tree4, 5) == [5, 5, 5], "Test Case 7 Failed"  # All nodes with value 5
print("Test Case 7 Passed")
assert search_all(tree4, 3) == [3], "Test Case 8 Failed"  # Only one node with value 3
print("Test Case 8 Passed")

