class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Function to create a tree from a list with `None` values to handle incomplete trees
def create_tree_from_list(lst):
    if not lst or lst[0] is None:
        return None

    # Create the root node
    root = TreeNode(lst[0])
    queue = [root]  # Initialize a queue with the root node

    i = 1  # Index to track list elements
    while i < len(lst):
        current_node = queue.pop(0)  # Get the current node

        # Add left child if not None
        if i < len(lst) and lst[i] is not None:
            current_node.left = TreeNode(lst[i])
            queue.append(current_node.left)
        i += 1

        # Add right child if not None
        if i < len(lst) and lst[i] is not None:
            current_node.right = TreeNode(lst[i])
            queue.append(current_node.right)
        i += 1

    return root
    

def is_valid_bst(root):
    #TODO

# Test cases as lists
test_cases = [
    {"lst": [10, 5, 15, 3, 7, None, 20], "expected": True},  # Valid BST
    {"lst": [10, 5, 15, None, 4, None, 20], "expected": False},  # Invalid BST (4 is on the right of 5)
    {"lst": [0, -10, 10, None, -5], "expected": True},  # Valid BST with negative and positive values
    {"lst": [5], "expected": True},  # Single node (edge case)
    {"lst": [], "expected": True}  # Empty tree (edge case)
]

# Test runner
for i, test in enumerate(test_cases, start=1):
    root = create_tree_from_list(test["lst"])
    result = is_bst(root)
    print(f"Test Case {i}: {'Passed' if result == test['expected'] else 'Failed'}")
