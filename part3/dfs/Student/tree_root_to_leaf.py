from typing import List, Optional, Set, Tuple

# ────── data structure ──────
class Node:
    def __init__(self, val: int,
                 left: Optional["Node"] = None,
                 right: Optional["Node"] = None):
        self.val = val
        self.left = left
        self.right = right

# Only consider perfect binary tree
def root_to_leaf_paths(root):
    """Return all root-to-leaf paths as lists of values."""
    

# ────── helper for comparison ──────
def canonical(paths: List[List[int]]) -> Set[Tuple[int, ...]]:
    """Convert list-of-lists to a set of tuples so order doesn’t matter."""
    return {tuple(p) for p in paths}

# ────── build test fixtures ──────
# 5. perfect depth-3 tree
#        1
#      /   \
#     2     3
#    / \   / \
#   4   5 6   7
perfect = Node(1,
               Node(2, Node(4), Node(5)),
               Node(3, Node(6), Node(7)))

# ────── expected answers ──────
tests = [
    ("perfect",     perfect,
     [[1, 2, 4], [1, 2, 5], [1, 3, 6], [1, 3, 7]]),
]

# ────── run the assertions ──────
for name, tree, expected in tests:
    got = root_to_leaf_paths(tree)
    if canonical(got) != canonical(expected):
        raise AssertionError(
            f"{name} failed:\n"
            f"  expected {expected}\n"
            f"  got      {got}"
        )

print("All tests passed!")
