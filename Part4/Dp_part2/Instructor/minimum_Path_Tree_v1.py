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
lst = [5, 3, 7, 2, None, None,6, 4, 1, 8, 3]
root = create_tree_from_list(lst)

min_sum = float("inf")

def sum_tree_path(root, path):
    global min_sum
    
    if root == None:
        return
        
    if root.left == None and root.right == None:
        total = sum(path)
        if total + root.value < min_sum:
            min_sum = total + root.value

    sum_tree_path(root.left, path+[root.value])
    sum_tree_path(root.right, path+[root.value])

sum_tree_path(root,[])
print(min_sum)
