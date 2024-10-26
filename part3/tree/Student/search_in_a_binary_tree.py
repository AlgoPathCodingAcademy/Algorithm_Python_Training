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
    
def searchBST(root, val):
    #TODO
    
def test_searchBST():
    # Define test cases with expected outputs
    test_cases = [
        {
            "description": "Find node 2 in a balanced BST",
            "tree": [4, 2, 7, 1, 3],
            "value": 2,
            "expected": [2, 1, 3]  # Expected subtree rooted at node with value 2
        },
        {
            "description": "Find node 5 in right-skewed BST",
            "tree": [1, None, 2, None, 3, None, 4, None, 5],
            "value": 5,
            "expected": [5]  # Expected subtree rooted at node with value 5
        },
        {
            "description": "Value not present in BST",
            "tree": [4, 2, 7, 1, 3],
            "value": 5,
            "expected": None  # Expected result is None since 5 is not in the tree
        },
        {
            "description": "Find root node",
            "tree": [4, 2, 7, 1, 3],
            "value": 4,
            "expected": [4, 2, 7, 1, 3]  # Expected subtree rooted at node with value 4
        },
        {
            "description": "Find leaf node",
            "tree": [4, 2, 7, 1, 3],
            "value": 3,
            "expected": [3]  # Expected subtree rooted at node with value 3
        }
    ]
    
    def tree_to_list(root):
        # Helper function to convert a tree to list (level order) for comparison
        if not root:
            return None
        result, queue = [], [root]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.value)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        # Remove trailing Nones for cleaner comparison
        while result and result[-1] is None:
            result.pop()
        return result

    # Run each test case
    for case in test_cases:
        root = create_tree_from_list(case["tree"])
        result_tree = searchBST(root, case["value"])
        result = tree_to_list(result_tree)
        expected = case["expected"]
        
        if result == expected:
            print(f"PASSED: {case['description']}")
        else:
            print(f"FAILED: {case['description']}")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")

# Run the tests
test_searchBST()
