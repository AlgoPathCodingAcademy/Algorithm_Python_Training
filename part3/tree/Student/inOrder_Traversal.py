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

# Example usage
lst = [1, 2, 3, None, 5, None, 7]
root = create_tree_from_list(lst)

# Function to traverse and print in-order
def inorder_traversal(node):
    #TODO

# Print the tree using in-order traversal
print("In-order traversal:")
inorder_traversal(root)
print()

