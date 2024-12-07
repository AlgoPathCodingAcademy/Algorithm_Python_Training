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


def search_tree(root,target):
    if root == None:
        return False
        
    left_result = search_tree(root.left,target)
    right_result = search_tree(root.right,target)
    
    if root.value == target:
        return True
    else:
        return left_result or right_result
#TODO

# Test Case 1: Value exists in the tree
#       10
#      /  \
#     7   15
#    / \
#   2   7
tree1 = TreeNode(10, TreeNode(7, TreeNode(2), TreeNode(7)), TreeNode(15))
#check_tree(tree1)
assert search_tree(tree1, 7) == True, "Test Case 1 Failed"  # 7 is present
print("Test Case 1 Passed")
assert search_tree(tree1, 20) == False, "Test Case 2 Failed"  # 20 is not present
print("Test Case 2 Passed")

# Test Case 2: Single node tree
tree2 = TreeNode(8)
assert search_tree(tree2, 8) == True, "Test Case 3 Failed"  # Target matches the node value
print("Test Case 3 Passed")
assert search_tree(tree2, 10) == False, "Test Case 4 Failed"  # Target is not present
print("Test Case 4 Passed")
# Test Case 3: Tree with values greater than target
#       1
#      / \
#     2   3
tree3 = TreeNode(1, TreeNode(2), TreeNode(3))
assert search_tree(tree3, 4) == False, "Test Case 5 Failed"  # 4 is not present
print("Test Case 5 Passed")
assert search_tree(tree3, 2) == True, "Test Case 6 Failed"  # 2 is present
print("Test Case 6 Passed")
# Test Case 4: Tree with negative and positive values
#       5
#      / \
#    -3   7
#   /  \
# -4   -2
tree4 = TreeNode(5, TreeNode(-3, TreeNode(-4), TreeNode(-2)), TreeNode(7))
assert search_tree(tree4, -3) == True, "Test Case 7 Failed"  # -3 is present
print("Test Case 7 Passed")
assert search_tree(tree4, 0) == False, "Test Case 8 Failed"  # 0 is not present
print("Test Case 8 Passed")