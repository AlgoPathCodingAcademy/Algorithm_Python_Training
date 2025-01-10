import heapq

def dijkstra_shortest_path(n, adjacency_list, source, destination):
    """
    Find the shortest distance from 'source' to 'destination' using Dijkstra's Algorithm.
    
    Parameters:
    - n               : number of vertices (labeled from 0 to n-1)
    - adjacency_list  : adjacency_list[u] = list of (v, w) indicating an edge u->v with weight w
    - source          : the starting vertex
    - destination     : the target vertex

    Returns:
    - The shortest distance from 'source' to 'destination' if it exists,
      or float('inf') if 'destination' is not reachable.
    """

def run_dijkstra_tests():
    """
    Runs 10 test cases to verify 'dijkstra_shortest_path'.
    Prints PASS or FAIL for each test.
    """

    test_cases = []

    # -----------------
    # TEST CASE 1
    # -----------------
    # Graph Description:
    #   0 --2--1
    #    \     / \
    #   (5)  (1)  (6)
    #      \ /     \
    #       2 --2--3 --3--4
    #
    # Shortest path from 0 to 4 is 0->1->2->3->4 with total weight 8
    #
    # ASCII Diagram:
    #
    #     (2)
    #   0 ----- 1
    #    \     / \
    #   (5)  (1)  (6)
    #       \ /     \
    #        2 --2--3 --3--4

    test_case_1 = {
        "n": 5,
        "adjacency_list": {
            0: [(1, 2), (2, 5)],
            1: [(0, 2), (2, 1), (3, 6)],
            2: [(0, 5), (1, 1), (3, 2)],
            3: [(1, 6), (2, 2), (4, 3)],
            4: [(3, 3)]
        },
        "source": 0,
        "destination": 4,
        "expected": 8
    }

    # -----------------
    # TEST CASE 2
    # -----------------
    # Graph Description:
    #    0 --1--1
    #    |     |
    #   (4)   (2)
    #    |     |
    #    2 --3--3 --4--5
    #        |  \
    #       (2) (1)
    #        |    \
    #        4-----5
    #
    # Shortest path from 0 to 5 is 0->1->2->4->5 with total weight 9
    #
    # ASCII Diagram:
    #
    #      (1)
    #     0 --- 1
    #      \     \
    #     (4)    (2)
    #        \     \
    #         2 --3--3 --4--5
    #             |  \
    #            (2) (1)
    #             |    \
    #             4-----5

    test_case_2 = {
        "n": 6,
        "adjacency_list": {
            0: [(1, 1), (2, 4)],
            1: [(0, 1), (2, 2), (3, 7)],
            2: [(0, 4), (1, 2), (3, 3), (4, 5)],
            3: [(1, 7), (2, 3), (4, 2), (5, 4)],
            4: [(2, 5), (3, 2), (5, 1)],
            5: [(3, 4), (4, 1)]
        },
        "source": 0,
        "destination": 5,
        "expected": 9
    }

    # -----------------
    # TEST CASE 3
    # -----------------
    # Graph Description:
    #     0 --2--1
    #      \     |
    #     (7)   (3)
    #        \   |
    #         2 --3--1--4
    #
    # Shortest path from 0 to 4 is 0->1->3->4 with total weight 6
    #
    # ASCII Diagram:
    #
    #     (2)
    #    0 --- 1
    #     \     |
    #    (7)   (3)
    #        \   |
    #         2 --3--1--4

    test_case_3 = {
        "n": 5,
        "adjacency_list": {
            0: [(1, 2), (2, 7)],
            1: [(0, 2), (3, 3)],
            2: [(0, 7), (3, 2)],
            3: [(1, 3), (2, 2), (4, 1)],
            4: [(3, 1)]
        },
        "source": 0,
        "destination": 4,
        "expected": 6
    }

    # -----------------
    # TEST CASE 4
    # -----------------
    # Graph Description:
    #       (1)
    #     0 ----- 1
    #      |     |
    #    (5)   (2)
    #      |     |
    #      3 -----2
    #       (3)
    #
    # Shortest path from 0 to 2 is 0->1->2 with total weight 3
    #
    # ASCII Diagram:
    #
    #     (1)
    #   0 ----- 1
    #    |     |
    #   (5)   (2)
    #    |     |
    #    3 -----2
    #     (3)

    test_case_4 = {
        "n": 4,
        "adjacency_list": {
            0: [(1, 1), (3, 5)],
            1: [(0, 1), (2, 2)],
            2: [(1, 2), (3, 3)],
            3: [(0, 5), (2, 3)]
        },
        "source": 0,
        "destination": 2,
        "expected": 3  # Path 0->1->2 = 1 + 2 = 3
    }

    # -----------------
    # TEST CASE 5
    # -----------------
    # Graph Description:
    #       1
    #       |
    #     (2)
    #    / | \
    #  0  (5) 2
    #    \ | /
    #     (4) 3
    #       \
    #       (1)
    #         \
    #          4
    #
    # Shortest path from 0 to 4 is 0->4 with total weight 3
    #
    # ASCII Diagram:
    #
    #        1
    #        |
    #      (2)
    #     / | \
    #   0  (5) 2
    #     \ | /
    #      (4) 3
    #        \
    #        (1)
    #          \
    #           4

    test_case_5 = {
        "n": 5,
        "adjacency_list": {
            0: [(1, 2), (2, 5), (3, 4), (4, 3)],
            1: [(0, 2)],
            2: [(0, 5)],
            3: [(0, 4)],
            4: [(0, 3)]
        },
        "source": 0,
        "destination": 4,
        "expected": 3  # Direct path 0->4 with weight 3
    }

    # -----------------
    # TEST CASE 6
    # -----------------
    # Graph Description:
    #    0 --1--1 --2--2 --3--3 --4--4 --5--5
    #
    # Shortest path from 0 to 5 is 0->1->2->3->4->5 with total weight 15
    #
    # ASCII Diagram:
    #
    #    0 --1--1 --2--2 --3--3 --4--4 --5--5

    test_case_6 = {
        "n": 6,
        "adjacency_list": {
            0: [(1, 1)],
            1: [(0, 1), (2, 2)],
            2: [(1, 2), (3, 3)],
            3: [(2, 3), (4, 4)],
            4: [(3, 4), (5, 5)],
            5: [(4, 5)]
        },
        "source": 0,
        "destination": 5,
        "expected": 15  # Path 0->1->2->3->4->5 = 1 + 2 + 3 + 4 + 5 = 15
    }

    # -----------------
    # TEST CASE 7
    # -----------------
    # Graph Description:
    #   Component A:
    #     0 --1--1 --1--2 --1--3
    #   
    #   Component B:
    #     4 --2--5 --2--6
    #
    # Shortest path from 0 to 3 is 0->1->2->3 with total weight 3
    #
    # ASCII Diagram:
    #
    #   Component A:
    #     0 --1--1 --1--2 --1--3
    #
    #   Component B:
    #     4 --2--5 --2--6

    test_case_7 = {
        "n": 7,
        "adjacency_list": {
            0: [(1, 1)],
            1: [(0, 1), (2, 1)],
            2: [(1, 1), (3, 1)],
            3: [(2, 1)],
            4: [(5, 2)],
            5: [(4, 2), (6, 2)],
            6: [(5, 2)]
        },
        "source": 0,
        "destination": 3,
        "expected": 3  # Path 0->1->2->3 with total weight 3
    }

    # -----------------
    # TEST CASE 8
    # -----------------
    # Graph Description:
    #   Component A:
    #     0 --1--1 --1--2 --1--3
    #   
    #   Component B:
    #     4 --2--5 --2--6
    #
    # Shortest path from 0 to 5 is unreachable, expected float('inf')
    #
    # ASCII Diagram:
    #
    #   Component A:
    #     0 --1--1 --1--2 --1--3
    #
    #   Component B:
    #     4 --2--5 --2--6

    test_case_8 = {
        "n": 7,
        "adjacency_list": {
            0: [(1, 1)],
            1: [(0, 1), (2, 1)],
            2: [(1, 1), (3, 1)],
            3: [(2, 1)],
            4: [(5, 2)],
            5: [(4, 2), (6, 2)],
            6: [(5, 2)]
        },
        "source": 0,
        "destination": 5,
        "expected": float('inf')  # No path from 0's component to 5's component
    }

    # -----------------
    # TEST CASE 9
    # -----------------
    # Graph Description:
    #      (2)
    #    0 -----1
    #     |      \
    #    (6)     (1)
    #     |        \
    #     4 --3--3 --2
    #      \      /
    #     (3)  (4)
    #
    # Shortest path from 1 to 4 is 1->3->4 with total weight 4
    #
    # ASCII Diagram:
    #
    #       (2)
    #     0 -----1
    #      |      \
    #    (6)     (1)
    #      |        \
    #      4 --3--3 --2
    #       \      /
    #      (3)  (4)

    test_case_9 = {
        "n": 5,
        "adjacency_list": {
            0: [(1, 2), (4, 6)],
            1: [(0, 2), (2, 4), (3, 1)],
            2: [(1, 4), (3, 2)],
            3: [(1, 1), (2, 2), (4, 3)],
            4: [(0, 6), (3, 3)]
        },
        "source": 1,
        "destination": 4,
        "expected": 4  # Path 1->3->4 with total weight 1 + 3 = 4
    }

    # -----------------
    # TEST CASE 10
    # -----------------
    # Graph Description:
    #        1
    #        |
    #      (2)
    #     / | \
    #   0  (5) 2
    #     \ | /
    #      (4) 3
    #        | \
    #      (1) (5)
    #         \  \
    #         4 --5
    #
    # Shortest path from 0 to 5 is 0->3->4->5 with total weight 5 + 1 + 2 = 8
    #
    # ASCII Diagram:
    #
    #         1
    #         |
    #       (2)
    #      / | \
    #    0  (5) 2
    #      \ | /
    #       (4) 3
    #         | \
    #        (1) (5)
    #           \  \
    #            4 --5

    test_case_10 = {
        "n": 6,
        "adjacency_list": {
            0: [(1, 1), (2, 4), (3, 2)],
            1: [(0, 1), (3, 2)],
            2: [(0, 4), (3, 3)],
            3: [(0, 2), (1, 2), (2, 3), (4, 1), (5, 5)],
            4: [(3, 1), (5, 2)],
            5: [(3, 5), (4, 2)]
        },
        "source": 0,
        "destination": 5,
        "expected": 5  # Path 0->3->4->5 = 2 + 1 + 2 = 5
    }

    # Add all test cases to the list
    test_cases.extend([
        test_case_1,
        test_case_2,
        test_case_3,
        test_case_4,
        test_case_5,
        test_case_6,
        test_case_7,
        test_case_8,
        test_case_9,
        test_case_10
    ])

    # Run tests
    for i, tc in enumerate(test_cases, 1):
        result = dijkstra_shortest_path(
            tc["n"],
            tc["adjacency_list"],
            tc["source"],
            tc["destination"]
        )

        # Determine if the test passed
        if tc["expected"] == float('inf'):
            pass_condition = result == float('inf')
        else:
            pass_condition = result == tc["expected"]

        if pass_condition:
            print(f"Test {i}: PASS")
        else:
            expected = tc["expected"]
            got = result
            print(f"Test {i}: FAIL (expected {expected}, got {got})")


if __name__ == "__main__":
    run_dijkstra_tests()

