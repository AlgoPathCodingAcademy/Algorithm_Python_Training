# ------------------------------------------------------------
# tiny tree helper
# ------------------------------------------------------------
class Node:
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right


# ------------------------------------------------------------
# To Complete this function
# ------------------------------------------------------------
def max_root_leaf(node):
    """
    Maximum sum of any path that starts at this node and
    follows child links downward to a leaf.
    """


# ------------------------------------------------------------
# TEST CASES
# ------------------------------------------------------------
def build_cases():
    """returns list[(root, expected_sum, human_name)]"""
    cases = []

    # 0. empty tree  →  sum = 0  (define however you like)
    cases.append((None, 0, "empty tree"))

    # 1. single node
    cases.append((Node(5), 5, "single node 5"))

    # 2. balanced three-node tree
    #          10
    #        /    \
    #       5     15
    cases.append((Node(10, Node(5), Node(15)), 25, "10-5-15"))

    # 3. left-skewed chain
    #     2
    #    /
    #   3
    #  /
    # 4
    cases.append((Node(2, Node(3, Node(4))), 9, "left chain 2-3-4"))

    # 4. negative & positive mix (classic LeetCode 124 shape)
    #       -10
    #      /    \
    #     9     20
    #          /  \
    #         7   -25
    # best root→leaf is -10 + 20 + 7 = 17
    cases.append((
        Node(-10,
             Node(9),
             Node(20, Node(7), Node(-25))
        ),
        17,
        "mixed negatives"
    ))

    return cases


# ------------------------------------------------------------
# TEST RUNNER
# ------------------------------------------------------------
def run_tests(getSumTree):
    """
    getSumTree must be a function node -> int.
    Prints PASS / FAIL per case and summary at the end.
    """
    cases = build_cases()
    passed = 0

    for root, expected, name in cases:
        want = expected
        got  = getSumTree(root)
        if got == want:
            print(f"✅  PASS  ({name:>15}) → {got}")
            passed += 1
        else:
            print(f"❌  FAIL  ({name:>15}) → got {got}, expected {want}")

    print(f"\n{passed}/{len(cases)} tests passed.")


# ------------------------------------------------------------
# QUICK DEMO
# ------------------------------------------------------------
if __name__ == "__main__":

    getSumTree = max_root_leaf

    try:
        getSumTree
    except NameError:
        raise SystemExit(
            "Please import or define your getSumTree(node) function before running."
        )

    run_tests(getSumTree)

